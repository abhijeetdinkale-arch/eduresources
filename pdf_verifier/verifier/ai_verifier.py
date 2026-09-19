"""
AI Verifier
===========
Uses Google Gemini API to verify statements, formulas, and factual claims
that cannot be algebraically verified by SymPy.

For each item it returns:
    {
        "status": "correct" | "error" | "uncertain",
        "explanation": str
    }

Items are batched per page to reduce API call overhead.
"""

import json
import time
from typing import Optional
from google import genai
from google.genai import types


# System prompt for the verification model
SYSTEM_PROMPT = """You are a rigorous academic fact-checker and mathematics expert.
You will be given content extracted from a PDF textbook — it may contain:
- Mathematical formulas and equations
- Factual statements
- Definitions
- Scientific claims

Your task is to verify whether each item is CORRECT, INCORRECT (ERROR), or UNCERTAIN.

Respond ONLY with a valid JSON array matching this exact schema:
[
  {
    "line_number": <int>,
    "status": "correct" | "error" | "uncertain",
    "explanation": "<brief explanation — only for errors or uncertain items>"
  }
]

Rules:
- Be strict. If a formula or fact is wrong, mark it as "error".
- If you cannot confidently verify (ambiguous context, undefined variable, etc.), mark "uncertain".
- For trivially correct items (clear, well-known facts), mark "correct" with explanation "".
- Explanation must be concise (max 2 sentences).
- Do NOT include any text outside the JSON array.
"""


def _build_batch_prompt(items: list[dict]) -> str:
    """Build a prompt string for a batch of items."""
    lines = ["Verify each of the following items from a textbook:\n"]
    for item in items:
        lines.append(
            f"[Line {item['line_number']}] ({item['type']}) {item['content']}"
        )
    return "\n".join(lines)


def _parse_ai_response(response_text: str, items: list[dict]) -> list[dict]:
    """Parse the AI JSON response into a list of results."""
    try:
        # Strip markdown code fences if present
        text = response_text.strip()
        if text.startswith("```"):
            text = re.sub(r"^```[a-z]*\n?", "", text)
            text = re.sub(r"\n?```$", "", text)

        data = json.loads(text)
        results = {}
        for entry in data:
            results[entry["line_number"]] = {
                "status": entry.get("status", "uncertain"),
                "explanation": entry.get("explanation", ""),
            }
        # Fill in uncertain for any missing items
        for item in items:
            if item["line_number"] not in results:
                results[item["line_number"]] = {
                    "status": "uncertain",
                    "explanation": "AI did not return a result for this item",
                }
        return results

    except (json.JSONDecodeError, KeyError, TypeError):
        # If parsing fails, mark all as uncertain
        return {
            item["line_number"]: {
                "status": "uncertain",
                "explanation": "AI response could not be parsed",
            }
            for item in items
        }


import re

BATCH_SIZE = 30   # items per API call
RETRY_DELAY = 2   # seconds between retries
MAX_RETRIES = 3


class AIVerifier:
    def __init__(self, api_key: str, verbose: bool = False):
        self.verbose = verbose
        self._client = genai.Client(api_key=api_key)
        self._model = "gemini-2.0-flash"
        self._cache: dict[str, dict] = {}  # content hash → result

    def verify(self, item: dict) -> dict:
        """Verify a single item. Uses cache to avoid duplicate API calls."""
        cache_key = f"{item['type']}::{item['content']}"
        if cache_key in self._cache:
            return self._cache[cache_key]

        # Single-item call (used when called from main.py item-by-item)
        result = self._verify_batch([item]).get(item["line_number"], {
            "status": "uncertain",
            "explanation": "AI verification failed",
        })
        self._cache[cache_key] = result
        return result

    def verify_page(self, items: list[dict]) -> dict[int, dict]:
        """
        Verify all items on a page in batches.
        Returns a dict mapping line_number → result.
        """
        all_results = {}
        for i in range(0, len(items), BATCH_SIZE):
            batch = items[i : i + BATCH_SIZE]
            batch_results = self._verify_batch(batch)
            all_results.update(batch_results)
        return all_results

    def _verify_batch(self, items: list[dict]) -> dict[int, dict]:
        """Send a batch of items to Gemini and return results."""
        prompt = _build_batch_prompt(items)

        for attempt in range(MAX_RETRIES):
            try:
                response = self._client.models.generate_content(
                    model=self._model,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        temperature=0.1,   # low temperature for factual accuracy
                        max_output_tokens=4096,
                    ),
                )
                text = response.text
                if self.verbose:
                    print(f"      [AI] Batch of {len(items)} → response received")
                return _parse_ai_response(text, items)

            except Exception as e:
                if attempt < MAX_RETRIES - 1:
                    if self.verbose:
                        print(f"      [AI] Error (attempt {attempt + 1}): {e}. Retrying...")
                    time.sleep(RETRY_DELAY * (attempt + 1))
                else:
                    return {
                        item["line_number"]: {
                            "status": "uncertain",
                            "explanation": f"AI verification failed after {MAX_RETRIES} attempts: {e}",
                        }
                        for item in items
                    }
