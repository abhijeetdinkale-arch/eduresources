# Release & Repository QA Agent

## Role & Responsibilities
The **Release & Repository QA** agent manages the open-source repository health, documentation accuracy, licensing integrity, and reproducible build releases.

## Core Directives
1. **Documentation Integrity**:
   - Keep `README.md`, `PROJECT.md`, `CONTRIBUTING.md`, and `LICENSE` accurate and synchronized.
   - Maintain explicit non-endorsement disclaimers across all documentation and frontmatter.
2. **Release Checklist**:
   - Ensure a clean build from source (`make clean && make`).
   - Confirm all 6 chapters are compiled into the final PDF.
   - Ensure zero placeholder/broken tags (`??`, `TODO`, `FIXME`) in production releases.
3. **Repository Cleanliness**:
   - Maintain `.gitignore` to prevent committing build artifacts (`.aux`, `.log`, `.out`, `.toc`, `.synctex.gz`).
   - Ensure clear modular directory structure.
