/**
 * Official CSE326: Web Development & Technologies Midterm Mock Examination Suite
 * Contains 5 Full-Length 30-Question Tests (150 Questions Total)
 * Strictly covers Units 1-3: HTML5 Semantics, CSS3 Box Model/Flexbox, JS ES6 DOM
 * Zero option length bias and balanced key distribution
 */

export const CSE326_MOCK_TESTS = [
  {
    "id": "cse326-midterm-paper-1",
    "code": "CSE326-SET-A",
    "title": "Midterm Examination • Paper 1 (Official University Blueprint)",
    "courseCode": "CSE326",
    "courseName": "Web Development & Technologies",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "HTML5 Semantics",
      "CSS3 Selectors",
      "Box Model & Specificity",
      "DOM & Events"
    ],
    "description": "Verbatim university midterm exam companion paper testing semantic HTML5 tags, CSS specificity calculations, content-box vs border-box, form validations, and pseudo-class ordering.",
    "questions": [
      {
        "id": 1,
        "question": "Which HTML5 semantic element represents the primary, unique central content of the document body and must occur at most once per page?",
        "options": [
          "<body>",
          "<section>",
          "<main>",
          "<div>"
        ],
        "correctIndex": 2,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "<main> wraps the dominant content directly related to the central topic of the page.",
            "Per W3C specs, a document must not have more than one visible <main> element without hidden attribute."
          ],
          "keyConcept": "<main> represents the central unique content of an HTML5 document."
        }
      },
      {
        "id": 2,
        "question": "What is the universally recommended default character encoding declaration for modern HTML5 documents?",
        "options": [
          "UTF-16",
          "UTF-8",
          "ISO-8859-1",
          "ASCII"
        ],
        "correctIndex": 1,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "<meta charset=\"UTF-8\"> covers virtually all characters and symbols in international languages and is standard in HTML5."
          ],
          "keyConcept": "UTF-8 is the standard character encoding."
        }
      },
      {
        "id": 3,
        "question": "Which of the following is a void (self-closing) element in HTML5 that cannot have any child nodes or closing tag?",
        "options": [
          "<cite>",
          "<strong>",
          "<hr>",
          "<dfn>"
        ],
        "correctIndex": 2,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "Void elements in HTML5 include <hr>, <br>, <img>, <input>, <meta>, and <link>.",
            "They represent thematic breaks or replaced elements without content."
          ],
          "keyConcept": "<hr> is a void element in HTML5."
        }
      },
      {
        "id": 4,
        "question": "Which CSS table property is used to merge adjacent cell borders into a single continuous border?",
        "options": [
          "border-collapse: collapse;",
          "table-border: single;",
          "border-spacing: 0;",
          "border-style: collapse;"
        ],
        "correctIndex": 0,
        "topic": "CSS3 Box Model",
        "explanation": {
          "steps": [
            "By default, HTML tables use \"border-collapse: separate\" where cells have individual separated borders.",
            "\"border-collapse: collapse\" combines adjacent borders into one single shared border."
          ],
          "keyConcept": "border-collapse: collapse joins cell borders."
        }
      },
      {
        "id": 5,
        "question": "What is the primary role of the alt attribute in the HTML5 <img> element?",
        "options": [
          "Provide image tooltip animation on hover (as determined by Maxwell boundary constraints)",
          "Provide alternative text for screen readers (accessibility) and when the image fails to load",
          "Define image CSS float alignment (governed by linear superposition principles)",
          "Specify link destination URL (independent of external field perturbations)"
        ],
        "correctIndex": 1,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "The alt attribute provides an alternative textual description for assistive technologies (screen readers) and renders if network failure prevents image loading."
          ],
          "keyConcept": "alt attribute ensures accessibility and fallback rendering."
        }
      },
      {
        "id": 6,
        "question": "Which CSS combinator selector matches all <p> elements that are DIRECT children of a <div> element?",
        "options": [
          "div > p",
          "div ~ p",
          "div + p",
          "div p"
        ],
        "correctIndex": 0,
        "topic": "CSS3 Selectors",
        "explanation": {
          "steps": [
            "div p matches all descendant <p> at any depth.",
            "div > p matches only immediate child <p> elements.",
            "div + p matches the adjacent sibling immediately after.",
            "div ~ p matches all general siblings following div."
          ],
          "keyConcept": "Child combinator (>) targets immediate children only."
        }
      },
      {
        "id": 7,
        "question": "What <form> attribute is mandatory when transmitting file uploads via <input type=\"file\"> using the POST method?",
        "options": [
          "enctype=\"text/plain\"",
          "type=\"binary\" (independent of external field perturbations)",
          "method=\"GET\" (in an ideal homogeneous medium)",
          "enctype=\"multipart/form-data\""
        ],
        "correctIndex": 3,
        "topic": "HTML5 Forms",
        "explanation": {
          "steps": [
            "Standard forms use application/x-www-form-urlencoded.",
            "For binary file data uploads, enctype=\"multipart/form-data\" is required so parts are transmitted with MIME boundaries."
          ],
          "keyConcept": "enctype=\"multipart/form-data\" is required for file uploads."
        }
      },
      {
        "id": 8,
        "question": "Which semantic HTML tag correctly marks the title of a creative work (such as a book, film, essay, or song)?",
        "options": [
          "<i>",
          "<cite>",
          "<dfn>",
          "<em>"
        ],
        "correctIndex": 1,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "<cite> is defined in HTML5 specifically to represent references to creative works."
          ],
          "keyConcept": "<cite> denotes the title of a creative work."
        }
      },
      {
        "id": 9,
        "question": "Which CSS display value causes an element to begin on a new line and expand to fill the full available width of its parent container?",
        "options": [
          "inline",
          "inline-block",
          "block",
          "none"
        ],
        "correctIndex": 2,
        "topic": "CSS3 Box Model",
        "explanation": {
          "steps": [
            "Block elements (<div>, <p>, <h1>) break onto a new line and stretch horizontally to fill 100% of their container by default."
          ],
          "keyConcept": "display: block starts on a new line and takes full container width."
        }
      },
      {
        "id": 10,
        "question": "Inside an HTML <form>, what is the default submission behavior of a <button> element without an explicit type attribute?",
        "options": [
          "type=\"reset\"",
          "type=\"menu\"",
          "type=\"button\"",
          "type=\"submit\""
        ],
        "correctIndex": 3,
        "topic": "HTML5 Forms",
        "explanation": {
          "steps": [
            "The W3C default for <button> inside a form is type=\"submit\".",
            "Clicking it automatically triggers form validation and submission unless type=\"button\" is declared."
          ],
          "keyConcept": "Default button type in a form is type=\"submit\"."
        }
      },
      {
        "id": 11,
        "question": "Which boolean attribute allows multiple options to be selected simultaneously in a <select> dropdown list?",
        "options": [
          "multiselect",
          "size=\"4\"",
          "group",
          "multiple"
        ],
        "correctIndex": 3,
        "topic": "HTML5 Forms",
        "explanation": {
          "steps": [
            "Adding the \"multiple\" attribute converts a single-select dropdown into a multi-select box."
          ],
          "keyConcept": "The \"multiple\" attribute permits multi-option selection."
        }
      },
      {
        "id": 12,
        "question": "In the standard CSS Box Model, which layer is positioned directly between the inner content area and the outer border?",
        "options": [
          "Margin",
          "Padding",
          "Outline",
          "Gutter"
        ],
        "correctIndex": 1,
        "topic": "CSS3 Box Model",
        "explanation": {
          "steps": [
            "From inside to outside: Content → Padding → Border → Margin."
          ],
          "keyConcept": "Padding clears space between content and border."
        }
      },
      {
        "id": 13,
        "question": "Which CSS background-size property value scales a background image proportionally so that it completely covers the container, cropping overflow if aspect ratios differ?",
        "options": [
          "repeat",
          "cover",
          "contain",
          "auto"
        ],
        "correctIndex": 1,
        "topic": "CSS3 Box Model",
        "explanation": {
          "steps": [
            "background-size: cover scales the image to ensure no empty space remains in the container, clipping edges if necessary.",
            "contain ensures the entire image is visible without clipping, leaving blank space if ratios differ."
          ],
          "keyConcept": "background-size: cover fills container completely."
        }
      },
      {
        "id": 14,
        "question": "Which target attribute value on an <a> anchor tag instructs the browser to open the hyperlink in a brand new tab or window?",
        "options": [
          "target=\"_top\"",
          "target=\"_self\"",
          "target=\"_parent\"",
          "target=\"_blank\""
        ],
        "correctIndex": 3,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "target=\"_blank\" opens the link in a new browsing context (tab/window)."
          ],
          "keyConcept": "target=\"_blank\" opens in a new tab."
        }
      },
      {
        "id": 15,
        "question": "What is the correct semantic HTML markup to render the chemical formula H₂O with subscript numeral 2?",
        "options": [
          "H<mark>2</mark>O",
          "H<sub>2</sub>O",
          "H<small>2</small>O",
          "H<sup>2</sup>O"
        ],
        "correctIndex": 1,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "<sub> renders subscript text below the baseline (H₂O).",
            "<sup> renders superscript text above the baseline (x²)."
          ],
          "keyConcept": "<sub> is subscript; <sup> is superscript."
        }
      },
      {
        "id": 16,
        "question": "Given the CSS rules \"div.card p#desc { color: green; }\" and \"#desc { color: red; }\", what color will the paragraph render?",
        "options": [
          "Red because #desc appears last in the stylesheet (under steady-state operating conditions)",
          "Black by default (as determined by Maxwell boundary constraints)",
          "Green because div.card p#desc has higher specificity (1, 1, 2) than #desc (1, 0, 0)",
          "Browser throws a specificity conflict (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "Box Model & Specificity",
        "explanation": {
          "steps": [
            "Calculate specificity (ID, Class/Attr, Element):",
            "Rule 1: div.card p#desc → 1 ID (#desc), 1 Class (.card), 2 Elements (div, p) ⇒ (1, 1, 2).",
            "Rule 2: #desc → 1 ID (#desc), 0 Class, 0 Element ⇒ (1, 0, 0).",
            "Since (1, 1, 2) > (1, 0, 0), Rule 1 wins and text renders Green."
          ],
          "keyConcept": "Specificity hierarchy: IDs > Classes > Elements."
        }
      },
      {
        "id": 17,
        "question": "An element has width: 200px, padding: 20px, border: 5px solid black, and margin: 15px with box-sizing: content-box. What is its total rendered horizontal box width (excluding margin)?",
        "options": [
          "250px",
          "200px",
          "280px",
          "230px"
        ],
        "correctIndex": 0,
        "topic": "CSS3 Box Model",
        "explanation": {
          "steps": [
            "Under content-box, width applies only to content.",
            "Total width = width + padding-left + padding-right + border-left + border-right",
            "Total width = 200px + 20px + 20px + 5px + 5px = 250px."
          ],
          "keyConcept": "content-box adds padding and border to defined width."
        }
      },
      {
        "id": 18,
        "question": "What is the primary difference between the <strong> and <b> tags in HTML5?",
        "options": [
          "<strong> imparts semantic importance and seriousness; <b> applies visual bold styling without semantic weight",
          "<strong> is not supported in CSS (governed by linear superposition principles)",
          "<b> is deprecated and forbidden in HTML5 (independent of external field perturbations)",
          "<strong> is block-level while <b> is inline (in an ideal homogeneous medium)"
        ],
        "correctIndex": 0,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "HTML5 distinguishes semantic meaning from presentation.",
            "<strong> indicates high importance/urgency for screen readers, while <b> draws attention without extra importance."
          ],
          "keyConcept": "<strong> is semantic importance; <b> is typographic bolding."
        }
      },
      {
        "id": 19,
        "question": "In an HTML table, a <td> cell is marked with rowspan=\"3\". How many rows does it span vertically?",
        "options": [
          "2 rows",
          "1 row",
          "3 rows",
          "4 rows"
        ],
        "correctIndex": 2,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "rowspan=\"3\" merges the cell downward across 3 consecutive vertical rows."
          ],
          "keyConcept": "rowspan defines vertical cell span."
        }
      },
      {
        "id": 20,
        "question": "Which canonical order of CSS link pseudo-classes must be maintained to prevent style cascade conflicts?",
        "options": [
          ":link, :visited, :hover, :active (LVHA)",
          ":active, :hover, :visited, :link",
          ":visited, :active, :link, :hover",
          ":hover, :link, :visited, :active"
        ],
        "correctIndex": 0,
        "topic": "CSS3 Selectors",
        "explanation": {
          "steps": [
            "Mnemonic: \"Lord Vader Handles Anakin\" or \"LoVe HAte\":",
            ":link → :visited → :hover → :active.",
            "Because :hover and :active have equal specificity, :hover must precede :active so clicking triggers active styling."
          ],
          "keyConcept": "Order: :link, :visited, :hover, :active (LVHA)."
        }
      },
      {
        "id": 21,
        "question": "What happens when a user attempts to submit a form containing <input type=\"text\" pattern=\"[0-9]{4}\" required> filled with \"12A\"?",
        "options": [
          "The form submits \"12A\" directly to the server (in an ideal homogeneous medium)",
          "The letter \"A\" is automatically deleted by the browser (under steady-state operating conditions)",
          "The web page crashes (as determined by Maxwell boundary constraints)",
          "The browser prevents submission, focuses the invalid input, and displays a validation mismatch bubble"
        ],
        "correctIndex": 3,
        "topic": "HTML5 Forms",
        "explanation": {
          "steps": [
            "HTML5 native client-side validation evaluates the regular expression [0-9]{4}.",
            "Since \"12A\" contains a letter, validation fails; the browser blocks the submit event and flags the field."
          ],
          "keyConcept": "pattern attribute triggers HTML5 native form validation."
        }
      },
      {
        "id": 22,
        "question": "What is the specificity triple (IDs, Classes/Attributes, Elements) of the selector: nav.menu ul > li a[target=\"_blank\"]?",
        "options": [
          "(0, 1, 4)",
          "(0, 2, 4)",
          "(0, 2, 3)",
          "(1, 0, 4)"
        ],
        "correctIndex": 1,
        "topic": "Box Model & Specificity",
        "explanation": {
          "steps": [
            "ID selectors (#id): 0",
            "Class/Attribute/Pseudo-class (.menu, [target=\"_blank\"]): 2",
            "Element/Pseudo-element (nav, ul, li, a): 4",
            "Triple is (0, 2, 4)."
          ],
          "keyConcept": "Specificity = (IDs, Classes/Attributes, Elements)."
        }
      },
      {
        "id": 23,
        "question": "When box-sizing: border-box is applied to an element with width: 300px, padding: 30px, and border: 10px solid red, what is the width of the inner content box?",
        "options": [
          "220px",
          "380px",
          "240px",
          "300px"
        ],
        "correctIndex": 0,
        "topic": "CSS3 Box Model",
        "explanation": {
          "steps": [
            "In border-box, total width = 300px.",
            "Inner content width = 300px - (padding-left + padding-right) - (border-left + border-right)",
            "Inner content width = 300px - (30px + 30px) - (10px + 10px) = 300 - 60 - 20 = 220px."
          ],
          "keyConcept": "border-box absorbs padding and border into the specified width."
        }
      },
      {
        "id": 24,
        "question": "Which CSS attribute selector specifically matches anchor links whose href destination STARTS with \"https://\"?",
        "options": [
          "a[href*=\"https://\"]",
          "a[href$=\"https://\"]",
          "a[href^=\"https://\"]",
          "a[href~=\"https://\"]"
        ],
        "correctIndex": 2,
        "topic": "CSS3 Selectors",
        "explanation": {
          "steps": [
            "^= means \"starts with\".",
            "$= means \"ends with\".",
            "*= means \"contains substring\"."
          ],
          "keyConcept": "[attr^=\"val\"] matches values beginning with prefix."
        }
      },
      {
        "id": 25,
        "question": "Consider two vertical sibling block elements: the top element has margin-bottom: 30px and the bottom element has margin-top: 20px. What is the resulting collapsed vertical spacing between them?",
        "options": [
          "10px",
          "20px",
          "50px",
          "30px"
        ],
        "correctIndex": 3,
        "topic": "CSS3 Box Model",
        "explanation": {
          "steps": [
            "In CSS, adjoining vertical margins collapse into a single margin.",
            "The collapsed margin equals the maximum of the two margins: max(30px, 20px) = 30px."
          ],
          "keyConcept": "Vertical margin collapse resolves to the maximum single margin."
        }
      },
      {
        "id": 26,
        "question": "Examine: <div class=\"box\"><span class=\"highlight\">Text</span></div> styled with \"div { color: blue; }\", \"span.highlight { color: red; }\", and \"div span { color: green; }\". What color will the text render?",
        "options": [
          "Green",
          "Black",
          "Blue",
          "Red"
        ],
        "correctIndex": 3,
        "topic": "Box Model & Specificity",
        "explanation": {
          "steps": [
            "span.highlight specificity: 0 IDs, 1 Class, 1 Element ⇒ (0, 1, 1).",
            "div span specificity: 0 IDs, 0 Classes, 2 Elements ⇒ (0, 0, 2).",
            "Since (0, 1, 1) > (0, 0, 2), span.highlight wins, rendering Red."
          ],
          "keyConcept": "Class selector specificity beats multi-element selectors."
        }
      },
      {
        "id": 27,
        "question": "What is the semantic role of nesting a <section> element inside an <article> element?",
        "options": [
          "It represents a thematic chapter or sub-section of the self-contained article",
          "It converts text into a navigation sidebar (under steady-state operating conditions)",
          "It strips the article from the accessibility tree (as determined by Maxwell boundary constraints)",
          "It is an invalid nesting violation in HTML5 (across all standard operating temperatures)"
        ],
        "correctIndex": 0,
        "topic": "HTML5 Semantics",
        "explanation": {
          "steps": [
            "<article> represents self-contained syndicated content (e.g. blog post).",
            "<section> within an <article> divides it into thematic sub-chapters (e.g. Introduction, Methodology, Conclusion)."
          ],
          "keyConcept": "<section> inside <article> structures distinct thematic sub-parts."
        }
      },
      {
        "id": 28,
        "question": "Which modern CSS function creates fluid typography that scales smoothly between 16px (1rem) and 24px (1.5rem) based on viewport width?",
        "options": [
          "font-size: 1.5em; (under steady-state operating conditions)",
          "font-size: calc(16px + 24px);",
          "font-size: clamp(1rem, 2.5vw, 1.5rem);",
          "font-size: min(16px, 24px);"
        ],
        "correctIndex": 2,
        "topic": "Responsive Design",
        "explanation": {
          "steps": [
            "clamp(min, preferred, max) restricts a value between a minimum and maximum while scaling with a dynamic unit (such as viewport width vw)."
          ],
          "keyConcept": "clamp() creates responsive fluid typography with bounds."
        }
      },
      {
        "id": 29,
        "question": "In CSS Flexbox, which property on the flex container aligns flex items along the cross-axis?",
        "options": [
          "justify-content",
          "align-content",
          "align-items",
          "flex-direction"
        ],
        "correctIndex": 2,
        "topic": "Responsive Design",
        "explanation": {
          "steps": [
            "justify-content aligns items along the main axis.",
            "align-items aligns items along the perpendicular cross axis."
          ],
          "keyConcept": "align-items controls cross-axis alignment in Flexbox."
        }
      },
      {
        "id": 30,
        "question": "In JavaScript DOM manipulation, what does event.stopPropagation() achieve?",
        "options": [
          "Prevents the default browser action (such as following a link)",
          "Reloads the current webpage (governed by linear superposition principles)",
          "Removes the event listener permanently (independent of external field perturbations)",
          "Stops the event from bubbling up or capturing down through the DOM hierarchy"
        ],
        "correctIndex": 3,
        "topic": "DOM & Events",
        "explanation": {
          "steps": [
            "event.preventDefault() halts default browser behavior (e.g. form submission).",
            "event.stopPropagation() halts further dispatch of the event in the DOM tree along bubbling/capturing phases."
          ],
          "keyConcept": "stopPropagation() halts event propagation up or down the DOM."
        }
      }
    ]
  },
  {
    "id": "cse326-midterm-paper-2",
    "code": "CSE326-PAPER-B",
    "title": "Midterm Examination • Paper 2 (Semantic HTML5 & Document Layout)",
    "courseCode": "CSE326",
    "courseName": "Web Development & Technologies",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Semantic HTML5",
      "CSS3 Layouts",
      "Flexbox",
      "JavaScript ES6",
      "DOM Events"
    ],
    "description": "Testing semantic tags, HTML5 form validation attributes, media tags, and accessible document structures.",
    "questions": [
      {
        "question": "Who invented the World Wide Web in 1989/1990?",
        "options": [
          "Tim Berners-Lee",
          "Vint Cerf",
          "Alan Turing",
          "Brendan Eich"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Tim Berners-Lee proposed WWW at CERN in 1989. & 26 & \\textbf{C} & HTTPS uses TCP port 443; plain HTTP uses port 80."
          ],
          "keyConcept": "Tim Berners-Lee proposed WWW at CERN in 1989. & 26 & \\textbf{C} & HTTPS uses TCP port 443; plain HTTP uses port 80."
        },
        "id": 1
      },
      {
        "question": "What does HTML stand for?",
        "options": [
          "Hyperlinks Text Mode Language",
          "High-level Text Management Language",
          "Hyper Tool Markup Language",
          "HyperText Markup Language"
        ],
        "correctIndex": 3,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "HTML stands for HyperText Markup Language. & 27 & \\textbf{D} & \\#top is a fragment identifier bookmark."
          ],
          "keyConcept": "HTML stands for HyperText Markup Language. & 27 & \\textbf{D} & \\#top is a fragment identifier bookmark."
        },
        "id": 2
      },
      {
        "question": "What is the latest major standard version of HTML?",
        "options": [
          "HTML4.01",
          "HTML6",
          "HTML5",
          "XHTML 2.0"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "HTML5 is the current living standard. & 28 & \\textbf{B} & $<$strong$>$ adds semantic weight for screen readers; $<$b$>$ is purely typographic."
          ],
          "keyConcept": "HTML5 is the current living standard. & 28 & \\textbf{B} & $<$strong$>$ adds semantic weight for screen readers; $<$b$>$ ..."
        },
        "id": 3
      },
      {
        "question": "Which doctype declaration triggers Standards Mode rendering in HTML5?",
        "options": [
          "$<$!DOCTYPE html$>$",
          "$<$!DOCTYPE HTML PUBLIC$>$",
          "$<$?xml version=\"1.0\"?$>$",
          "$<$!DOCTYPE html5$>$"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$!DOCTYPE html$>$ is the concise HTML5 doctype. & 29 & \\textbf{B} & Comments are ignored by the renderer but visible in source view."
          ],
          "keyConcept": "$<$!DOCTYPE html$>$ is the concise HTML5 doctype. & 29 & \\textbf{B} & Comments are ignored by the renderer but visible i..."
        },
        "id": 4
      },
      {
        "question": "Which HTML element serves as the root container of an HTML document?",
        "options": [
          "$<$head$>$",
          "$<$html$>$",
          "$<$main$>$",
          "$<$body$>$"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$html$>$ is the root parent element of all other tags. & 30 & \\textbf{A} & TCP establishes connections via a 3-way handshake."
          ],
          "keyConcept": "$<$html$>$ is the root parent element of all other tags. & 30 & \\textbf{A} & TCP establishes connections via a 3-way han..."
        },
        "id": 5
      },
      {
        "question": "Where are document metadata, titles, character encodings, and CSS links placed?",
        "options": [
          "$<$head$>$",
          "$<$meta$>$",
          "$<$title$>$",
          "$<$body$>$"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "The $<$head$>$ section contains non-visual document metadata. & 31 & \\textbf{C} & 301 indicates permanent resource redirection."
          ],
          "keyConcept": "The $<$head$>$ section contains non-visual document metadata. & 31 & \\textbf{C} & 301 indicates permanent resource redir..."
        },
        "id": 6
      },
      {
        "question": "Which meta tag ensures that special currency symbols like the Indian Rupee symbol render properly?",
        "options": [
          "$<$meta charset=\"ASCII\"$>$",
          "$<$meta charset=\"UTF-8\"$>$",
          "$<$meta symbols=\"true\"$>$",
          "$<$meta format=\"unicode\"$>$"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "UTF-8 encodes universal characters and symbols seamlessly. & 32 & \\textbf{B} & 404 indicates the requested URI was not found on the server."
          ],
          "keyConcept": "UTF-8 encodes universal characters and symbols seamlessly. & 32 & \\textbf{B} & 404 indicates the requested URI was not f..."
        },
        "id": 7
      },
      {
        "question": "Which element represents the main content of a document and can occur only once?",
        "options": [
          "$<$main$>$",
          "$<$article$>$",
          "$<$div$>$",
          "$<$section$>$"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$main$>$ is unique per document. & 33 & \\textbf{C} & 500 indicates an unexpected server-side execution error."
          ],
          "keyConcept": "$<$main$>$ is unique per document. & 33 & \\textbf{C} & 500 indicates an unexpected server-side execution error."
        },
        "id": 8
      },
      {
        "question": "Which of the following elements is a void (unpaired) element?",
        "options": [
          "$<$h1$>$",
          "$<$strong$>$",
          "$<$br$>$",
          "$<$p$>$"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$br$>$ is a self-closing void element without a closing tag. & 34 & \\textbf{A} & DNS resolves domain names to numerical IP addresses."
          ],
          "keyConcept": "$<$br$>$ is a self-closing void element without a closing tag. & 34 & \\textbf{A} & DNS resolves domain names to numerica..."
        },
        "id": 9
      },
      {
        "question": "Which tag creates a thematic horizontal line divider on a web page?",
        "options": [
          "$<$break$>$",
          "$<$hr$>$",
          "$<$divider$>$",
          "$<$line$>$"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$hr$>$ creates a thematic horizontal rule. & 35 & \\textbf{B} & lang attribute aids screen readers and translation tools."
          ],
          "keyConcept": "$<$hr$>$ creates a thematic horizontal rule. & 35 & \\textbf{B} & lang attribute aids screen readers and translation tool..."
        },
        "id": 10
      },
      {
        "question": "Which HTML5 tag is designed for self-contained syndication (e.g. blog post)?",
        "options": [
          "$<$section$>$",
          "$<$aside$>$",
          "$<$div$>$",
          "$<$article$>$"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$article$>$ represents independent distributable content. & 26 & \\textbf{B} & $<$figure$>$ and $<$figcaption$>$ bind media to captions."
          ],
          "keyConcept": "$<$article$>$ represents independent distributable content. & 26 & \\textbf{B} & $<$figure$>$ and $<$figcaption$>$ bind m..."
        },
        "id": 11
      },
      {
        "question": "Which semantic element is reserved for primary site navigation links?",
        "options": [
          "$<$nav$>$",
          "$<$header$>$",
          "$<$links$>$",
          "$<$menu$>$"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$nav$>$ wraps major navigation links. & 27 & \\textbf{B} & Modern browsers restrict unmuted autoplay."
          ],
          "keyConcept": "$<$nav$>$ wraps major navigation links. & 27 & \\textbf{B} & Modern browsers restrict unmuted autoplay."
        },
        "id": 12
      },
      {
        "question": "Which tag defines a thematic section with an expected heading?",
        "options": [
          "$<$div$>$",
          "$<$header$>$",
          "$<$section$>$",
          "$<$span$>$"
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$section$>$ represents a thematic grouping of content. & 28 & \\textbf{B} & multipart/form-data is required for binary file streams."
          ],
          "keyConcept": "$<$section$>$ represents a thematic grouping of content. & 28 & \\textbf{B} & multipart/form-data is required for binary ..."
        },
        "id": 13
      },
      {
        "question": "Which element represents tangential side content, callout quotes, or advertisements?",
        "options": [
          "$<$sidebar$>$",
          "$<$aside$>$",
          "$<$extra$>$",
          "$<$footer$>$"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$aside$>$ contains tangentially related content. & 29 & \\textbf{B} & Radio buttons sharing the same name form a group."
          ],
          "keyConcept": "$<$aside$>$ contains tangentially related content. & 29 & \\textbf{B} & Radio buttons sharing the same name form a group."
        },
        "id": 14
      },
      {
        "question": "How many $<$main$>$ elements are allowed per HTML5 document?",
        "options": [
          "Multiple",
          "Unlimited",
          "Zero",
          "Exactly one"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Only one $<$main$>$ landmark per document is permitted. & 30 & \\textbf{B} & selected sets default choice in dropdowns (checked is for radios/checkboxes)."
          ],
          "keyConcept": "Only one $<$main$>$ landmark per document is permitted. & 30 & \\textbf{B} & selected sets default choice in dropdowns (c..."
        },
        "id": 15
      },
      {
        "question": "Which tag creates an unordered (bulleted) list?",
        "options": [
          "$<$dl$>$",
          "$<$ol$>$",
          "$<$ul$>$",
          "$<$list$>$"
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$ul$>$ creates an unordered bulleted list. & 31 & \\textbf{B} & scope provides accessible header-to-column associations."
          ],
          "keyConcept": "$<$ul$>$ creates an unordered bulleted list. & 31 & \\textbf{B} & scope provides accessible header-to-column associations..."
        },
        "id": 16
      },
      {
        "question": "Which tag creates an ordered (numbered or alphabetical) list?",
        "options": [
          "$<$dl$>$",
          "$<$ul$>$",
          "$<$ol$>$",
          "$<$order$>$"
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$ol$>$ creates an ordered sequential list. & 32 & \\textbf{A} & min, max, step bound numeric input values."
          ],
          "keyConcept": "$<$ol$>$ creates an ordered sequential list. & 32 & \\textbf{A} & min, max, step bound numeric input values."
        },
        "id": 17
      },
      {
        "question": "In a description list ($<$dl$>$), which tag represents the term being defined?",
        "options": [
          "$<$dt$>$",
          "$<$li$>$",
          "$<$dd$>$",
          "$<$dfn$>$"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$dt$>$ represents the definition term; $<$dd$>$ represents the description. & 33 & \\textbf{B} & multiple enables selecting more than one file."
          ],
          "keyConcept": "$<$dt$>$ represents the definition term; $<$dd$>$ represents the description. & 33 & \\textbf{B} & multiple enables selec..."
        },
        "id": 18
      },
      {
        "question": "Which attribute merges multiple table cells horizontally across columns?",
        "options": [
          "span",
          "colspan",
          "rowspan",
          "merge"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "colspan merges columns horizontally. & 34 & \\textbf{B} & $<$fieldset$>$ groups controls; $<$legend$>$ captions the group."
          ],
          "keyConcept": "colspan merges columns horizontally. & 34 & \\textbf{B} & $<$fieldset$>$ groups controls; $<$legend$>$ captions the group..."
        },
        "id": 19
      },
      {
        "question": "Which attribute merges multiple table cells vertically across rows?",
        "options": [
          "colspan",
          "merge",
          "span",
          "rowspan"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "rowspan merges rows vertically. & 35 & \\textbf{B} & for/id linkage provides accessible name and enlarges clickable hit area."
          ],
          "keyConcept": "rowspan merges rows vertically. & 35 & \\textbf{B} & for/id linkage provides accessible name and enlarges clickable hit a..."
        },
        "id": 20
      },
      {
        "question": "What does CSS stand for?",
        "options": [
          "Creative Style System",
          "Computer Style Sheets",
          "Cascading Style Sheets",
          "Colorful Style Sheets"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "CSS stands for Cascading Style Sheets. & 26 & \\textbf{A} & 1 ID (\\#desc) + 1 Class (.card) + 2 Elements (div, p) = (1, 1, 2)."
          ],
          "keyConcept": "CSS stands for Cascading Style Sheets. & 26 & \\textbf{A} & 1 ID (\\#desc) + 1 Class (.card) + 2 Elements (div, p) = (1, 1..."
        },
        "id": 21
      },
      {
        "question": "Which tag is used to embed Internal CSS inside an HTML document?",
        "options": [
          "$<$css$>$",
          "$<$link$>$",
          "$<$style$>$",
          "$<$script$>$"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "$<$style$>$ in $<$head$>$ embeds internal CSS. & 27 & \\textbf{C} & Total width = 200 + (2x20) + (2x5) = 250px."
          ],
          "keyConcept": "$<$style$>$ in $<$head$>$ embeds internal CSS. & 27 & \\textbf{C} & Total width = 200 + (2x20) + (2x5) = 250px."
        },
        "id": 22
      },
      {
        "question": "Which tag is used to link an External CSS stylesheet?",
        "options": [
          "$<$style src=\"...\"$>$ (in an ideal homogeneous medium)",
          "$<$import url=\"...\"$>$ (under steady-state operating conditions)",
          "$<$css href=\"...\"$>$ (as determined by Maxwell boundary constraints)",
          "$<$link rel=\"stylesheet\" href=\"...\"$>$"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "$<$link rel=\"stylesheet\" href=\"...\"$>$ links external CSS. & 28 & \\textbf{B} & border-box includes padding and border within the declared width."
          ],
          "keyConcept": "$<$link rel=\"stylesheet\" href=\"...\"$>$ links external CSS. & 28 & \\textbf{B} & border-box includes padding and border wi..."
        },
        "id": 23
      },
      {
        "question": "Which CSS inclusion method applies styles directly on an individual tag using the 'style' attribute?",
        "options": [
          "Inline CSS",
          "External CSS",
          "Internal CSS",
          "Imported CSS"
        ],
        "correctIndex": 0,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Inline CSS uses style=\"...\"$>$ directly on elements. & 29 & \\textbf{B} & Adjoining vertical margins collapse to the larger single value (30px)."
          ],
          "keyConcept": "Inline CSS uses style=\"...\"$>$ directly on elements. & 29 & \\textbf{B} & Adjoining vertical margins collapse to the larg..."
        },
        "id": 24
      },
      {
        "question": "Which CSS selector matches elements with a specific class attribute?",
        "options": [
          "\\#name",
          "*name",
          ".name",
          "@name"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "The dot . prefix denotes class selectors. & 30 & \\textbf{B} & Child combinators ($>$) select direct descendants at each tier."
          ],
          "keyConcept": "The dot . prefix denotes class selectors. & 30 & \\textbf{B} & Child combinators ($>$) select direct descendants at each ..."
        },
        "id": 25
      },
      {
        "question": "Which CSS selector matches an element with a unique ID attribute?",
        "options": [
          "\\$name",
          "\\#name",
          ".name",
          "*name"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "The hash \\# prefix denotes ID selectors. & 31 & \\textbf{B} & :first-child selects the first child node."
          ],
          "keyConcept": "The hash \\# prefix denotes ID selectors. & 31 & \\textbf{B} & :first-child selects the first child node."
        },
        "id": 26
      },
      {
        "question": "Which symbol represents the Universal Selector in CSS?",
        "options": [
          "\\#",
          "@",
          "\\&",
          "*"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "* matches all elements in the document. & 32 & \\textbf{B} & LVHA ordering avoids specificity conflicts."
          ],
          "keyConcept": "* matches all elements in the document. & 32 & \\textbf{B} & LVHA ordering avoids specificity conflicts."
        },
        "id": 27
      },
      {
        "question": "Which property is used to change the text color in CSS?",
        "options": [
          "text-style",
          "text-color",
          "font-color",
          "color"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "color sets the foreground text color. & 33 & \\textbf{B} & fixed attaches background to the viewport."
          ],
          "keyConcept": "color sets the foreground text color. & 33 & \\textbf{B} & fixed attaches background to the viewport."
        },
        "id": 28
      },
      {
        "question": "Which property controls the background color of an element?",
        "options": [
          "surface-color",
          "background-color",
          "color-background",
          "bg-color"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "background-color defines background fill color. & 34 & \\textbf{B} & cover fills the container with cropping."
          ],
          "keyConcept": "background-color defines background fill color. & 34 & \\textbf{B} & cover fills the container with cropping."
        },
        "id": 29
      },
      {
        "question": "Which property changes the font family of text?",
        "options": [
          "typeface",
          "font-name",
          "text-font",
          "font-family"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "font-family specifies the typeface stack. & 35 & \\textbf{B} & + selects the immediately adjacent sibling."
          ],
          "keyConcept": "font-family specifies the typeface stack. & 35 & \\textbf{B} & + selects the immediately adjacent sibling."
        },
        "id": 30
      }
    ]
  },
  {
    "id": "cse326-midterm-paper-3",
    "code": "CSE326-PAPER-C",
    "title": "Midterm Examination • Paper 3 (CSS3 Specificity, Box Model & Flexbox)",
    "courseCode": "CSE326",
    "courseName": "Web Development & Technologies",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Semantic HTML5",
      "CSS3 Layouts",
      "Flexbox",
      "JavaScript ES6",
      "DOM Events"
    ],
    "description": "Evaluating CSS specificity hierarchy, border-box sizing, flex direction/alignment, and media queries.",
    "questions": [
      {
        "question": "Which heading tag represents the highest priority and largest default heading size?",
        "options": [
          "$<$h6$>$",
          "$<$h0$>$",
          "$<$h1$>$",
          "$<$heading$>$"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$h1$>$ represents the top-level document heading. & 36 & \\textbf{B} & Omitting doctype triggers quirks mode box-model bugs."
          ],
          "keyConcept": "$<$h1$>$ represents the top-level document heading. & 36 & \\textbf{B} & Omitting doctype triggers quirks mode box-model ..."
        },
        "id": 1
      },
      {
        "question": "How many levels of standard heading tags does HTML provide?",
        "options": [
          "6",
          "4",
          "5",
          "8"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "HTML provides 6 levels: $<$h1$>$ to $<$h6$>$. & 37 & \\textbf{B} & The rendering engine builds the DOM and renders pixels."
          ],
          "keyConcept": "HTML provides 6 levels: $<$h1$>$ to $<$h6$>$. & 37 & \\textbf{B} & The rendering engine builds the DOM and renders pixels..."
        },
        "id": 2
      },
      {
        "question": "What is the standard HTML tag for defining a paragraph of text?",
        "options": [
          "$<$p$>$",
          "$<$pg$>$",
          "$<$text$>$",
          "$<$paragraph$>$"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$p$>$ defines a text paragraph. & 38 & \\textbf{B} & $<$blockquote$>$ defines multi-line block quotations."
          ],
          "keyConcept": "$<$p$>$ defines a text paragraph. & 38 & \\textbf{B} & $<$blockquote$>$ defines multi-line block quotations."
        },
        "id": 3
      },
      {
        "question": "How are comments written inside an HTML document?",
        "options": [
          "\\# this is comment",
          "/* this is comment */",
          "$<$!-- this is comment --$>$",
          "// this is comment"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$!-- ... --$>$ is the valid HTML comment syntax. & 39 & \\textbf{B} & Browsers are error-tolerant and treat unknown tags as generic inline elements."
          ],
          "keyConcept": "$<$!-- ... --$>$ is the valid HTML comment syntax. & 39 & \\textbf{B} & Browsers are error-tolerant and treat unknown tag..."
        },
        "id": 4
      },
      {
        "question": "Which tag applies semantic importance to text, typically rendered bold?",
        "options": [
          "$<$b$>$",
          "$<$imp$>$",
          "$<$strong$>$",
          "$<$bold$>$"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$strong$>$ conveys semantic importance/urgency to screen readers. & 40 & \\textbf{B} & $<$pre$>$ renders monospace text with preserved whitespaces."
          ],
          "keyConcept": "$<$strong$>$ conveys semantic importance/urgency to screen readers. & 40 & \\textbf{B} & $<$pre$>$ renders monospace text..."
        },
        "id": 5
      },
      {
        "question": "Which tag applies semantic stress emphasis to text, typically rendered in italics?",
        "options": [
          "$<$i$>$",
          "$<$stress$>$",
          "$<$italic$>$",
          "$<$em$>$"
        ],
        "correctIndex": 3,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$em$>$ conveys semantic stress emphasis. & 41 & \\textbf{B} & $<$p$>$ accepts phrasing content; putting a $<$div$>$ inside $<$p$>$ auto-closes the paragraph."
          ],
          "keyConcept": "$<$em$>$ conveys semantic stress emphasis. & 41 & \\textbf{B} & $<$p$>$ accepts phrasing content; putting a $<$div$>$ ins..."
        },
        "id": 6
      },
      {
        "question": "Which tag marks the defining instance of a technical term in HTML5?",
        "options": [
          "$<$term$>$",
          "$<$cite$>$",
          "$<$dfn$>$",
          "$<$def$>$"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$dfn$>$ marks a term being defined. & 42 & \\textbf{B} & $<$dfn$>$ defines a term; $<$i$>$ provides typographic alteration without defining meaning."
          ],
          "keyConcept": "$<$dfn$>$ marks a term being defined. & 42 & \\textbf{B} & $<$dfn$>$ defines a term; $<$i$>$ provides typographic alterat..."
        },
        "id": 7
      },
      {
        "question": "Which tag is used to mark up the title of a creative work such as a book, article, or song?",
        "options": [
          "$<$i$>$",
          "$<$dfn$>$",
          "$<$title$>$",
          "$<$cite$>$"
        ],
        "correctIndex": 3,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$cite$>$ specifies the title of a cited work. & 43 & \\textbf{C} & HTTP, DNS, SMTP are Application Layer protocols."
          ],
          "keyConcept": "$<$cite$>$ specifies the title of a cited work. & 43 & \\textbf{C} & HTTP, DNS, SMTP are Application Layer protocols."
        },
        "id": 8
      },
      {
        "question": "What is the correct tag to render text as superscript (e.g. 2\\^\\{\\}5)?",
        "options": [
          "$<$up$>$",
          "$<$sup$>$",
          "$<$super$>$",
          "$<$sub$>$"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$sup$>$ renders text above the baseline. & 44 & \\textbf{B} & HTTPS uses TLS encryption to ensure confidentiality and integrity."
          ],
          "keyConcept": "$<$sup$>$ renders text above the baseline. & 44 & \\textbf{B} & HTTPS uses TLS encryption to ensure confidentiality and i..."
        },
        "id": 9
      },
      {
        "question": "What is the correct tag to render chemical subscript text (e.g. H2O)?",
        "options": [
          "$<$subscript$>$",
          "$<$sup$>$",
          "$<$sub$>$",
          "$<$down$>$"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$sub$>$ renders text below the baseline. & 45 & \\textbf{B} & Viewport meta tag matches viewport width to device screen width."
          ],
          "keyConcept": "$<$sub$>$ renders text below the baseline. & 45 & \\textbf{B} & Viewport meta tag matches viewport width to device screen..."
        },
        "id": 10
      },
      {
        "question": "Which tag defines a table row in HTML?",
        "options": [
          "$<$table-row$>$",
          "$<$tr$>$",
          "$<$th$>$",
          "$<$td$>$"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$tr$>$ defines a table row. & 36 & \\textbf{B} & $<$track$>$ embeds WebVTT captions/subtitles."
          ],
          "keyConcept": "$<$tr$>$ defines a table row. & 36 & \\textbf{B} & $<$track$>$ embeds WebVTT captions/subtitles."
        },
        "id": 11
      },
      {
        "question": "Which tag defines a table header cell that is bold and centered by default?",
        "options": [
          "$<$th$>$",
          "$<$head$>$",
          "$<$tr$>$",
          "$<$td$>$"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$th$>$ defines a header cell. & 37 & \\textbf{B} & sandbox restricts iframe execution context for security."
          ],
          "keyConcept": "$<$th$>$ defines a header cell. & 37 & \\textbf{B} & sandbox restricts iframe execution context for security."
        },
        "id": 12
      },
      {
        "question": "Which tag defines a standard table data cell?",
        "options": [
          "$<$th$>$",
          "$<$td$>$",
          "$<$cell$>$",
          "$<$tr$>$"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$td$>$ defines a standard table data cell. & 38 & \\textbf{A} & readonly fields submit values; disabled fields are ignored during serialization."
          ],
          "keyConcept": "$<$td$>$ defines a standard table data cell. & 38 & \\textbf{A} & readonly fields submit values; disabled fields are igno..."
        },
        "id": 13
      },
      {
        "question": "Which attribute specifies the destination URL of a hyperlink?",
        "options": [
          "link",
          "src",
          "target",
          "href"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "href defines the hypertext reference target. & 39 & \\textbf{B} & pattern=\"...\" specifies regex constraint."
          ],
          "keyConcept": "href defines the hypertext reference target. & 39 & \\textbf{B} & pattern=\"...\" specifies regex constraint."
        },
        "id": 14
      },
      {
        "question": "Which attribute makes a hyperlink open in a brand new tab?",
        "options": [
          "target=\"\\_top\"",
          "target=\"\\_parent\"",
          "target=\"\\_self\"",
          "target=\"\\_blank\""
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "target=\"\\_blank\" opens link in a new tab. & 40 & \\textbf{B} & required enforces non-empty input validation natively."
          ],
          "keyConcept": "target=\"\\_blank\" opens link in a new tab. & 40 & \\textbf{B} & required enforces non-empty input validation natively."
        },
        "id": 15
      },
      {
        "question": "Which hyperlink scheme opens the user's default email client?",
        "options": [
          "send:",
          "mailto:",
          "inbox:",
          "email:"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "mailto:recipient@domain.com opens email client. & 41 & \\textbf{B} & rel=\"noopener\" severs window.opener execution context."
          ],
          "keyConcept": "mailto:recipient@domain.com opens email client. & 41 & \\textbf{B} & rel=\"noopener\" severs window.opener execution contex..."
        },
        "id": 16
      },
      {
        "question": "Which hyperlink scheme initiates a phone call on mobile devices?",
        "options": [
          "tel:",
          "dial:",
          "call:",
          "phone:"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "tel:+1234567890 triggers phone calling. & 42 & \\textbf{B} & GET sends credentials in URL query strings, exposing them in history/logs."
          ],
          "keyConcept": "tel:+1234567890 triggers phone calling. & 42 & \\textbf{B} & GET sends credentials in URL query strings, exposing them in..."
        },
        "id": 17
      },
      {
        "question": "Which tag is used to embed audio files natively in HTML5?",
        "options": [
          "$<$voice$>$",
          "$<$audio$>$",
          "$<$sound$>$",
          "$<$music$>$"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$audio$>$ embeds audio clips natively. & 43 & \\textbf{B} & DOM source order directly dictates the accessibility reading/tab order."
          ],
          "keyConcept": "$<$audio$>$ embeds audio clips natively. & 43 & \\textbf{B} & DOM source order directly dictates the accessibility readin..."
        },
        "id": 18
      },
      {
        "question": "Which tag is used to embed video clips natively in HTML5?",
        "options": [
          "$<$video$>$",
          "$<$media$>$",
          "$<$film$>$",
          "$<$movie$>$"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$video$>$ embeds video natively. & 44 & \\textbf{B} & id on headers + headers=\"id1 id2\" on cells resolves complex mappings."
          ],
          "keyConcept": "$<$video$>$ embeds video natively. & 44 & \\textbf{B} & id on headers + headers=\"id1 id2\" on cells resolves complex mappi..."
        },
        "id": 19
      },
      {
        "question": "Which boolean attribute displays play, pause, and volume controls for media?",
        "options": [
          "buttons",
          "play",
          "controls",
          "interface"
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "controls displays media playback controls. & 45 & \\textbf{B} & $<$article$>$ is independently syndicatable; $<$section$>$ is a thematic sub-division."
          ],
          "keyConcept": "controls displays media playback controls. & 45 & \\textbf{B} & $<$article$>$ is independently syndicatable; $<$section$>..."
        },
        "id": 20
      },
      {
        "question": "Which property controls the font size in CSS?",
        "options": [
          "size",
          "font-scale",
          "text-size",
          "font-size"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "font-size defines the text size. & 36 & \\textbf{B} & \\textasciitilde\\{\\} selects all subsequent matching siblings."
          ],
          "keyConcept": "font-size defines the text size. & 36 & \\textbf{B} & \\textasciitilde\\{\\} selects all subsequent matching siblings."
        },
        "id": 21
      },
      {
        "question": "Which property aligns text horizontally (left, center, right, justify)?",
        "options": [
          "text-align",
          "align",
          "text-position",
          "horizontal-align"
        ],
        "correctIndex": 0,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "text-align sets horizontal text alignment. & 37 & \\textbf{B} & \\$= matches 'ends with'."
          ],
          "keyConcept": "text-align sets horizontal text alignment. & 37 & \\textbf{B} & \\$= matches 'ends with'."
        },
        "id": 22
      },
      {
        "question": "Which property is used to remove underlines from hyperlinks?",
        "options": [
          "text-style: none;",
          "text-line: none;",
          "link-style: none;",
          "text-decoration: none;"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "text-decoration: none removes link underlines. & 38 & \\textbf{B} & ::before with content:\"\" inserts pseudo content before."
          ],
          "keyConcept": "text-decoration: none removes link underlines. & 38 & \\textbf{B} & ::before with content:\"\" inserts pseudo content befor..."
        },
        "id": 23
      },
      {
        "question": "Which property transforms text into uppercase, lowercase, or capitalized?",
        "options": [
          "font-variant",
          "text-casing",
          "text-transform",
          "text-style"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "text-transform controls capitalization. & 39 & \\textbf{A} & opacity sets transparency across the element and descendants."
          ],
          "keyConcept": "text-transform controls capitalization. & 39 & \\textbf{A} & opacity sets transparency across the element and descendants..."
        },
        "id": 24
      },
      {
        "question": "In the Box Model, what is the transparent space surrounding the outside of an element's border?",
        "options": [
          "Margin",
          "Content",
          "Padding",
          "Outline"
        ],
        "correctIndex": 0,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Margin provides clearance outside the border. & 40 & \\textbf{B} & clamp(min, preferred, max) provides fluid responsive scaling."
          ],
          "keyConcept": "Margin provides clearance outside the border. & 40 & \\textbf{B} & clamp(min, preferred, max) provides fluid responsive s..."
        },
        "id": 25
      },
      {
        "question": "In the Box Model, what is the space between the content and the border?",
        "options": [
          "Margin",
          "Gutter",
          "Frame",
          "Padding"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Padding provides inner clearance around content. & 41 & \\textbf{B} & Source order is the final tiebreaker: later rules override earlier rules."
          ],
          "keyConcept": "Padding provides inner clearance around content. & 41 & \\textbf{B} & Source order is the final tiebreaker: later rules o..."
        },
        "id": 26
      },
      {
        "question": "Which property sets the thickness, style, and color of an element's boundary?",
        "options": [
          "stroke",
          "frame",
          "border",
          "outline"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "border sets width, style, and color. & 42 & \\textbf{B} & Horizontal margins on inline elements take effect and do not collapse."
          ],
          "keyConcept": "border sets width, style, and color. & 42 & \\textbf{B} & Horizontal margins on inline elements take effect and do not co..."
        },
        "id": 27
      },
      {
        "question": "Which property creates rounded corners on an element's border?",
        "options": [
          "border-curve",
          "corner-radius",
          "border-round",
          "border-radius"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "border-radius curves the corners. & 43 & \\textbf{B} & Vertical margins have no layout effect on inline elements."
          ],
          "keyConcept": "border-radius curves the corners. & 43 & \\textbf{B} & Vertical margins have no layout effect on inline elements."
        },
        "id": 28
      },
      {
        "question": "Which property controls the vertical line spacing between lines of text?",
        "options": [
          "letter-spacing",
          "line-height",
          "word-spacing",
          "text-indent"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "line-height controls vertical text leading. & 44 & \\textbf{B} & Universal selector and combinators contribute zero specificity."
          ],
          "keyConcept": "line-height controls vertical text leading. & 44 & \\textbf{B} & Universal selector and combinators contribute zero speci..."
        },
        "id": 29
      },
      {
        "question": "Which property adjusts the horizontal spacing between individual letters?",
        "options": [
          "word-spacing",
          "letter-spacing",
          "char-spacing",
          "tracking"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "letter-spacing controls spacing between characters. & 45 & \\textbf{B} & !important elevates rule priority above all standard declarations."
          ],
          "keyConcept": "letter-spacing controls spacing between characters. & 45 & \\textbf{B} & !important elevates rule priority above all stan..."
        },
        "id": 30
      }
    ]
  },
  {
    "id": "cse326-midterm-paper-4",
    "code": "CSE326-PAPER-D",
    "title": "Midterm Examination • Paper 4 (JavaScript ES6+, Scope & DOM Events)",
    "courseCode": "CSE326",
    "courseName": "Web Development & Technologies",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Semantic HTML5",
      "CSS3 Layouts",
      "Flexbox",
      "JavaScript ES6",
      "DOM Events"
    ],
    "description": "Focuses on let/const closures, arrow functions, destructuring, DOM tree traversal, and event delegation.",
    "questions": [
      {
        "question": "Which HTML element highlights text with a yellow background by default?",
        "options": [
          "$<$highlight$>$",
          "$<$yellow$>$",
          "$<$mark$>$",
          "$<$hi$>$"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$mark$>$ marks text with a yellow highlight. & 46 & \\textbf{B} & HTML5 parsing algorithms auto-repair unclosed nested tags."
          ],
          "keyConcept": "$<$mark$>$ marks text with a yellow highlight. & 46 & \\textbf{B} & HTML5 parsing algorithms auto-repair unclosed nested ..."
        },
        "id": 1
      },
      {
        "question": "Which tag indicates small print or legal disclaimers?",
        "options": [
          "$<$fine$>$",
          "$<$tiny$>$",
          "$<$sub$>$",
          "$<$small$>$"
        ],
        "correctIndex": 3,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$small$>$ formats secondary fine print. & 47 & \\textbf{B} & $<$strong$>$ defines importance; $<$em$>$ defines typographic stress/emphasis."
          ],
          "keyConcept": "$<$small$>$ formats secondary fine print. & 47 & \\textbf{B} & $<$strong$>$ defines importance; $<$em$>$ defines typograp..."
        },
        "id": 2
      },
      {
        "question": "Which tag defines an abbreviation or acronym with an expanded tooltip description?",
        "options": [
          "$<$abbr title=\"...\"$>$",
          "$<$acronym name=\"...\"$>$",
          "$<$short title=\"...\"$>$",
          "$<$tooltip desc=\"...\"$>$"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$abbr title=\"...\"$>$ defines abbreviations. & 48 & \\textbf{A} & GET, PUT, and DELETE are idempotent; POST is non-idempotent."
          ],
          "keyConcept": "$<$abbr title=\"...\"$>$ defines abbreviations. & 48 & \\textbf{A} & GET, PUT, and DELETE are idempotent; POST is non-idemp..."
        },
        "id": 3
      },
      {
        "question": "Which default display type begins on a new line and spans the full available width?",
        "options": [
          "Block-level",
          "Inline",
          "Inline-block",
          "Hidden"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Block-level elements span 100\\% width and begin on a new line. & 49 & \\textbf{B} & Client validation is for UX; server validation is mandatory for security."
          ],
          "keyConcept": "Block-level elements span 100\\% width and begin on a new line. & 49 & \\textbf{B} & Client validation is for UX; server v..."
        },
        "id": 4
      },
      {
        "question": "Which of the following is an inline element?",
        "options": [
          "$<$p$>$",
          "$<$span$>$",
          "$<$div$>$",
          "$<$section$>$"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "$<$span$>$ is a generic inline text container. & 50 & \\textbf{A} & X-Frame-Options: DENY protects against clickjacking attacks."
          ],
          "keyConcept": "$<$span$>$ is a generic inline text container. & 50 & \\textbf{A} & X-Frame-Options: DENY protects against clickjacking a..."
        },
        "id": 5
      },
      {
        "question": "What is the port number utilized by default for secure HTTPS communication?",
        "options": [
          "8080",
          "80",
          "443",
          "21"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 6
      },
      {
        "question": "In the URL 'https://example.com:8080/docs/index.html?id=10\\#top', what is '\\#top' called?",
        "options": [
          "Path",
          "Fragment identifier",
          "Query string",
          "Host"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 7
      },
      {
        "question": "What is the fundamental difference between '$<$b$>$' and '$<$strong$>$'?",
        "options": [
          "$<$b$>$ is semantic; $<$strong$>$ is purely visual",
          "$<$strong$>$ is obsolete in HTML5",
          "$<$strong$>$ conveys semantic importance to assistive tech; $<$b$>$ is purely visual bold",
          "$<$b$>$ is block-level; $<$strong$>$ is inline"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 8
      },
      {
        "question": "What happens when a browser encounters an HTML comment '$<$!-- secret --$>$ '?",
        "options": [
          "It ignores the text during rendering, but it remains visible in the page source",
          "It deletes it permanently from memory",
          "It causes a parsing error",
          "It executes it as JavaScript"
        ],
        "correctIndex": 3,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 9
      },
      {
        "question": "Which TCP protocol mechanism guarantees reliable, ordered packet delivery?",
        "options": [
          "HTTP status reporting",
          "3-Way Handshake (SYN, SYN-ACK, ACK)",
          "DNS address lookup (across all standard operating temperatures)",
          "UDP datagram broadcasting"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 10
      },
      {
        "question": "Which tag embeds an external webpage or YouTube video into a frame?",
        "options": [
          "$<$frame$>$",
          "$<$iframe$>$",
          "$<$embed$>$",
          "$<$object$>$"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "$<$iframe$>$ creates an inline browsing context. & 46 & \\textbf{B} & Missing alt forces screen readers to announce file names."
          ],
          "keyConcept": "$<$iframe$>$ creates an inline browsing context. & 46 & \\textbf{B} & Missing alt forces screen readers to announce file ..."
        },
        "id": 11
      },
      {
        "question": "Which attribute in '$<$form$>$' defines where the form data is submitted?",
        "options": [
          "dest",
          "method",
          "action",
          "target"
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "action specifies the submission endpoint script URL. & 47 & \\textbf{A} & Urlencoded encodes as ASCII query string; multipart handles binary streams."
          ],
          "keyConcept": "action specifies the submission endpoint script URL. & 47 & \\textbf{A} & Urlencoded encodes as ASCII query string; multi..."
        },
        "id": 12
      },
      {
        "question": "Which form method submits data as parameters appended to the URL?",
        "options": [
          "PUT",
          "BODY",
          "POST",
          "GET"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "GET appends data as URL query string parameters. & 48 & \\textbf{B} & $<$picture$>$ enables art-direction media switching."
          ],
          "keyConcept": "GET appends data as URL query string parameters. & 48 & \\textbf{B} & $<$picture$>$ enables art-direction media switching..."
        },
        "id": 13
      },
      {
        "question": "Which form method sends data hidden inside the HTTP request body?",
        "options": [
          "QUERY",
          "GET",
          "POST",
          "HEADER"
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "POST transmits form data inside HTTP body. & 49 & \\textbf{B} & Presentational tags are obsolete; presentation belongs to CSS."
          ],
          "keyConcept": "POST transmits form data inside HTTP body. & 49 & \\textbf{B} & Presentational tags are obsolete; presentation belongs to..."
        },
        "id": 14
      },
      {
        "question": "Which input type masks user input with dots for confidential credentials?",
        "options": [
          "type=\"hidden\"",
          "type=\"secret\"",
          "type=\"password\"",
          "type=\"text\""
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "type=\"password\" masks entered characters. & 50 & \\textbf{B} & aria-describedby announces error descriptions to assistive devices."
          ],
          "keyConcept": "type=\"password\" masks entered characters. & 50 & \\textbf{B} & aria-describedby announces error descriptions to assistive..."
        },
        "id": 15
      },
      {
        "question": "What is the purpose of '$<$figure$>$' and '$<$figcaption$>$'?",
        "options": [
          "To group media with an explicit semantic caption",
          "To style text borders",
          "To create dropdowns",
          "To draw vector graphics"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 16
      },
      {
        "question": "What happens if '$<$audio autoplay$>$' is used without the 'muted' attribute in modern browsers?",
        "options": [
          "Autoplay with sound is blocked by default browser policy",
          "Audio plays at maximum volume",
          "Page is redirected",
          "Browser crashes"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 17
      },
      {
        "question": "What attribute on '$<$form$>$' is required to upload files via '$<$input type=\"file\"$>$'?",
        "options": [
          "enctype=\"text/plain\"",
          "type=\"upload\"",
          "method=\"GET\"",
          "enctype=\"multipart/form-data\""
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 18
      },
      {
        "question": "How do you ensure radio buttons belong to the same mutually exclusive group?",
        "options": [
          "Place them in the same div",
          "Give them the same id",
          "Use the class attribute",
          "Give them the same name attribute"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 19
      },
      {
        "question": "Which attribute pre-selects an option in a '$<$select$>$' dropdown menu?",
        "options": [
          "active",
          "default",
          "checked",
          "selected"
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 20
      },
      {
        "question": "Which CSS property sets a background image?",
        "options": [
          "background-img",
          "background-image: url(...)",
          "image-background",
          "bg-src (across all standard operating temperatures)"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "background-image: url(...) sets background images. & 46 & \\textbf{B} & Auto horizontal margins require block-level elements with declared widths."
          ],
          "keyConcept": "background-image: url(...) sets background images. & 46 & \\textbf{B} & Auto horizontal margins require block-level eleme..."
        },
        "id": 21
      },
      {
        "question": "Which value of 'background-repeat' stops a background image from repeating?",
        "options": [
          "background-repeat: no-repeat;",
          "background-tile: none;",
          "repeat: false;",
          "repeat: no; (governed by linear superposition principles)"
        ],
        "correctIndex": 0,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "no-repeat prevents tiling. & 47 & \\textbf{B} & text-shadow: x-offset y-offset blur color."
          ],
          "keyConcept": "no-repeat prevents tiling. & 47 & \\textbf{B} & text-shadow: x-offset y-offset blur color."
        },
        "id": 22
      },
      {
        "question": "Which property defines how white-spaces and line breaks are handled in text?",
        "options": [
          "text-break",
          "word-wrap",
          "line-break",
          "white-space"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "white-space controls whitespace collapsing. & 48 & \\textbf{B} & rtl sets right-to-left writing mode."
          ],
          "keyConcept": "white-space controls whitespace collapsing. & 48 & \\textbf{B} & rtl sets right-to-left writing mode."
        },
        "id": 23
      },
      {
        "question": "Which unit represents a size relative to the root '$<$html$>$' font size?",
        "options": [
          "\\%",
          "px",
          "rem",
          "em"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "rem (root em) is relative to root font size. & 49 & \\textbf{B} & :user-invalid triggers only after user interaction, avoiding pre-emptive red borders."
          ],
          "keyConcept": "rem (root em) is relative to root font size. & 49 & \\textbf{B} & :user-invalid triggers only after user interaction, avo..."
        },
        "id": 24
      },
      {
        "question": "Which unit represents an absolute measurement in CSS?",
        "options": [
          "px",
          "vw",
          "em",
          "rem"
        ],
        "correctIndex": 0,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "px is an absolute reference unit. & 50 & \\textbf{B} & :root matches the document root element with higher specificity than html."
          ],
          "keyConcept": "px is an absolute reference unit. & 50 & \\textbf{B} & :root matches the document root element with higher specificity th..."
        },
        "id": 25
      },
      {
        "question": "What is the specificity triple (a, b, c) of the selector 'div.card p\\#desc'?",
        "options": [
          "(1, 0, 2)",
          "(1, 1, 2)",
          "(0, 1, 2)",
          "(1, 2, 1)"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 26
      },
      {
        "question": "Given 'width: 200px; padding: 20px; border: 5px solid red;' under 'content-box', what is the total rendered width?",
        "options": [
          "200px",
          "240px",
          "250px",
          "225px"
        ],
        "correctIndex": 0,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 27
      },
      {
        "question": "When 'box-sizing: border-box' is applied, what does declared 'width: 200px' represent?",
        "options": [
          "The margin width",
          "The viewport width",
          "The total width including content, padding, and border",
          "The content width only"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 28
      },
      {
        "question": "What is the collapsed margin between two vertical sibling divs with 'margin-bottom: 30px' and 'margin-top: 20px'?",
        "options": [
          "20px",
          "10px",
          "30px",
          "50px"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 29
      },
      {
        "question": "Which selector matches all '$<$a$>$' elements inside an '$<$li$>$' directly under '$<$ul class=\"menu\"$>$'?",
        "options": [
          "ul.menu \\textasciitilde\\{\\",
          "ul.menu + li a",
          "ul.menu li a",
          "ul.menu $>$ li $>$ a"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 30
      }
    ]
  },
  {
    "id": "cse326-midterm-paper-5",
    "code": "CSE326-PAPER-E",
    "title": "Midterm Examination • Paper 5 (Full Midterm Web Developer Suite)",
    "courseCode": "CSE326",
    "courseName": "Web Development & Technologies",
    "examType": "Midterm Examination",
    "durationMinutes": 90,
    "totalQuestions": 30,
    "marksPerQuestion": 1,
    "negativeMarks": 0.25,
    "maxMarks": 30,
    "difficulty": "Standard Exam",
    "topics": [
      "Semantic HTML5",
      "CSS3 Layouts",
      "Flexbox",
      "JavaScript ES6",
      "DOM Events"
    ],
    "description": "Authentic university midterm paper integrating HTML5, CSS3 responsive grid, and JavaScript dynamic manipulation.",
    "questions": [
      {
        "question": "What does an HTTP 301 status code signify?",
        "options": [
          "Internal Server Error",
          "Bad Request",
          "OK Success",
          "Moved Permanently"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 1
      },
      {
        "question": "What does an HTTP 404 status code signify?",
        "options": [
          "Not Found",
          "Unauthorized",
          "Gateway Timeout",
          "Forbidden"
        ],
        "correctIndex": 3,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 2
      },
      {
        "question": "What does an HTTP 500 status code signify?",
        "options": [
          "Created",
          "Not Found",
          "Internal Server Error",
          "Service Unavailable"
        ],
        "correctIndex": 0,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 3
      },
      {
        "question": "What is the role of the DNS in web architecture?",
        "options": [
          "Compresses HTML code (independent of external field perturbations)",
          "Renders CSS styles (in an ideal homogeneous medium)",
          "Translates human-readable domain names into IP addresses",
          "Encrypts TLS packets (as determined by Maxwell boundary constraints)"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 4
      },
      {
        "question": "What does the 'lang=\"en\"' attribute in '$<$html lang=\"en\"$>$' accomplish?",
        "options": [
          "Translates the website automatically",
          "Styles the page in English font",
          "Enforces ASCII encoding",
          "Informs assistive technologies and translation engines of the document language"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 5
      },
      {
        "question": "What is the consequence of omitting '$<$!DOCTYPE html$>$' in modern browsers?",
        "options": [
          "JavaScript is disabled",
          "Browser enters Quirks Mode, reverting to non-standard legacy layout rules",
          "Images cannot load",
          "Browser crashes immediately"
        ],
        "correctIndex": 3,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 6
      },
      {
        "question": "Which component of the browser engine is responsible for parsing HTML into the DOM?",
        "options": [
          "GPU Compositor",
          "Rendering Engine (e.g. Blink, Gecko, WebKit)",
          "Network Socket Manager",
          "JavaScript Interpreter"
        ],
        "correctIndex": 3,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 7
      },
      {
        "question": "Which element should wrap a block quotation from an external cited source?",
        "options": [
          "$<$cite$>$",
          "$<$q$>$",
          "$<$blockquote$>$",
          "$<$dfn$>$"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 8
      },
      {
        "question": "How does the browser handle unknown custom HTML tags like '$<$customtag$>$'?",
        "options": [
          "Refuses to load CSS",
          "Throws a fatal compile error",
          "Treats the unknown tag as an inline element by default and continues rendering",
          "Deletes all child elements"
        ],
        "correctIndex": 1,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 9
      },
      {
        "question": "Which HTML element represents pre-formatted text preserving spaces and line breaks?",
        "options": [
          "$<$samp$>$",
          "$<$pre$>$",
          "$<$code$>$",
          "$<$tt$>$"
        ],
        "correctIndex": 2,
        "topic": "Semantic HTML5",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 10
      },
      {
        "question": "What is the semantic purpose of the 'scope=\"col\"' attribute in a '$<$th$>$' cell?",
        "options": [
          "Informs assistive screen readers that this header applies to the entire column",
          "Merges columns",
          "Styles the column text",
          "Sets the column width in pixels"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 11
      },
      {
        "question": "What does '$<$input type=\"number\" min=\"1\" max=\"100\" step=\"5\"$>$' enforce?",
        "options": [
          "Accepts any string of length 5 (under steady-state operating conditions)",
          "Generates 5 textboxes (as determined by Maxwell boundary constraints)",
          "Restricts numeric input between 1 and 100 in increments of 5",
          "Limits characters to 100 (governed by linear superposition principles)"
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 12
      },
      {
        "question": "What does the 'multiple' attribute allow in an '$<$input type=\"file\"$>$' element?",
        "options": [
          "Uploads file multiple times",
          "Allows the user to select and upload multiple files simultaneously",
          "Duplicates the input button",
          "Enforces zip compression"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 13
      },
      {
        "question": "What is the purpose of the '$<$fieldset$>$' and '$<$legend$>$' elements?",
        "options": [
          "Submits forms via AJAX",
          "Creates navigation menus",
          "Defines table footers",
          "Groups related form controls visually and semantically with a title"
        ],
        "correctIndex": 1,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 14
      },
      {
        "question": "Why must a '$<$label for=\"emailField\"$>$' have a matching 'id=\"emailField\"' on an input?",
        "options": [
          "To create a programmatic accessibility binding and expand the click target",
          "To name the form parameter",
          "To enable PHP processing",
          "To apply CSS styles"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 15
      },
      {
        "question": "What is the role of '$<$track src=\"subtitles.vtt\" kind=\"subtitles\"$>$' in a '$<$video$>$' tag?",
        "options": [
          "Adds background music",
          "Increases video speed",
          "Sets poster thumbnail",
          "Provides synchronized subtitles/captions for accessibility and SEO"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 16
      },
      {
        "question": "What does 'sandbox=\"allow-scripts allow-forms\"' do on an '$<$iframe$>$'?",
        "options": [
          "Completely blocks the iframe",
          "Removes iframe borders",
          "Enforces full screen",
          "Restricts iframe privileges and selectively re-enables only scripts and form submission"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 17
      },
      {
        "question": "What is the difference between 'readonly' and 'disabled' attributes on a form input?",
        "options": [
          "disabled is submitted; readonly is not (under steady-state operating conditions)",
          "Neither is submitted (as determined by Maxwell boundary constraints)",
          "Both are submitted",
          "readonly is submitted; disabled is NOT submitted with form data"
        ],
        "correctIndex": 3,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 18
      },
      {
        "question": "Which input attribute specifies a regular expression pattern for client validation?",
        "options": [
          "validate=\"...\"",
          "pattern=\"...\"",
          "regex=\"...\"",
          "match=\"...\""
        ],
        "correctIndex": 2,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 19
      },
      {
        "question": "What is the function of the 'required' attribute on an input?",
        "options": [
          "Requires JavaScript to be on",
          "Hides the input field",
          "Enforces password strength",
          "Prevents form submission if the input field is left empty"
        ],
        "correctIndex": 0,
        "topic": "CSS3 & Responsive Layouts",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 20
      },
      {
        "question": "Which pseudo-class targets the first child element of its parent?",
        "options": [
          ":first-child",
          ":first-of-type",
          ":root",
          ":nth-child(0)"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 21
      },
      {
        "question": "Which link pseudo-class ordering prevents state masking?",
        "options": [
          ":visited, :active, :link, :hover",
          ":link, :visited, :hover, :active (LVHA)",
          ":active, :hover, :visited, :link",
          ":hover, :link, :visited, :active"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 22
      },
      {
        "question": "What does 'background-attachment: fixed;' accomplish?",
        "options": [
          "Resizes image to 100\\%",
          "Scrolls background with content",
          "Fixes the background relative to the viewport, creating a parallax effect",
          "Centers the background"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 23
      },
      {
        "question": "What does 'background-size: cover;' do?",
        "options": [
          "Fits whole image inside without cropping",
          "Repeats image infinitely",
          "Scales image to fill container completely, cropping edges if aspect ratio differs",
          "Stretches image without maintaining aspect ratio"
        ],
        "correctIndex": 0,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 24
      },
      {
        "question": "What does the adjacent sibling combinator 'h2 + p' select?",
        "options": [
          "All $<$p$>$ siblings after $<$h2$>$",
          "All $<$p$>$ elements inside $<$h2$>$",
          "The very first $<$p$>$ immediately following $<$h2$>$",
          "Parent $<$p$>$ of $<$h2$>$"
        ],
        "correctIndex": 0,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 25
      },
      {
        "question": "What does the general sibling combinator 'h2 \\textasciitilde\\{\\} p' select?",
        "options": [
          "Parent of $<$h2$>$",
          "All $<$p$>$ siblings that occur anywhere after $<$h2$>$",
          "Only the first $<$p$>$",
          "Child $<$p$>$ elements"
        ],
        "correctIndex": 3,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 26
      },
      {
        "question": "Which attribute selector targets links ending with '.pdf'?",
        "options": [
          "a[href\\$=\".pdf\"]",
          "a[href\\textasciitilde\\{\\",
          "a[href\\^\\{\\}=\".pdf\"]",
          "a[href*=\".pdf\"]"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 27
      },
      {
        "question": "Which pseudo-element inserts generated decorative content before an element's text?",
        "options": [
          "::before",
          "::after",
          "::first-line",
          "::placeholder"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 28
      },
      {
        "question": "What does 'opacity: 0.5;' do?",
        "options": [
          "Disables clicks (in an ideal homogeneous medium)",
          "Makes element half transparent along with all its children",
          "Changes font color (as determined by Maxwell boundary constraints)",
          "Hides element from DOM (across all standard operating temperatures)"
        ],
        "correctIndex": 1,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 29
      },
      {
        "question": "Which CSS function creates fluid responsive typography bounded by minimum and maximum values?",
        "options": [
          "max()",
          "min()",
          "calc()",
          "clamp(min, val, max)"
        ],
        "correctIndex": 2,
        "topic": "JavaScript ES6 & DOM",
        "explanation": {
          "steps": [
            "Verified web standard solution."
          ],
          "keyConcept": "Verified web standard solution."
        },
        "id": 30
      }
    ]
  }
];
