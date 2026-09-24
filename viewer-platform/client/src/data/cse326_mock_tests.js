/**
 * Official CSE326: Web Development & Technologies Midterm Mock Examination Suite
 * Contains Full-Length 30-Question Tests
 * Modelled on actual University Midterm Examination Papers & Exam Companion
 * Focuses strictly on Units 1-3:
 *   Unit 1: HTML5 Semantic Architecture, Forms, Validations & Media
 *   Unit 2: CSS3 Box Model, Specificity Hierarchy, Selectors & Cascading
 *   Unit 3: Responsive Design, Flexbox Layouts, DOM Manipulation & Events
 * Authentic +1 / -0.25 marking scheme and detailed step-by-step solutions.
 */

export const CSE326_MOCK_TESTS = [
  {
    id: 'cse326-midterm-paper-1',
    code: 'CSE326-SET-A',
    title: 'Midterm Examination • Paper 1 (Official University Blueprint)',
    courseCode: 'CSE326',
    courseName: 'Web Development & Technologies',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['HTML5 Semantics', 'CSS3 Selectors', 'Box Model & Specificity', 'DOM & Events'],
    description: 'Verbatim university midterm exam companion paper testing semantic HTML5 tags, CSS specificity calculations, content-box vs border-box, form validations, and pseudo-class ordering.',
    questions: [
      {
        id: 1,
        question: 'Which HTML5 semantic element represents the primary, unique central content of the document body and must occur at most once per page?',
        options: ['<body>', '<main>', '<section>', '<div>'],
        correctIndex: 1,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            '<main> wraps the dominant content directly related to the central topic of the page.',
            'Per W3C specs, a document must not have more than one visible <main> element without hidden attribute.'
          ],
          keyConcept: '<main> represents the central unique content of an HTML5 document.'
        }
      },
      {
        id: 2,
        question: 'What is the universally recommended default character encoding declaration for modern HTML5 documents?',
        options: ['ASCII', 'UTF-8', 'ISO-8859-1', 'UTF-16'],
        correctIndex: 1,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            '<meta charset="UTF-8"> covers virtually all characters and symbols in international languages and is standard in HTML5.'
          ],
          keyConcept: 'UTF-8 is the standard character encoding.'
        }
      },
      {
        id: 3,
        question: 'Which of the following is a void (self-closing) element in HTML5 that cannot have any child nodes or closing tag?',
        options: ['<dfn>', '<hr>', '<cite>', '<strong>'],
        correctIndex: 1,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            'Void elements in HTML5 include <hr>, <br>, <img>, <input>, <meta>, and <link>.',
            'They represent thematic breaks or replaced elements without content.'
          ],
          keyConcept: '<hr> is a void element in HTML5.'
        }
      },
      {
        id: 4,
        question: 'Which CSS table property is used to merge adjacent cell borders into a single continuous border?',
        options: ['border-style: collapse;', 'border-collapse: collapse;', 'border-spacing: 0;', 'table-border: single;'],
        correctIndex: 1,
        topic: 'CSS3 Box Model',
        explanation: {
          steps: [
            'By default, HTML tables use "border-collapse: separate" where cells have individual separated borders.',
            '"border-collapse: collapse" combines adjacent borders into one single shared border.'
          ],
          keyConcept: 'border-collapse: collapse joins cell borders.'
        }
      },
      {
        id: 5,
        question: 'What is the primary role of the alt attribute in the HTML5 <img> element?',
        options: [
          'Provide image tooltip animation on hover',
          'Provide alternative text for screen readers (accessibility) and when the image fails to load',
          'Define image CSS float alignment',
          'Specify link destination URL'
        ],
        correctIndex: 1,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            'The alt attribute provides an alternative textual description for assistive technologies (screen readers) and renders if network failure prevents image loading.'
          ],
          keyConcept: 'alt attribute ensures accessibility and fallback rendering.'
        }
      },
      {
        id: 6,
        question: 'Which CSS combinator selector matches all <p> elements that are DIRECT children of a <div> element?',
        options: ['div + p', 'div ~ p', 'div > p', 'div p'],
        correctIndex: 2,
        topic: 'CSS3 Selectors',
        explanation: {
          steps: [
            'div p matches all descendant <p> at any depth.',
            'div > p matches only immediate child <p> elements.',
            'div + p matches the adjacent sibling immediately after.',
            'div ~ p matches all general siblings following div.'
          ],
          keyConcept: 'Child combinator (>) targets immediate children only.'
        }
      },
      {
        id: 7,
        question: 'What <form> attribute is mandatory when transmitting file uploads via <input type="file"> using the POST method?',
        options: ['enctype="text/plain"', 'enctype="multipart/form-data"', 'method="GET"', 'type="binary"'],
        correctIndex: 1,
        topic: 'HTML5 Forms',
        explanation: {
          steps: [
            'Standard forms use application/x-www-form-urlencoded.',
            'For binary file data uploads, enctype="multipart/form-data" is required so parts are transmitted with MIME boundaries.'
          ],
          keyConcept: 'enctype="multipart/form-data" is required for file uploads.'
        }
      },
      {
        id: 8,
        question: 'Which semantic HTML tag correctly marks the title of a creative work (such as a book, film, essay, or song)?',
        options: ['<i>', '<em>', '<cite>', '<dfn>'],
        correctIndex: 2,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            '<cite> is defined in HTML5 specifically to represent references to creative works.'
          ],
          keyConcept: '<cite> denotes the title of a creative work.'
        }
      },
      {
        id: 9,
        question: 'Which CSS display value causes an element to begin on a new line and expand to fill the full available width of its parent container?',
        options: ['inline', 'block', 'inline-block', 'none'],
        correctIndex: 1,
        topic: 'CSS3 Box Model',
        explanation: {
          steps: [
            'Block elements (<div>, <p>, <h1>) break onto a new line and stretch horizontally to fill 100% of their container by default.'
          ],
          keyConcept: 'display: block starts on a new line and takes full container width.'
        }
      },
      {
        id: 10,
        question: 'Inside an HTML <form>, what is the default submission behavior of a <button> element without an explicit type attribute?',
        options: ['type="button"', 'type="reset"', 'type="submit"', 'type="menu"'],
        correctIndex: 2,
        topic: 'HTML5 Forms',
        explanation: {
          steps: [
            'The W3C default for <button> inside a form is type="submit".',
            'Clicking it automatically triggers form validation and submission unless type="button" is declared.'
          ],
          keyConcept: 'Default button type in a form is type="submit".'
        }
      },
      {
        id: 11,
        question: 'Which boolean attribute allows multiple options to be selected simultaneously in a <select> dropdown list?',
        options: ['multiselect', 'size="4"', 'multiple', 'group'],
        correctIndex: 2,
        topic: 'HTML5 Forms',
        explanation: {
          steps: [
            'Adding the "multiple" attribute converts a single-select dropdown into a multi-select box.'
          ],
          keyConcept: 'The "multiple" attribute permits multi-option selection.'
        }
      },
      {
        id: 12,
        question: 'In the standard CSS Box Model, which layer is positioned directly between the inner content area and the outer border?',
        options: ['Margin', 'Padding', 'Outline', 'Gutter'],
        correctIndex: 1,
        topic: 'CSS3 Box Model',
        explanation: {
          steps: [
            'From inside to outside: Content → Padding → Border → Margin.'
          ],
          keyConcept: 'Padding clears space between content and border.'
        }
      },
      {
        id: 13,
        question: 'Which CSS background-size property value scales a background image proportionally so that it completely covers the container, cropping overflow if aspect ratios differ?',
        options: ['contain', 'cover', 'auto', 'repeat'],
        correctIndex: 1,
        topic: 'CSS3 Box Model',
        explanation: {
          steps: [
            'background-size: cover scales the image to ensure no empty space remains in the container, clipping edges if necessary.',
            'contain ensures the entire image is visible without clipping, leaving blank space if ratios differ.'
          ],
          keyConcept: 'background-size: cover fills container completely.'
        }
      },
      {
        id: 14,
        question: 'Which target attribute value on an <a> anchor tag instructs the browser to open the hyperlink in a brand new tab or window?',
        options: ['target="_parent"', 'target="_self"', 'target="_blank"', 'target="_top"'],
        correctIndex: 2,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            'target="_blank" opens the link in a new browsing context (tab/window).'
          ],
          keyConcept: 'target="_blank" opens in a new tab.'
        }
      },
      {
        id: 15,
        question: 'What is the correct semantic HTML markup to render the chemical formula H₂O with subscript numeral 2?',
        options: ['H<sup>2</sup>O', 'H<sub>2</sub>O', 'H<small>2</small>O', 'H<mark>2</mark>O'],
        correctIndex: 1,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            '<sub> renders subscript text below the baseline (H₂O).',
            '<sup> renders superscript text above the baseline (x²).'
          ],
          keyConcept: '<sub> is subscript; <sup> is superscript.'
        }
      },
      {
        id: 16,
        question: 'Given the CSS rules "div.card p#desc { color: green; }" and "#desc { color: red; }", what color will the paragraph render?',
        options: [
          'Red because #desc appears last in the stylesheet',
          'Green because div.card p#desc has higher specificity (1, 1, 2) than #desc (1, 0, 0)',
          'Black by default',
          'Browser throws a specificity conflict'
        ],
        correctIndex: 1,
        topic: 'Box Model & Specificity',
        explanation: {
          steps: [
            'Calculate specificity (ID, Class/Attr, Element):',
            'Rule 1: div.card p#desc → 1 ID (#desc), 1 Class (.card), 2 Elements (div, p) ⇒ (1, 1, 2).',
            'Rule 2: #desc → 1 ID (#desc), 0 Class, 0 Element ⇒ (1, 0, 0).',
            'Since (1, 1, 2) > (1, 0, 0), Rule 1 wins and text renders Green.'
          ],
          keyConcept: 'Specificity hierarchy: IDs > Classes > Elements.'
        }
      },
      {
        id: 17,
        question: 'An element has width: 200px, padding: 20px, border: 5px solid black, and margin: 15px with box-sizing: content-box. What is its total rendered horizontal box width (excluding margin)?',
        options: ['200px', '250px', '280px', '230px'],
        correctIndex: 1,
        topic: 'CSS3 Box Model',
        explanation: {
          steps: [
            'Under content-box, width applies only to content.',
            'Total width = width + padding-left + padding-right + border-left + border-right',
            'Total width = 200px + 20px + 20px + 5px + 5px = 250px.'
          ],
          keyConcept: 'content-box adds padding and border to defined width.'
        }
      },
      {
        id: 18,
        question: 'What is the primary difference between the <strong> and <b> tags in HTML5?',
        options: [
          '<strong> is block-level while <b> is inline',
          '<strong> imparts semantic importance and seriousness; <b> applies visual bold styling without semantic weight',
          '<b> is deprecated and forbidden in HTML5',
          '<strong> is not supported in CSS'
        ],
        correctIndex: 1,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            'HTML5 distinguishes semantic meaning from presentation.',
            '<strong> indicates high importance/urgency for screen readers, while <b> draws attention without extra importance.'
          ],
          keyConcept: '<strong> is semantic importance; <b> is typographic bolding.'
        }
      },
      {
        id: 19,
        question: 'In an HTML table, a <td> cell is marked with rowspan="3". How many rows does it span vertically?',
        options: ['1 row', '2 rows', '3 rows', '4 rows'],
        correctIndex: 2,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            'rowspan="3" merges the cell downward across 3 consecutive vertical rows.'
          ],
          keyConcept: 'rowspan defines vertical cell span.'
        }
      },
      {
        id: 20,
        question: 'Which canonical order of CSS link pseudo-classes must be maintained to prevent style cascade conflicts?',
        options: [
          ':hover, :link, :visited, :active',
          ':link, :visited, :hover, :active (LVHA)',
          ':active, :hover, :visited, :link',
          ':visited, :active, :link, :hover'
        ],
        correctIndex: 1,
        topic: 'CSS3 Selectors',
        explanation: {
          steps: [
            'Mnemonic: "Lord Vader Handles Anakin" or "LoVe HAte":',
            ':link → :visited → :hover → :active.',
            'Because :hover and :active have equal specificity, :hover must precede :active so clicking triggers active styling.'
          ],
          keyConcept: 'Order: :link, :visited, :hover, :active (LVHA).'
        }
      },
      {
        id: 21,
        question: 'What happens when a user attempts to submit a form containing <input type="text" pattern="[0-9]{4}" required> filled with "12A"?',
        options: [
          'The form submits "12A" directly to the server',
          'The browser prevents submission, focuses the invalid input, and displays a validation mismatch bubble',
          'The letter "A" is automatically deleted by the browser',
          'The web page crashes'
        ],
        correctIndex: 1,
        topic: 'HTML5 Forms',
        explanation: {
          steps: [
            'HTML5 native client-side validation evaluates the regular expression [0-9]{4}.',
            'Since "12A" contains a letter, validation fails; the browser blocks the submit event and flags the field.'
          ],
          keyConcept: 'pattern attribute triggers HTML5 native form validation.'
        }
      },
      {
        id: 22,
        question: 'What is the specificity triple (IDs, Classes/Attributes, Elements) of the selector: nav.menu ul > li a[target="_blank"]?',
        options: ['(0, 2, 4)', '(0, 1, 4)', '(1, 0, 4)', '(0, 2, 3)'],
        correctIndex: 0,
        topic: 'Box Model & Specificity',
        explanation: {
          steps: [
            'ID selectors (#id): 0',
            'Class/Attribute/Pseudo-class (.menu, [target="_blank"]): 2',
            'Element/Pseudo-element (nav, ul, li, a): 4',
            'Triple is (0, 2, 4).'
          ],
          keyConcept: 'Specificity = (IDs, Classes/Attributes, Elements).'
        }
      },
      {
        id: 23,
        question: 'When box-sizing: border-box is applied to an element with width: 300px, padding: 30px, and border: 10px solid red, what is the width of the inner content box?',
        options: ['300px', '220px', '380px', '240px'],
        correctIndex: 1,
        topic: 'CSS3 Box Model',
        explanation: {
          steps: [
            'In border-box, total width = 300px.',
            'Inner content width = 300px - (padding-left + padding-right) - (border-left + border-right)',
            'Inner content width = 300px - (30px + 30px) - (10px + 10px) = 300 - 60 - 20 = 220px.'
          ],
          keyConcept: 'border-box absorbs padding and border into the specified width.'
        }
      },
      {
        id: 24,
        question: 'Which CSS attribute selector specifically matches anchor links whose href destination STARTS with "https://"?',
        options: ['a[href$="https://"]', 'a[href*="https://"]', 'a[href^="https://"]', 'a[href~="https://"]'],
        correctIndex: 2,
        topic: 'CSS3 Selectors',
        explanation: {
          steps: [
            '^= means "starts with".',
            '$= means "ends with".',
            '*= means "contains substring".'
          ],
          keyConcept: '[attr^="val"] matches values beginning with prefix.'
        }
      },
      {
        id: 25,
        question: 'Consider two vertical sibling block elements: the top element has margin-bottom: 30px and the bottom element has margin-top: 20px. What is the resulting collapsed vertical spacing between them?',
        options: ['50px', '30px', '20px', '10px'],
        correctIndex: 1,
        topic: 'CSS3 Box Model',
        explanation: {
          steps: [
            'In CSS, adjoining vertical margins collapse into a single margin.',
            'The collapsed margin equals the maximum of the two margins: max(30px, 20px) = 30px.'
          ],
          keyConcept: 'Vertical margin collapse resolves to the maximum single margin.'
        }
      },
      {
        id: 26,
        question: 'Examine: <div class="box"><span class="highlight">Text</span></div> styled with "div { color: blue; }", "span.highlight { color: red; }", and "div span { color: green; }". What color will the text render?',
        options: ['Blue', 'Green', 'Red', 'Black'],
        correctIndex: 2,
        topic: 'Box Model & Specificity',
        explanation: {
          steps: [
            'span.highlight specificity: 0 IDs, 1 Class, 1 Element ⇒ (0, 1, 1).',
            'div span specificity: 0 IDs, 0 Classes, 2 Elements ⇒ (0, 0, 2).',
            'Since (0, 1, 1) > (0, 0, 2), span.highlight wins, rendering Red.'
          ],
          keyConcept: 'Class selector specificity beats multi-element selectors.'
        }
      },
      {
        id: 27,
        question: 'What is the semantic role of nesting a <section> element inside an <article> element?',
        options: [
          'It is an invalid nesting violation in HTML5',
          'It represents a thematic chapter or sub-section of the self-contained article',
          'It strips the article from the accessibility tree',
          'It converts text into a navigation sidebar'
        ],
        correctIndex: 1,
        topic: 'HTML5 Semantics',
        explanation: {
          steps: [
            '<article> represents self-contained syndicated content (e.g. blog post).',
            '<section> within an <article> divides it into thematic sub-chapters (e.g. Introduction, Methodology, Conclusion).'
          ],
          keyConcept: '<section> inside <article> structures distinct thematic sub-parts.'
        }
      },
      {
        id: 28,
        question: 'Which modern CSS function creates fluid typography that scales smoothly between 16px (1rem) and 24px (1.5rem) based on viewport width?',
        options: [
          'font-size: calc(16px + 24px);',
          'font-size: clamp(1rem, 2.5vw, 1.5rem);',
          'font-size: min(16px, 24px);',
          'font-size: 1.5em;'
        ],
        correctIndex: 1,
        topic: 'Responsive Design',
        explanation: {
          steps: [
            'clamp(min, preferred, max) restricts a value between a minimum and maximum while scaling with a dynamic unit (such as viewport width vw).'
          ],
          keyConcept: 'clamp() creates responsive fluid typography with bounds.'
        }
      },
      {
        id: 29,
        question: 'In CSS Flexbox, which property on the flex container aligns flex items along the cross-axis?',
        options: ['justify-content', 'align-items', 'flex-direction', 'align-content'],
        correctIndex: 1,
        topic: 'Responsive Design',
        explanation: {
          steps: [
            'justify-content aligns items along the main axis.',
            'align-items aligns items along the perpendicular cross axis.'
          ],
          keyConcept: 'align-items controls cross-axis alignment in Flexbox.'
        }
      },
      {
        id: 30,
        question: 'In JavaScript DOM manipulation, what does event.stopPropagation() achieve?',
        options: [
          'Prevents the default browser action (such as following a link)',
          'Stops the event from bubbling up or capturing down through the DOM hierarchy',
          'Removes the event listener permanently',
          'Reloads the current webpage'
        ],
        correctIndex: 1,
        topic: 'DOM & Events',
        explanation: {
          steps: [
            'event.preventDefault() halts default browser behavior (e.g. form submission).',
            'event.stopPropagation() halts further dispatch of the event in the DOM tree along bubbling/capturing phases.'
          ],
          keyConcept: 'stopPropagation() halts event propagation up or down the DOM.'
        }
      }
    ]
  }
];
