/**
 * Official MEC136: Engineering Graphics & CAD Midterm Drafting Examination Suite
 * Contains 5 Full Subjective Blueprint Drafting Challenges
 * Strictly covers Units 1-3: Scales, Line Projections, Orthographic Multi-View
 * Includes interactive CAD Studio instructions and step-by-step solutions
 */

export const MEC136_DRAFTING_TESTS = [
  {
    "id": "mec136-midterm-paper-1",
    "code": "23241MEC20623-A",
    "title": "Midterm Examination • Paper 1 (Official Drafting Blueprint)",
    "courseCode": "MEC136",
    "courseName": "Engineering Graphics and CAD",
    "examType": "Midterm Drafting Examination (Subjective)",
    "isDraftingExam": true,
    "durationMinutes": 90,
    "totalQuestions": 8,
    "maxMarks": 40,
    "difficulty": "University Standard",
    "topics": [
      "Diagonal Scales",
      "Projections of Lines",
      "Orthographic Multi-View",
      "First & Third Angle",
      "Lettering"
    ],
    "description": "Authentic university subjective drawing paper. Part A covers scales, quadrants, line definitions, and projection symbols. Part B features complete drafting of diagonal scales, line inclinations with traces, and orthographic multi-view extraction from a 3D isometric component.",
    "partA": {
      "title": "Part-A: Technical & Conceptual Fundamentals",
      "instructions": "Answer all 5 questions. Each question carries 2 marks.",
      "marks": 10,
      "questions": [
        {
          "id": "q1a",
          "questionNumber": "Q1 (a)",
          "title": "Difference between Plain and Diagonal Scales",
          "marks": 2,
          "topic": "Scales",
          "prompt": "What is the fundamental difference between plain and diagonal scales?",
          "modelAnswer": {
            "summary": "Plain scale reads two consecutive units; Diagonal scale reads three consecutive units based on the principle of similar triangles.",
            "points": [
              "Plain Scale: Measures two consecutive units (e.g. metres and decimetres, or kilometres and hectometres), or a single unit and its primary subdivision (up to 1 decimal place).",
              "Diagonal Scale: Measures three consecutive units (e.g. metres, decimetres, and centimetres, or yards, feet, and inches), or up to two decimal places (e.g. 4.75 m) using the principle of diagonal division of similar triangles."
            ],
            "keyFormula": "Principle of Diagonal Scale: In a right-angled triangle, parallel divisions along the perpendicular are proportional to the base: x_n = (n / N) × Base."
          }
        },
        {
          "id": "q1b",
          "questionNumber": "Q1 (b)",
          "title": "Quadrant Identification for Points",
          "marks": 2,
          "topic": "Projections of Points",
          "prompt": "Name the quadrant for a point which is below HP (Horizontal Plane) and behind VP (Vertical Plane).",
          "modelAnswer": {
            "summary": "Third Quadrant (3rd Angle).",
            "points": [
              "First Quadrant: Above HP, in front of VP (1st angle projection).",
              "Second Quadrant: Above HP, behind VP.",
              "Third Quadrant: Below HP, behind VP (3rd angle projection: Top view above XY, Front view below XY).",
              "Fourth Quadrant: Below HP, in front of VP."
            ],
            "keyFormula": "Position: Below HP (-y) and Behind VP (-x) ⟹ 3rd Quadrant."
          }
        },
        {
          "id": "q1c",
          "questionNumber": "Q1 (c)",
          "title": "Definition of Apparent and True Length of a Line",
          "marks": 2,
          "topic": "Projections of Lines",
          "prompt": "Define apparent length and true length of a straight line in engineering graphics.",
          "modelAnswer": {
            "summary": "True length is the actual 3D length measured when parallel to a projection plane; Apparent length is the foreshortened projected length when inclined.",
            "points": [
              "True Length (TL): The actual, true physical distance between two endpoints in space. A projection displays true length only when the line is parallel to that projection plane.",
              "Apparent Length: The foreshortened length of the line as seen in a projection when the line is inclined at an angle to the plane of projection (e.g., apparent length in TV = TL · cos θ)."
            ],
            "keyFormula": "Apparent Length (Plan/Elevation) = True Length × cos(angle of inclination)."
          }
        },
        {
          "id": "q1d",
          "questionNumber": "Q1 (d)",
          "title": "Symbols of First Angle and Third Angle Projection",
          "marks": 2,
          "topic": "Projection Symbols",
          "prompt": "Describe and sketch the standard ISO symbols for First Angle and Third Angle projections.",
          "modelAnswer": {
            "summary": "Both symbols depict a truncated cone (frustum) of diameter D and d, length L, with concentric circles indicating the end view.",
            "points": [
              "First Angle Projection Symbol: The side view (two concentric circles of diameter D and d) is drawn on the right-hand side of the frustum when viewed from the left (object between observer and plane).",
              "Third Angle Projection Symbol: The side view (concentric circles) is placed on the left-hand side, between the observer and the frustum (plane between observer and object)."
            ],
            "keyFormula": "Concentric circles position relative to trapezoid frustum defines 1st vs 3rd angle."
          }
        },
        {
          "id": "q1e",
          "questionNumber": "Q1 (e)",
          "title": "Definition and Principles of Orthographic Projection",
          "marks": 2,
          "topic": "Orthographic Projection",
          "prompt": "What do you mean by orthographic projection? Why are the 2nd and 4th quadrants avoided in practice?",
          "modelAnswer": {
            "summary": "Orthographic projection projects 3D features onto perpendicular 2D reference planes using parallel rays normal to the planes. 2nd & 4th quadrants cause overlapping views.",
            "points": [
              "Definition: A system of drawing in which parallel projection lines (projectors) are perpendicular (ortho = 90°) to the projection planes (HP and VP).",
              "Why 2nd and 4th angles are avoided: When HP is rotated by 90° clockwise to align with VP, both the Front View and Top View fall on the same side of the XY reference line (both above XY in 2nd angle, both below in 4th angle), causing views to overlap and create severe ambiguity."
            ],
            "keyFormula": "Orthogonal condition: Projectors ⊥ Projection Planes; Avoid overlap in 2nd & 4th quadrants."
          }
        }
      ]
    },
    "partB": {
      "title": "Part-B: Engineering Blueprint Drafting & Construction",
      "instructions": "Answer all 3 drafting problems. Each problem carries 10 marks.",
      "marks": 30,
      "problems": [
        {
          "id": "p2",
          "questionNumber": "Q2",
          "title": "Construction of Diagonal Scale",
          "marks": 10,
          "topic": "Scales Construction",
          "problemStatement": "Construct a diagonal scale, having Representative Fraction R.F. = 1/50, showing metres, decimetres and centimetres, to measure up to 5 metres. Mark a distance of 4.75 m on it.",
          "specifications": {
            "rf": "1/50",
            "maxMeasurement": "5 metres",
            "unitsShown": "Metres (Main), Decimetres (Subdivision), Centimetres (Diagonal)",
            "lengthToMark": "4.75 m"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Calculate Length of Scale (LOS)",
              "description": "LOS = R.F. × Maximum Length to be measured = (1/50) × 5 m = (1/50) × 500 cm = 10 cm."
            },
            {
              "step": 2,
              "title": "Draw the Outer Scale Boundary",
              "description": "Draw a horizontal line of length 10 cm. Construct a rectangle of height 5 cm (allowing 10 equal diagonal divisions of 5 mm each)."
            },
            {
              "step": 3,
              "title": "Primary Division for Metres",
              "description": "Divide the 10 cm length into 5 equal major divisions, each representing 1 metre (length of each part = 2 cm). Label the 0 mark after the first block: 0, 1, 2, 3, 4 to the right."
            },
            {
              "step": 4,
              "title": "Secondary Division for Decimetres",
              "description": "Divide the first 2 cm block (to the left of 0) into 10 equal parts of 2 mm each. Each sub-part represents 1 decimetre (0.1 m). Label 0 to 10 going left."
            },
            {
              "step": 5,
              "title": "Vertical Diagonal Division for Centimetres",
              "description": "Divide the 5 cm vertical edge into 10 equal parts of 5 mm each, representing 1 centimetre (0.01 m) each. Draw diagonal lines from division n on the bottom to (n+1) on the top line."
            },
            {
              "step": 6,
              "title": "Measure and Mark 4.75 m",
              "description": "Take 4 metres on the main scale to the right of 0. Move 7 decimetres to the left of 0 along the bottom line. Move vertically up along the 7th diagonal to the 5th horizontal centimetre line. Draw dimension line with arrowheads and label \"4.75 m\"."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Calculation of LOS (10 cm) & Formula",
              "marks": 2
            },
            {
              "criterion": "Equal division of main scale (5 parts) & decimetres (10 parts)",
              "marks": 3
            },
            {
              "criterion": "Accurate construction of diagonal lines (10 parts) & parallelism",
              "marks": 3
            },
            {
              "criterion": "Accurate marking of 4.75 m with standard dimensioning & lettering",
              "marks": 2
            }
          ]
        },
        {
          "id": "p3",
          "questionNumber": "Q3",
          "title": "Projections of Straight Line with Traces",
          "marks": 10,
          "topic": "Projections of Straight Lines",
          "problemStatement": "Represent the projection of line AB 60 mm long inclined to HP at 45° and parallel to VP. The nearest end A is 20 mm above HP and 25 mm in front of VP. Also locate and show the trace of the line.",
          "specifications": {
            "trueLength": "60 mm",
            "inclinationHP": "θ = 45°",
            "inclinationVP": "φ = 0° (Parallel to VP)",
            "positionA": "20 mm above HP, 25 mm in front of VP"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Draw Reference Line XY",
              "description": "Draw a horizontal reference line XY. Above XY represents VP (Front View); below XY represents HP (Top View) in 1st angle projection."
            },
            {
              "step": 2,
              "title": "Plot End A Coordinates",
              "description": "Draw a vertical projector perpendicular to XY. Mark front view point a' at 20 mm above XY. Mark top view point a at 25 mm below XY."
            },
            {
              "step": 3,
              "title": "Construct Front View (Elevation)",
              "description": "Since the line is parallel to VP, its front view exhibits True Length (60 mm). From a', draw line a'b' = 60 mm inclined at θ = 45° to XY. Measure vertical height of b' from XY = 20 + 60 sin(45°) = 20 + 42.43 = 62.43 mm."
            },
            {
              "step": 4,
              "title": "Construct Top View (Plan)",
              "description": "From a, draw a horizontal line parallel to XY (since line is parallel to VP, every point is 25 mm in front of VP). Drop a vertical projector from b' to intersect this horizontal line at b. Apparent length ab = 60 cos(45°) = 42.43 mm."
            },
            {
              "step": 5,
              "title": "Locate Traces of the Line",
              "description": "Extend front view line b'a' downward until it intersects XY at point h'. Drop a vertical projector from h' to meet the extension of top view line ba at H (Horizontal Trace). Distance of HT from XY = 25 mm. Since the line is parallel to VP, it does not pierce VP; hence, Vertical Trace (VT) does not exist (at infinity)."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Reference line XY and correct projection of point A",
              "marks": 2
            },
            {
              "criterion": "Front view a'b' drawn at 45° true length (60 mm)",
              "marks": 3
            },
            {
              "criterion": "Top view ab drawn parallel to XY with correct apparent length (42.4 mm)",
              "marks": 3
            },
            {
              "criterion": "Correct construction and labeling of Horizontal Trace (HT)",
              "marks": 2
            }
          ]
        },
        {
          "id": "p4",
          "questionNumber": "Q4",
          "title": "Orthographic Multi-View Drafting from 3D Isometric View",
          "marks": 10,
          "topic": "Orthographic Projection",
          "problemStatement": "Given the specified 3D isometric component (stepped slotted block: Base 60 mm × 35 mm, overall height 45 mm, step height 10 mm, upper block 35 mm × 35 mm). Draw the following views in First Angle Projection: (a) Front View looking in direction of arrow X, (b) Top View, (c) Left Side View. Include all visible outlines, hidden lines, and standard dimensioning.",
          "specifications": {
            "overallDimensions": "60 mm (Length) × 35 mm (Width) × 45 mm (Height)",
            "basePlate": "60 mm × 35 mm × 10 mm thick",
            "stepBlock": "35 mm length × 35 mm width × 35 mm height above base (total 45 mm)",
            "projectionSystem": "First Angle Projection (FV above XY, TV below XY, Left Side View on Right of FV)"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Front View (Elevation - Looking along Arrow X)",
              "description": "Width = 60 mm, Height = 45 mm. Bottom base rectangle: 60 mm wide × 10 mm high. Right vertical step: 35 mm wide × 35 mm high rising from the base to total height 45 mm. Remaining left ledge: 25 mm wide at height 10 mm."
            },
            {
              "step": 2,
              "title": "Top View (Plan - Looking from directly above)",
              "description": "Length = 60 mm, Width = 35 mm. The top view is an enclosing rectangle of 60 mm × 35 mm. A vertical boundary line divides it into two surfaces: the lower step on the left (25 mm × 35 mm) and the elevated top surface on the right (35 mm × 35 mm)."
            },
            {
              "step": 3,
              "title": "Left Side View (Looking from left, drawn on right of FV)",
              "description": "Width = 35 mm, Height = 45 mm. From the left, the object appears as an upright L-profile or single enclosing block of 35 mm width × 45 mm total height, with a horizontal line at 10 mm height indicating the base step level."
            },
            {
              "step": 4,
              "title": "Projection Alignment & ISO Dimensioning",
              "description": "Align TV vertically under FV with continuous projection rays. Project horizontal coordinates from FV and 45° miter line from TV to form the Side View. Place dimensions 60, 35, 45, 10, and 25 using aligned system with 3:1 arrowheads."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Accurate Front View (FV) with correct stepped profile",
              "marks": 3
            },
            {
              "criterion": "Accurate Top View (TV) with correct boundary dividing line",
              "marks": 3
            },
            {
              "criterion": "Accurate Side View (SV) projected using 45° miter / alignment",
              "marks": 2
            },
            {
              "criterion": "Standard ISO dimensioning, projection alignment, and line quality",
              "marks": 2
            }
          ]
        }
      ]
    },
    "questions": [
      {
        "id": 1,
        "question": "What is the fundamental difference between a plain scale and a diagonal scale in engineering drawing?",
        "options": [
          "Plain scale is for metric units, diagonal scale is for imperial units",
          "Plain scale measures up to two consecutive units; diagonal scale measures three consecutive units using similar triangles",
          "Plain scale is only used for reductions, diagonal scale for enlargements",
          "Plain scale requires representative fraction while diagonal scale does not"
        ],
        "correctIndex": 1,
        "topic": "Scales",
        "explanation": {
          "steps": [
            "Plain scale measures two consecutive units (e.g., m and dm) or a unit with one decimal place.",
            "Diagonal scale measures three consecutive units (e.g., m, dm, and cm) or up to two decimal places.",
            "The diagonal scale relies on the principle of similar triangles to subdivide the smallest division."
          ],
          "keyConcept": "Diagonal scale principle: x_n = (n/N) × Base division."
        }
      },
      {
        "id": 2,
        "question": "A point is located below the Horizontal Plane (HP) and behind the Vertical Plane (VP). Which quadrant does it lie in?",
        "options": [
          "First Quadrant",
          "Second Quadrant",
          "Third Quadrant",
          "Fourth Quadrant"
        ],
        "correctIndex": 2,
        "topic": "Projections of Points",
        "explanation": {
          "steps": [
            "1st Quadrant: Above HP, in front of VP",
            "2nd Quadrant: Above HP, behind VP",
            "3rd Quadrant: Below HP, behind VP",
            "4th Quadrant: Below HP, in front of VP"
          ],
          "keyConcept": "Point below HP and behind VP belongs to the Third Quadrant (used in 3rd Angle Projection)."
        }
      },
      {
        "id": 3,
        "question": "The Horizontal Trace (HT) of a straight line is defined as:",
        "options": [
          "The point where the line (or its extension) intersects the Horizontal Plane (HP)",
          "The point where the line intersects the Vertical Plane (VP)",
          "The projection of the line on the horizontal plane",
          "The angle of inclination with the ground plane"
        ],
        "correctIndex": 0,
        "topic": "Projections of Lines",
        "explanation": {
          "steps": [
            "Trace of a line is the point of intersection of the line (produced if necessary) with the reference planes.",
            "Intersection with HP is the Horizontal Trace (HT).",
            "Intersection with VP is the Vertical Trace (VT)."
          ],
          "keyConcept": "HT lies on HP; its elevation h' lies on the reference XY line."
        }
      },
      {
        "id": 4,
        "question": "In standard First Angle projection symbol vs Third Angle projection symbol, the frustum of a cone is drawn such that:",
        "options": [
          "In First Angle, the concentric circles view is placed opposite the viewer (on the right of the trapezoid when viewed from left)",
          "In Third Angle, the circular view is placed between the cone and observer",
          "The symbol differentiates whether the object is placed between the observer and plane or vice versa",
          "All of the above statements are correct"
        ],
        "correctIndex": 3,
        "topic": "Projection Systems",
        "explanation": {
          "steps": [
            "In First Angle projection, Object is between Observer and Plane of Projection.",
            "In Third Angle projection, Plane of Projection is between Observer and Object.",
            "The ISO projection symbol shows the orthographic projection of a truncated cone.",
            "In 1st angle symbol, looking from left, circle is drawn on right. In 3rd angle, circle is on left."
          ],
          "keyConcept": "First angle: Observer -> Object -> Plane. Third angle: Observer -> Plane -> Object."
        }
      },
      {
        "id": 5,
        "question": "Calculate the Representative Fraction (RF) for an engineering drawing where a length of 5 mm represents an actual distance of 1 metre.",
        "options": [
          "1:20",
          "1:50",
          "1:200",
          "1:500"
        ],
        "correctIndex": 2,
        "topic": "Representative Fraction",
        "explanation": {
          "steps": [
            "RF = Dimension on drawing / Actual dimension.",
            "Drawing dimension = 5 mm.",
            "Actual dimension = 1 m = 1000 mm.",
            "RF = 5 mm / 1000 mm = 1 / 200."
          ],
          "keyConcept": "RF is a dimensionless ratio; units of numerator and denominator must be identical."
        }
      },
      {
        "id": 6,
        "question": "For a diagonal scale with RF = 1/50 designed to measure a maximum distance of 5 metres, what is the Length of Scale (LOS)?",
        "options": [
          "5 cm",
          "10 cm",
          "15 cm",
          "20 cm"
        ],
        "correctIndex": 1,
        "topic": "Scales Construction",
        "explanation": {
          "steps": [
            "Length of Scale (LOS) = RF × Maximum Length to be measured.",
            "LOS = (1/50) × 5 m = (1/50) × 500 cm = 10 cm."
          ],
          "keyConcept": "LOS = RF × Max Length = (1/50) × 500 cm = 10 cm."
        }
      },
      {
        "id": 7,
        "question": "A line AB of true length 60 mm has end A in HP and 20 mm in front of VP. The line is inclined at 45° to HP and parallel to VP. What are the lengths of its Front View and Top View?",
        "options": [
          "Front View = 60 mm (True Length), Top View = 42.4 mm parallel to XY",
          "Front View = 42.4 mm, Top View = 60 mm (True Length)",
          "Front View = 60 mm, Top View = 60 mm",
          "Front View = 30 mm, Top View = 30 mm"
        ],
        "correctIndex": 0,
        "topic": "Projections of Lines",
        "explanation": {
          "steps": [
            "Since the line is parallel to VP, its projection on VP (Front View) shows the True Length = 60 mm at angle θ = 45° to XY.",
            "Its Top View (Plan) is parallel to XY with apparent length = True Length × cos(45°) = 60 × 0.7071 ≈ 42.4 mm."
          ],
          "keyConcept": "When a line is parallel to a plane, its projection on that plane shows its true length and true inclination."
        }
      },
      {
        "id": 8,
        "question": "In First Angle Orthographic Projection, where is the Left Side View (LSV) positioned relative to the Front View?",
        "options": [
          "Directly above the Front View",
          "On the right-hand side of the Front View",
          "On the left-hand side of the Front View",
          "Directly below the Top View"
        ],
        "correctIndex": 1,
        "topic": "Orthographic Multi-View",
        "explanation": {
          "steps": [
            "In First Angle projection, views are cast on the plane behind the object.",
            "Looking from the left, rays project onto the Right Profile Plane (RPP).",
            "When RPP is revolved into the frontal plane, it appears on the right of the Front View."
          ],
          "keyConcept": "First Angle: Left view on the Right, Right view on the Left, Top view Below the Front view."
        }
      }
    ]
  },
  {
    "id": "mec136-midterm-paper-2",
    "code": "23241MEC20623-B",
    "title": "Midterm Examination • Paper 2 (Diagonal Scales & Line Inclinations)",
    "courseCode": "MEC136",
    "courseName": "Engineering Graphics and CAD",
    "examType": "Midterm Drafting Examination (Subjective)",
    "isDraftingExam": true,
    "durationMinutes": 90,
    "totalQuestions": 8,
    "maxMarks": 40,
    "difficulty": "University Standard",
    "topics": [
      "Diagonal Scales",
      "Projections of Lines",
      "Orthographic Multi-View",
      "First & Third Angle",
      "CAD Studio"
    ],
    "description": "Drafting paper covering Diagonal Scale (RF = 1/50, distance 4.35m) and Straight Line AB (True length 80mm inclined at 30° to HP and 45° to VP) with complete horizontal and vertical traces (HT & VT).",
    "partA": {
      "title": "Part-A: Technical & Conceptual Fundamentals",
      "instructions": "Answer all 5 questions. Each question carries 2 marks.",
      "marks": 10,
      "questions": [
        {
          "id": "q1a",
          "questionNumber": "Q1 (a)",
          "title": "Difference between Plain and Diagonal Scales",
          "marks": 2,
          "topic": "Scales",
          "prompt": "What is the fundamental difference between plain and diagonal scales?",
          "modelAnswer": {
            "summary": "Plain scale reads two consecutive units; Diagonal scale reads three consecutive units based on the principle of similar triangles.",
            "points": [
              "Plain Scale: Measures two consecutive units (e.g. metres and decimetres, or kilometres and hectometres), or a single unit and its primary subdivision (up to 1 decimal place).",
              "Diagonal Scale: Measures three consecutive units (e.g. metres, decimetres, and centimetres, or yards, feet, and inches), or up to two decimal places (e.g. 4.75 m) using the principle of diagonal division of similar triangles."
            ],
            "keyFormula": "Principle of Diagonal Scale: In a right-angled triangle, parallel divisions along the perpendicular are proportional to the base: x_n = (n / N) × Base."
          }
        },
        {
          "id": "q1b",
          "questionNumber": "Q1 (b)",
          "title": "Quadrant Identification for Points",
          "marks": 2,
          "topic": "Projections of Points",
          "prompt": "Name the quadrant for a point which is below HP (Horizontal Plane) and behind VP (Vertical Plane).",
          "modelAnswer": {
            "summary": "Third Quadrant (3rd Angle).",
            "points": [
              "First Quadrant: Above HP, in front of VP (1st angle projection).",
              "Second Quadrant: Above HP, behind VP.",
              "Third Quadrant: Below HP, behind VP (3rd angle projection: Top view above XY, Front view below XY).",
              "Fourth Quadrant: Below HP, in front of VP."
            ],
            "keyFormula": "Position: Below HP (-y) and Behind VP (-x) ⟹ 3rd Quadrant."
          }
        },
        {
          "id": "q1c",
          "questionNumber": "Q1 (c)",
          "title": "Definition of Apparent and True Length of a Line",
          "marks": 2,
          "topic": "Projections of Lines",
          "prompt": "Define apparent length and true length of a straight line in engineering graphics.",
          "modelAnswer": {
            "summary": "True length is the actual 3D length measured when parallel to a projection plane; Apparent length is the foreshortened projected length when inclined.",
            "points": [
              "True Length (TL): The actual, true physical distance between two endpoints in space. A projection displays true length only when the line is parallel to that projection plane.",
              "Apparent Length: The foreshortened length of the line as seen in a projection when the line is inclined at an angle to the plane of projection (e.g., apparent length in TV = TL · cos θ)."
            ],
            "keyFormula": "Apparent Length (Plan/Elevation) = True Length × cos(angle of inclination)."
          }
        },
        {
          "id": "q1d",
          "questionNumber": "Q1 (d)",
          "title": "Symbols of First Angle and Third Angle Projection",
          "marks": 2,
          "topic": "Projection Symbols",
          "prompt": "Describe and sketch the standard ISO symbols for First Angle and Third Angle projections.",
          "modelAnswer": {
            "summary": "Both symbols depict a truncated cone (frustum) of diameter D and d, length L, with concentric circles indicating the end view.",
            "points": [
              "First Angle Projection Symbol: The side view (two concentric circles of diameter D and d) is drawn on the right-hand side of the frustum when viewed from the left (object between observer and plane).",
              "Third Angle Projection Symbol: The side view (concentric circles) is placed on the left-hand side, between the observer and the frustum (plane between observer and object)."
            ],
            "keyFormula": "Concentric circles position relative to trapezoid frustum defines 1st vs 3rd angle."
          }
        },
        {
          "id": "q1e",
          "questionNumber": "Q1 (e)",
          "title": "Definition and Principles of Orthographic Projection",
          "marks": 2,
          "topic": "Orthographic Projection",
          "prompt": "What do you mean by orthographic projection? Why are the 2nd and 4th quadrants avoided in practice?",
          "modelAnswer": {
            "summary": "Orthographic projection projects 3D features onto perpendicular 2D reference planes using parallel rays normal to the planes. 2nd & 4th quadrants cause overlapping views.",
            "points": [
              "Definition: A system of drawing in which parallel projection lines (projectors) are perpendicular (ortho = 90°) to the projection planes (HP and VP).",
              "Why 2nd and 4th angles are avoided: When HP is rotated by 90° clockwise to align with VP, both the Front View and Top View fall on the same side of the XY reference line (both above XY in 2nd angle, both below in 4th angle), causing views to overlap and create severe ambiguity."
            ],
            "keyFormula": "Orthogonal condition: Projectors ⊥ Projection Planes; Avoid overlap in 2nd & 4th quadrants."
          }
        }
      ]
    },
    "partB": {
      "title": "Part-B: Engineering Blueprint Drafting & Construction",
      "instructions": "Answer all 3 drafting problems. Each problem carries 10 marks.",
      "marks": 30,
      "problems": [
        {
          "id": "p2",
          "questionNumber": "Q2",
          "title": "Construction of Diagonal Scale",
          "marks": 10,
          "topic": "Scales Construction",
          "problemStatement": "Construct a diagonal scale, having Representative Fraction R.F. = 1/50, showing metres, decimetres and centimetres, to measure up to 5 metres. Mark a distance of 4.75 m on it.",
          "specifications": {
            "rf": "1/50",
            "maxMeasurement": "5 metres",
            "unitsShown": "Metres (Main), Decimetres (Subdivision), Centimetres (Diagonal)",
            "lengthToMark": "4.75 m"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Calculate Length of Scale (LOS)",
              "description": "LOS = R.F. × Maximum Length to be measured = (1/50) × 5 m = (1/50) × 500 cm = 10 cm."
            },
            {
              "step": 2,
              "title": "Draw the Outer Scale Boundary",
              "description": "Draw a horizontal line of length 10 cm. Construct a rectangle of height 5 cm (allowing 10 equal diagonal divisions of 5 mm each)."
            },
            {
              "step": 3,
              "title": "Primary Division for Metres",
              "description": "Divide the 10 cm length into 5 equal major divisions, each representing 1 metre (length of each part = 2 cm). Label the 0 mark after the first block: 0, 1, 2, 3, 4 to the right."
            },
            {
              "step": 4,
              "title": "Secondary Division for Decimetres",
              "description": "Divide the first 2 cm block (to the left of 0) into 10 equal parts of 2 mm each. Each sub-part represents 1 decimetre (0.1 m). Label 0 to 10 going left."
            },
            {
              "step": 5,
              "title": "Vertical Diagonal Division for Centimetres",
              "description": "Divide the 5 cm vertical edge into 10 equal parts of 5 mm each, representing 1 centimetre (0.01 m) each. Draw diagonal lines from division n on the bottom to (n+1) on the top line."
            },
            {
              "step": 6,
              "title": "Measure and Mark 4.75 m",
              "description": "Take 4 metres on the main scale to the right of 0. Move 7 decimetres to the left of 0 along the bottom line. Move vertically up along the 7th diagonal to the 5th horizontal centimetre line. Draw dimension line with arrowheads and label \"4.75 m\"."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Calculation of LOS (10 cm) & Formula",
              "marks": 2
            },
            {
              "criterion": "Equal division of main scale (5 parts) & decimetres (10 parts)",
              "marks": 3
            },
            {
              "criterion": "Accurate construction of diagonal lines (10 parts) & parallelism",
              "marks": 3
            },
            {
              "criterion": "Accurate marking of 4.75 m with standard dimensioning & lettering",
              "marks": 2
            }
          ]
        },
        {
          "id": "p3",
          "questionNumber": "Q3",
          "title": "Projections of Straight Line with Traces",
          "marks": 10,
          "topic": "Projections of Straight Lines",
          "problemStatement": "Represent the projection of line AB 60 mm long inclined to HP at 45° and parallel to VP. The nearest end A is 20 mm above HP and 25 mm in front of VP. Also locate and show the trace of the line.",
          "specifications": {
            "trueLength": "60 mm",
            "inclinationHP": "θ = 45°",
            "inclinationVP": "φ = 0° (Parallel to VP)",
            "positionA": "20 mm above HP, 25 mm in front of VP"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Draw Reference Line XY",
              "description": "Draw a horizontal reference line XY. Above XY represents VP (Front View); below XY represents HP (Top View) in 1st angle projection."
            },
            {
              "step": 2,
              "title": "Plot End A Coordinates",
              "description": "Draw a vertical projector perpendicular to XY. Mark front view point a' at 20 mm above XY. Mark top view point a at 25 mm below XY."
            },
            {
              "step": 3,
              "title": "Construct Front View (Elevation)",
              "description": "Since the line is parallel to VP, its front view exhibits True Length (60 mm). From a', draw line a'b' = 60 mm inclined at θ = 45° to XY. Measure vertical height of b' from XY = 20 + 60 sin(45°) = 20 + 42.43 = 62.43 mm."
            },
            {
              "step": 4,
              "title": "Construct Top View (Plan)",
              "description": "From a, draw a horizontal line parallel to XY (since line is parallel to VP, every point is 25 mm in front of VP). Drop a vertical projector from b' to intersect this horizontal line at b. Apparent length ab = 60 cos(45°) = 42.43 mm."
            },
            {
              "step": 5,
              "title": "Locate Traces of the Line",
              "description": "Extend front view line b'a' downward until it intersects XY at point h'. Drop a vertical projector from h' to meet the extension of top view line ba at H (Horizontal Trace). Distance of HT from XY = 25 mm. Since the line is parallel to VP, it does not pierce VP; hence, Vertical Trace (VT) does not exist (at infinity)."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Reference line XY and correct projection of point A",
              "marks": 2
            },
            {
              "criterion": "Front view a'b' drawn at 45° true length (60 mm)",
              "marks": 3
            },
            {
              "criterion": "Top view ab drawn parallel to XY with correct apparent length (42.4 mm)",
              "marks": 3
            },
            {
              "criterion": "Correct construction and labeling of Horizontal Trace (HT)",
              "marks": 2
            }
          ]
        },
        {
          "id": "p4",
          "questionNumber": "Q4",
          "title": "Orthographic Multi-View Drafting from 3D Isometric View",
          "marks": 10,
          "topic": "Orthographic Projection",
          "problemStatement": "Given the specified 3D isometric component (stepped slotted block: Base 60 mm × 35 mm, overall height 45 mm, step height 10 mm, upper block 35 mm × 35 mm). Draw the following views in First Angle Projection: (a) Front View looking in direction of arrow X, (b) Top View, (c) Left Side View. Include all visible outlines, hidden lines, and standard dimensioning.",
          "specifications": {
            "overallDimensions": "60 mm (Length) × 35 mm (Width) × 45 mm (Height)",
            "basePlate": "60 mm × 35 mm × 10 mm thick",
            "stepBlock": "35 mm length × 35 mm width × 35 mm height above base (total 45 mm)",
            "projectionSystem": "First Angle Projection (FV above XY, TV below XY, Left Side View on Right of FV)"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Front View (Elevation - Looking along Arrow X)",
              "description": "Width = 60 mm, Height = 45 mm. Bottom base rectangle: 60 mm wide × 10 mm high. Right vertical step: 35 mm wide × 35 mm high rising from the base to total height 45 mm. Remaining left ledge: 25 mm wide at height 10 mm."
            },
            {
              "step": 2,
              "title": "Top View (Plan - Looking from directly above)",
              "description": "Length = 60 mm, Width = 35 mm. The top view is an enclosing rectangle of 60 mm × 35 mm. A vertical boundary line divides it into two surfaces: the lower step on the left (25 mm × 35 mm) and the elevated top surface on the right (35 mm × 35 mm)."
            },
            {
              "step": 3,
              "title": "Left Side View (Looking from left, drawn on right of FV)",
              "description": "Width = 35 mm, Height = 45 mm. From the left, the object appears as an upright L-profile or single enclosing block of 35 mm width × 45 mm total height, with a horizontal line at 10 mm height indicating the base step level."
            },
            {
              "step": 4,
              "title": "Projection Alignment & ISO Dimensioning",
              "description": "Align TV vertically under FV with continuous projection rays. Project horizontal coordinates from FV and 45° miter line from TV to form the Side View. Place dimensions 60, 35, 45, 10, and 25 using aligned system with 3:1 arrowheads."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Accurate Front View (FV) with correct stepped profile",
              "marks": 3
            },
            {
              "criterion": "Accurate Top View (TV) with correct boundary dividing line",
              "marks": 3
            },
            {
              "criterion": "Accurate Side View (SV) projected using 45° miter / alignment",
              "marks": 2
            },
            {
              "criterion": "Standard ISO dimensioning, projection alignment, and line quality",
              "marks": 2
            }
          ]
        }
      ]
    }
  },
  {
    "id": "mec136-midterm-paper-3",
    "code": "23241MEC20623-C",
    "title": "Midterm Examination • Paper 3 (First Angle Orthographic Projections)",
    "courseCode": "MEC136",
    "courseName": "Engineering Graphics and CAD",
    "examType": "Midterm Drafting Examination (Subjective)",
    "isDraftingExam": true,
    "durationMinutes": 90,
    "totalQuestions": 8,
    "maxMarks": 40,
    "difficulty": "University Standard",
    "topics": [
      "Diagonal Scales",
      "Projections of Lines",
      "Orthographic Multi-View",
      "First & Third Angle",
      "CAD Studio"
    ],
    "description": "CAD Drafting challenge converting a 3D Stepped Machine Bearing Bracket into Front Elevation, Top Plan View, and Left Side Profile in standard First-Angle projection.",
    "partA": {
      "title": "Part-A: Technical & Conceptual Fundamentals",
      "instructions": "Answer all 5 questions. Each question carries 2 marks.",
      "marks": 10,
      "questions": [
        {
          "id": "q1a",
          "questionNumber": "Q1 (a)",
          "title": "Difference between Plain and Diagonal Scales",
          "marks": 2,
          "topic": "Scales",
          "prompt": "What is the fundamental difference between plain and diagonal scales?",
          "modelAnswer": {
            "summary": "Plain scale reads two consecutive units; Diagonal scale reads three consecutive units based on the principle of similar triangles.",
            "points": [
              "Plain Scale: Measures two consecutive units (e.g. metres and decimetres, or kilometres and hectometres), or a single unit and its primary subdivision (up to 1 decimal place).",
              "Diagonal Scale: Measures three consecutive units (e.g. metres, decimetres, and centimetres, or yards, feet, and inches), or up to two decimal places (e.g. 4.75 m) using the principle of diagonal division of similar triangles."
            ],
            "keyFormula": "Principle of Diagonal Scale: In a right-angled triangle, parallel divisions along the perpendicular are proportional to the base: x_n = (n / N) × Base."
          }
        },
        {
          "id": "q1b",
          "questionNumber": "Q1 (b)",
          "title": "Quadrant Identification for Points",
          "marks": 2,
          "topic": "Projections of Points",
          "prompt": "Name the quadrant for a point which is below HP (Horizontal Plane) and behind VP (Vertical Plane).",
          "modelAnswer": {
            "summary": "Third Quadrant (3rd Angle).",
            "points": [
              "First Quadrant: Above HP, in front of VP (1st angle projection).",
              "Second Quadrant: Above HP, behind VP.",
              "Third Quadrant: Below HP, behind VP (3rd angle projection: Top view above XY, Front view below XY).",
              "Fourth Quadrant: Below HP, in front of VP."
            ],
            "keyFormula": "Position: Below HP (-y) and Behind VP (-x) ⟹ 3rd Quadrant."
          }
        },
        {
          "id": "q1c",
          "questionNumber": "Q1 (c)",
          "title": "Definition of Apparent and True Length of a Line",
          "marks": 2,
          "topic": "Projections of Lines",
          "prompt": "Define apparent length and true length of a straight line in engineering graphics.",
          "modelAnswer": {
            "summary": "True length is the actual 3D length measured when parallel to a projection plane; Apparent length is the foreshortened projected length when inclined.",
            "points": [
              "True Length (TL): The actual, true physical distance between two endpoints in space. A projection displays true length only when the line is parallel to that projection plane.",
              "Apparent Length: The foreshortened length of the line as seen in a projection when the line is inclined at an angle to the plane of projection (e.g., apparent length in TV = TL · cos θ)."
            ],
            "keyFormula": "Apparent Length (Plan/Elevation) = True Length × cos(angle of inclination)."
          }
        },
        {
          "id": "q1d",
          "questionNumber": "Q1 (d)",
          "title": "Symbols of First Angle and Third Angle Projection",
          "marks": 2,
          "topic": "Projection Symbols",
          "prompt": "Describe and sketch the standard ISO symbols for First Angle and Third Angle projections.",
          "modelAnswer": {
            "summary": "Both symbols depict a truncated cone (frustum) of diameter D and d, length L, with concentric circles indicating the end view.",
            "points": [
              "First Angle Projection Symbol: The side view (two concentric circles of diameter D and d) is drawn on the right-hand side of the frustum when viewed from the left (object between observer and plane).",
              "Third Angle Projection Symbol: The side view (concentric circles) is placed on the left-hand side, between the observer and the frustum (plane between observer and object)."
            ],
            "keyFormula": "Concentric circles position relative to trapezoid frustum defines 1st vs 3rd angle."
          }
        },
        {
          "id": "q1e",
          "questionNumber": "Q1 (e)",
          "title": "Definition and Principles of Orthographic Projection",
          "marks": 2,
          "topic": "Orthographic Projection",
          "prompt": "What do you mean by orthographic projection? Why are the 2nd and 4th quadrants avoided in practice?",
          "modelAnswer": {
            "summary": "Orthographic projection projects 3D features onto perpendicular 2D reference planes using parallel rays normal to the planes. 2nd & 4th quadrants cause overlapping views.",
            "points": [
              "Definition: A system of drawing in which parallel projection lines (projectors) are perpendicular (ortho = 90°) to the projection planes (HP and VP).",
              "Why 2nd and 4th angles are avoided: When HP is rotated by 90° clockwise to align with VP, both the Front View and Top View fall on the same side of the XY reference line (both above XY in 2nd angle, both below in 4th angle), causing views to overlap and create severe ambiguity."
            ],
            "keyFormula": "Orthogonal condition: Projectors ⊥ Projection Planes; Avoid overlap in 2nd & 4th quadrants."
          }
        }
      ]
    },
    "partB": {
      "title": "Part-B: Engineering Blueprint Drafting & Construction",
      "instructions": "Answer all 3 drafting problems. Each problem carries 10 marks.",
      "marks": 30,
      "problems": [
        {
          "id": "p2",
          "questionNumber": "Q2",
          "title": "Construction of Diagonal Scale",
          "marks": 10,
          "topic": "Scales Construction",
          "problemStatement": "Construct a diagonal scale, having Representative Fraction R.F. = 1/50, showing metres, decimetres and centimetres, to measure up to 5 metres. Mark a distance of 4.75 m on it.",
          "specifications": {
            "rf": "1/50",
            "maxMeasurement": "5 metres",
            "unitsShown": "Metres (Main), Decimetres (Subdivision), Centimetres (Diagonal)",
            "lengthToMark": "4.75 m"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Calculate Length of Scale (LOS)",
              "description": "LOS = R.F. × Maximum Length to be measured = (1/50) × 5 m = (1/50) × 500 cm = 10 cm."
            },
            {
              "step": 2,
              "title": "Draw the Outer Scale Boundary",
              "description": "Draw a horizontal line of length 10 cm. Construct a rectangle of height 5 cm (allowing 10 equal diagonal divisions of 5 mm each)."
            },
            {
              "step": 3,
              "title": "Primary Division for Metres",
              "description": "Divide the 10 cm length into 5 equal major divisions, each representing 1 metre (length of each part = 2 cm). Label the 0 mark after the first block: 0, 1, 2, 3, 4 to the right."
            },
            {
              "step": 4,
              "title": "Secondary Division for Decimetres",
              "description": "Divide the first 2 cm block (to the left of 0) into 10 equal parts of 2 mm each. Each sub-part represents 1 decimetre (0.1 m). Label 0 to 10 going left."
            },
            {
              "step": 5,
              "title": "Vertical Diagonal Division for Centimetres",
              "description": "Divide the 5 cm vertical edge into 10 equal parts of 5 mm each, representing 1 centimetre (0.01 m) each. Draw diagonal lines from division n on the bottom to (n+1) on the top line."
            },
            {
              "step": 6,
              "title": "Measure and Mark 4.75 m",
              "description": "Take 4 metres on the main scale to the right of 0. Move 7 decimetres to the left of 0 along the bottom line. Move vertically up along the 7th diagonal to the 5th horizontal centimetre line. Draw dimension line with arrowheads and label \"4.75 m\"."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Calculation of LOS (10 cm) & Formula",
              "marks": 2
            },
            {
              "criterion": "Equal division of main scale (5 parts) & decimetres (10 parts)",
              "marks": 3
            },
            {
              "criterion": "Accurate construction of diagonal lines (10 parts) & parallelism",
              "marks": 3
            },
            {
              "criterion": "Accurate marking of 4.75 m with standard dimensioning & lettering",
              "marks": 2
            }
          ]
        },
        {
          "id": "p3",
          "questionNumber": "Q3",
          "title": "Projections of Straight Line with Traces",
          "marks": 10,
          "topic": "Projections of Straight Lines",
          "problemStatement": "Represent the projection of line AB 60 mm long inclined to HP at 45° and parallel to VP. The nearest end A is 20 mm above HP and 25 mm in front of VP. Also locate and show the trace of the line.",
          "specifications": {
            "trueLength": "60 mm",
            "inclinationHP": "θ = 45°",
            "inclinationVP": "φ = 0° (Parallel to VP)",
            "positionA": "20 mm above HP, 25 mm in front of VP"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Draw Reference Line XY",
              "description": "Draw a horizontal reference line XY. Above XY represents VP (Front View); below XY represents HP (Top View) in 1st angle projection."
            },
            {
              "step": 2,
              "title": "Plot End A Coordinates",
              "description": "Draw a vertical projector perpendicular to XY. Mark front view point a' at 20 mm above XY. Mark top view point a at 25 mm below XY."
            },
            {
              "step": 3,
              "title": "Construct Front View (Elevation)",
              "description": "Since the line is parallel to VP, its front view exhibits True Length (60 mm). From a', draw line a'b' = 60 mm inclined at θ = 45° to XY. Measure vertical height of b' from XY = 20 + 60 sin(45°) = 20 + 42.43 = 62.43 mm."
            },
            {
              "step": 4,
              "title": "Construct Top View (Plan)",
              "description": "From a, draw a horizontal line parallel to XY (since line is parallel to VP, every point is 25 mm in front of VP). Drop a vertical projector from b' to intersect this horizontal line at b. Apparent length ab = 60 cos(45°) = 42.43 mm."
            },
            {
              "step": 5,
              "title": "Locate Traces of the Line",
              "description": "Extend front view line b'a' downward until it intersects XY at point h'. Drop a vertical projector from h' to meet the extension of top view line ba at H (Horizontal Trace). Distance of HT from XY = 25 mm. Since the line is parallel to VP, it does not pierce VP; hence, Vertical Trace (VT) does not exist (at infinity)."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Reference line XY and correct projection of point A",
              "marks": 2
            },
            {
              "criterion": "Front view a'b' drawn at 45° true length (60 mm)",
              "marks": 3
            },
            {
              "criterion": "Top view ab drawn parallel to XY with correct apparent length (42.4 mm)",
              "marks": 3
            },
            {
              "criterion": "Correct construction and labeling of Horizontal Trace (HT)",
              "marks": 2
            }
          ]
        },
        {
          "id": "p4",
          "questionNumber": "Q4",
          "title": "Orthographic Multi-View Drafting from 3D Isometric View",
          "marks": 10,
          "topic": "Orthographic Projection",
          "problemStatement": "Given the specified 3D isometric component (stepped slotted block: Base 60 mm × 35 mm, overall height 45 mm, step height 10 mm, upper block 35 mm × 35 mm). Draw the following views in First Angle Projection: (a) Front View looking in direction of arrow X, (b) Top View, (c) Left Side View. Include all visible outlines, hidden lines, and standard dimensioning.",
          "specifications": {
            "overallDimensions": "60 mm (Length) × 35 mm (Width) × 45 mm (Height)",
            "basePlate": "60 mm × 35 mm × 10 mm thick",
            "stepBlock": "35 mm length × 35 mm width × 35 mm height above base (total 45 mm)",
            "projectionSystem": "First Angle Projection (FV above XY, TV below XY, Left Side View on Right of FV)"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Front View (Elevation - Looking along Arrow X)",
              "description": "Width = 60 mm, Height = 45 mm. Bottom base rectangle: 60 mm wide × 10 mm high. Right vertical step: 35 mm wide × 35 mm high rising from the base to total height 45 mm. Remaining left ledge: 25 mm wide at height 10 mm."
            },
            {
              "step": 2,
              "title": "Top View (Plan - Looking from directly above)",
              "description": "Length = 60 mm, Width = 35 mm. The top view is an enclosing rectangle of 60 mm × 35 mm. A vertical boundary line divides it into two surfaces: the lower step on the left (25 mm × 35 mm) and the elevated top surface on the right (35 mm × 35 mm)."
            },
            {
              "step": 3,
              "title": "Left Side View (Looking from left, drawn on right of FV)",
              "description": "Width = 35 mm, Height = 45 mm. From the left, the object appears as an upright L-profile or single enclosing block of 35 mm width × 45 mm total height, with a horizontal line at 10 mm height indicating the base step level."
            },
            {
              "step": 4,
              "title": "Projection Alignment & ISO Dimensioning",
              "description": "Align TV vertically under FV with continuous projection rays. Project horizontal coordinates from FV and 45° miter line from TV to form the Side View. Place dimensions 60, 35, 45, 10, and 25 using aligned system with 3:1 arrowheads."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Accurate Front View (FV) with correct stepped profile",
              "marks": 3
            },
            {
              "criterion": "Accurate Top View (TV) with correct boundary dividing line",
              "marks": 3
            },
            {
              "criterion": "Accurate Side View (SV) projected using 45° miter / alignment",
              "marks": 2
            },
            {
              "criterion": "Standard ISO dimensioning, projection alignment, and line quality",
              "marks": 2
            }
          ]
        }
      ]
    }
  },
  {
    "id": "mec136-midterm-paper-4",
    "code": "23241MEC20623-D",
    "title": "Midterm Examination • Paper 4 (Third Angle Industrial Orthographic Blueprint)",
    "courseCode": "MEC136",
    "courseName": "Engineering Graphics and CAD",
    "examType": "Midterm Drafting Examination (Subjective)",
    "isDraftingExam": true,
    "durationMinutes": 90,
    "totalQuestions": 8,
    "maxMarks": 40,
    "difficulty": "University Standard",
    "topics": [
      "Diagonal Scales",
      "Projections of Lines",
      "Orthographic Multi-View",
      "First & Third Angle",
      "CAD Studio"
    ],
    "description": "Industrial blueprint drafting extracting Third Angle orthographic projections from a 3D Flanged Shaft Coupling with hidden detail lines and ISO standard dimensioning.",
    "partA": {
      "title": "Part-A: Technical & Conceptual Fundamentals",
      "instructions": "Answer all 5 questions. Each question carries 2 marks.",
      "marks": 10,
      "questions": [
        {
          "id": "q1a",
          "questionNumber": "Q1 (a)",
          "title": "Difference between Plain and Diagonal Scales",
          "marks": 2,
          "topic": "Scales",
          "prompt": "What is the fundamental difference between plain and diagonal scales?",
          "modelAnswer": {
            "summary": "Plain scale reads two consecutive units; Diagonal scale reads three consecutive units based on the principle of similar triangles.",
            "points": [
              "Plain Scale: Measures two consecutive units (e.g. metres and decimetres, or kilometres and hectometres), or a single unit and its primary subdivision (up to 1 decimal place).",
              "Diagonal Scale: Measures three consecutive units (e.g. metres, decimetres, and centimetres, or yards, feet, and inches), or up to two decimal places (e.g. 4.75 m) using the principle of diagonal division of similar triangles."
            ],
            "keyFormula": "Principle of Diagonal Scale: In a right-angled triangle, parallel divisions along the perpendicular are proportional to the base: x_n = (n / N) × Base."
          }
        },
        {
          "id": "q1b",
          "questionNumber": "Q1 (b)",
          "title": "Quadrant Identification for Points",
          "marks": 2,
          "topic": "Projections of Points",
          "prompt": "Name the quadrant for a point which is below HP (Horizontal Plane) and behind VP (Vertical Plane).",
          "modelAnswer": {
            "summary": "Third Quadrant (3rd Angle).",
            "points": [
              "First Quadrant: Above HP, in front of VP (1st angle projection).",
              "Second Quadrant: Above HP, behind VP.",
              "Third Quadrant: Below HP, behind VP (3rd angle projection: Top view above XY, Front view below XY).",
              "Fourth Quadrant: Below HP, in front of VP."
            ],
            "keyFormula": "Position: Below HP (-y) and Behind VP (-x) ⟹ 3rd Quadrant."
          }
        },
        {
          "id": "q1c",
          "questionNumber": "Q1 (c)",
          "title": "Definition of Apparent and True Length of a Line",
          "marks": 2,
          "topic": "Projections of Lines",
          "prompt": "Define apparent length and true length of a straight line in engineering graphics.",
          "modelAnswer": {
            "summary": "True length is the actual 3D length measured when parallel to a projection plane; Apparent length is the foreshortened projected length when inclined.",
            "points": [
              "True Length (TL): The actual, true physical distance between two endpoints in space. A projection displays true length only when the line is parallel to that projection plane.",
              "Apparent Length: The foreshortened length of the line as seen in a projection when the line is inclined at an angle to the plane of projection (e.g., apparent length in TV = TL · cos θ)."
            ],
            "keyFormula": "Apparent Length (Plan/Elevation) = True Length × cos(angle of inclination)."
          }
        },
        {
          "id": "q1d",
          "questionNumber": "Q1 (d)",
          "title": "Symbols of First Angle and Third Angle Projection",
          "marks": 2,
          "topic": "Projection Symbols",
          "prompt": "Describe and sketch the standard ISO symbols for First Angle and Third Angle projections.",
          "modelAnswer": {
            "summary": "Both symbols depict a truncated cone (frustum) of diameter D and d, length L, with concentric circles indicating the end view.",
            "points": [
              "First Angle Projection Symbol: The side view (two concentric circles of diameter D and d) is drawn on the right-hand side of the frustum when viewed from the left (object between observer and plane).",
              "Third Angle Projection Symbol: The side view (concentric circles) is placed on the left-hand side, between the observer and the frustum (plane between observer and object)."
            ],
            "keyFormula": "Concentric circles position relative to trapezoid frustum defines 1st vs 3rd angle."
          }
        },
        {
          "id": "q1e",
          "questionNumber": "Q1 (e)",
          "title": "Definition and Principles of Orthographic Projection",
          "marks": 2,
          "topic": "Orthographic Projection",
          "prompt": "What do you mean by orthographic projection? Why are the 2nd and 4th quadrants avoided in practice?",
          "modelAnswer": {
            "summary": "Orthographic projection projects 3D features onto perpendicular 2D reference planes using parallel rays normal to the planes. 2nd & 4th quadrants cause overlapping views.",
            "points": [
              "Definition: A system of drawing in which parallel projection lines (projectors) are perpendicular (ortho = 90°) to the projection planes (HP and VP).",
              "Why 2nd and 4th angles are avoided: When HP is rotated by 90° clockwise to align with VP, both the Front View and Top View fall on the same side of the XY reference line (both above XY in 2nd angle, both below in 4th angle), causing views to overlap and create severe ambiguity."
            ],
            "keyFormula": "Orthogonal condition: Projectors ⊥ Projection Planes; Avoid overlap in 2nd & 4th quadrants."
          }
        }
      ]
    },
    "partB": {
      "title": "Part-B: Engineering Blueprint Drafting & Construction",
      "instructions": "Answer all 3 drafting problems. Each problem carries 10 marks.",
      "marks": 30,
      "problems": [
        {
          "id": "p2",
          "questionNumber": "Q2",
          "title": "Construction of Diagonal Scale",
          "marks": 10,
          "topic": "Scales Construction",
          "problemStatement": "Construct a diagonal scale, having Representative Fraction R.F. = 1/50, showing metres, decimetres and centimetres, to measure up to 5 metres. Mark a distance of 4.75 m on it.",
          "specifications": {
            "rf": "1/50",
            "maxMeasurement": "5 metres",
            "unitsShown": "Metres (Main), Decimetres (Subdivision), Centimetres (Diagonal)",
            "lengthToMark": "4.75 m"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Calculate Length of Scale (LOS)",
              "description": "LOS = R.F. × Maximum Length to be measured = (1/50) × 5 m = (1/50) × 500 cm = 10 cm."
            },
            {
              "step": 2,
              "title": "Draw the Outer Scale Boundary",
              "description": "Draw a horizontal line of length 10 cm. Construct a rectangle of height 5 cm (allowing 10 equal diagonal divisions of 5 mm each)."
            },
            {
              "step": 3,
              "title": "Primary Division for Metres",
              "description": "Divide the 10 cm length into 5 equal major divisions, each representing 1 metre (length of each part = 2 cm). Label the 0 mark after the first block: 0, 1, 2, 3, 4 to the right."
            },
            {
              "step": 4,
              "title": "Secondary Division for Decimetres",
              "description": "Divide the first 2 cm block (to the left of 0) into 10 equal parts of 2 mm each. Each sub-part represents 1 decimetre (0.1 m). Label 0 to 10 going left."
            },
            {
              "step": 5,
              "title": "Vertical Diagonal Division for Centimetres",
              "description": "Divide the 5 cm vertical edge into 10 equal parts of 5 mm each, representing 1 centimetre (0.01 m) each. Draw diagonal lines from division n on the bottom to (n+1) on the top line."
            },
            {
              "step": 6,
              "title": "Measure and Mark 4.75 m",
              "description": "Take 4 metres on the main scale to the right of 0. Move 7 decimetres to the left of 0 along the bottom line. Move vertically up along the 7th diagonal to the 5th horizontal centimetre line. Draw dimension line with arrowheads and label \"4.75 m\"."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Calculation of LOS (10 cm) & Formula",
              "marks": 2
            },
            {
              "criterion": "Equal division of main scale (5 parts) & decimetres (10 parts)",
              "marks": 3
            },
            {
              "criterion": "Accurate construction of diagonal lines (10 parts) & parallelism",
              "marks": 3
            },
            {
              "criterion": "Accurate marking of 4.75 m with standard dimensioning & lettering",
              "marks": 2
            }
          ]
        },
        {
          "id": "p3",
          "questionNumber": "Q3",
          "title": "Projections of Straight Line with Traces",
          "marks": 10,
          "topic": "Projections of Straight Lines",
          "problemStatement": "Represent the projection of line AB 60 mm long inclined to HP at 45° and parallel to VP. The nearest end A is 20 mm above HP and 25 mm in front of VP. Also locate and show the trace of the line.",
          "specifications": {
            "trueLength": "60 mm",
            "inclinationHP": "θ = 45°",
            "inclinationVP": "φ = 0° (Parallel to VP)",
            "positionA": "20 mm above HP, 25 mm in front of VP"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Draw Reference Line XY",
              "description": "Draw a horizontal reference line XY. Above XY represents VP (Front View); below XY represents HP (Top View) in 1st angle projection."
            },
            {
              "step": 2,
              "title": "Plot End A Coordinates",
              "description": "Draw a vertical projector perpendicular to XY. Mark front view point a' at 20 mm above XY. Mark top view point a at 25 mm below XY."
            },
            {
              "step": 3,
              "title": "Construct Front View (Elevation)",
              "description": "Since the line is parallel to VP, its front view exhibits True Length (60 mm). From a', draw line a'b' = 60 mm inclined at θ = 45° to XY. Measure vertical height of b' from XY = 20 + 60 sin(45°) = 20 + 42.43 = 62.43 mm."
            },
            {
              "step": 4,
              "title": "Construct Top View (Plan)",
              "description": "From a, draw a horizontal line parallel to XY (since line is parallel to VP, every point is 25 mm in front of VP). Drop a vertical projector from b' to intersect this horizontal line at b. Apparent length ab = 60 cos(45°) = 42.43 mm."
            },
            {
              "step": 5,
              "title": "Locate Traces of the Line",
              "description": "Extend front view line b'a' downward until it intersects XY at point h'. Drop a vertical projector from h' to meet the extension of top view line ba at H (Horizontal Trace). Distance of HT from XY = 25 mm. Since the line is parallel to VP, it does not pierce VP; hence, Vertical Trace (VT) does not exist (at infinity)."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Reference line XY and correct projection of point A",
              "marks": 2
            },
            {
              "criterion": "Front view a'b' drawn at 45° true length (60 mm)",
              "marks": 3
            },
            {
              "criterion": "Top view ab drawn parallel to XY with correct apparent length (42.4 mm)",
              "marks": 3
            },
            {
              "criterion": "Correct construction and labeling of Horizontal Trace (HT)",
              "marks": 2
            }
          ]
        },
        {
          "id": "p4",
          "questionNumber": "Q4",
          "title": "Orthographic Multi-View Drafting from 3D Isometric View",
          "marks": 10,
          "topic": "Orthographic Projection",
          "problemStatement": "Given the specified 3D isometric component (stepped slotted block: Base 60 mm × 35 mm, overall height 45 mm, step height 10 mm, upper block 35 mm × 35 mm). Draw the following views in First Angle Projection: (a) Front View looking in direction of arrow X, (b) Top View, (c) Left Side View. Include all visible outlines, hidden lines, and standard dimensioning.",
          "specifications": {
            "overallDimensions": "60 mm (Length) × 35 mm (Width) × 45 mm (Height)",
            "basePlate": "60 mm × 35 mm × 10 mm thick",
            "stepBlock": "35 mm length × 35 mm width × 35 mm height above base (total 45 mm)",
            "projectionSystem": "First Angle Projection (FV above XY, TV below XY, Left Side View on Right of FV)"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Front View (Elevation - Looking along Arrow X)",
              "description": "Width = 60 mm, Height = 45 mm. Bottom base rectangle: 60 mm wide × 10 mm high. Right vertical step: 35 mm wide × 35 mm high rising from the base to total height 45 mm. Remaining left ledge: 25 mm wide at height 10 mm."
            },
            {
              "step": 2,
              "title": "Top View (Plan - Looking from directly above)",
              "description": "Length = 60 mm, Width = 35 mm. The top view is an enclosing rectangle of 60 mm × 35 mm. A vertical boundary line divides it into two surfaces: the lower step on the left (25 mm × 35 mm) and the elevated top surface on the right (35 mm × 35 mm)."
            },
            {
              "step": 3,
              "title": "Left Side View (Looking from left, drawn on right of FV)",
              "description": "Width = 35 mm, Height = 45 mm. From the left, the object appears as an upright L-profile or single enclosing block of 35 mm width × 45 mm total height, with a horizontal line at 10 mm height indicating the base step level."
            },
            {
              "step": 4,
              "title": "Projection Alignment & ISO Dimensioning",
              "description": "Align TV vertically under FV with continuous projection rays. Project horizontal coordinates from FV and 45° miter line from TV to form the Side View. Place dimensions 60, 35, 45, 10, and 25 using aligned system with 3:1 arrowheads."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Accurate Front View (FV) with correct stepped profile",
              "marks": 3
            },
            {
              "criterion": "Accurate Top View (TV) with correct boundary dividing line",
              "marks": 3
            },
            {
              "criterion": "Accurate Side View (SV) projected using 45° miter / alignment",
              "marks": 2
            },
            {
              "criterion": "Standard ISO dimensioning, projection alignment, and line quality",
              "marks": 2
            }
          ]
        }
      ]
    }
  },
  {
    "id": "mec136-midterm-paper-5",
    "code": "23241MEC20623-E",
    "title": "Midterm Examination • Paper 5 (Isometric to Orthographic Master Challenge)",
    "courseCode": "MEC136",
    "courseName": "Engineering Graphics and CAD",
    "examType": "Midterm Drafting Examination (Subjective)",
    "isDraftingExam": true,
    "durationMinutes": 90,
    "totalQuestions": 8,
    "maxMarks": 40,
    "difficulty": "University Standard",
    "topics": [
      "Diagonal Scales",
      "Projections of Lines",
      "Orthographic Multi-View",
      "First & Third Angle",
      "CAD Studio"
    ],
    "description": "Comprehensive university drafting examination requiring Vernier Scale construction, Line with both traces, and complete multi-view extraction from a complex slotted prism.",
    "partA": {
      "title": "Part-A: Technical & Conceptual Fundamentals",
      "instructions": "Answer all 5 questions. Each question carries 2 marks.",
      "marks": 10,
      "questions": [
        {
          "id": "q1a",
          "questionNumber": "Q1 (a)",
          "title": "Difference between Plain and Diagonal Scales",
          "marks": 2,
          "topic": "Scales",
          "prompt": "What is the fundamental difference between plain and diagonal scales?",
          "modelAnswer": {
            "summary": "Plain scale reads two consecutive units; Diagonal scale reads three consecutive units based on the principle of similar triangles.",
            "points": [
              "Plain Scale: Measures two consecutive units (e.g. metres and decimetres, or kilometres and hectometres), or a single unit and its primary subdivision (up to 1 decimal place).",
              "Diagonal Scale: Measures three consecutive units (e.g. metres, decimetres, and centimetres, or yards, feet, and inches), or up to two decimal places (e.g. 4.75 m) using the principle of diagonal division of similar triangles."
            ],
            "keyFormula": "Principle of Diagonal Scale: In a right-angled triangle, parallel divisions along the perpendicular are proportional to the base: x_n = (n / N) × Base."
          }
        },
        {
          "id": "q1b",
          "questionNumber": "Q1 (b)",
          "title": "Quadrant Identification for Points",
          "marks": 2,
          "topic": "Projections of Points",
          "prompt": "Name the quadrant for a point which is below HP (Horizontal Plane) and behind VP (Vertical Plane).",
          "modelAnswer": {
            "summary": "Third Quadrant (3rd Angle).",
            "points": [
              "First Quadrant: Above HP, in front of VP (1st angle projection).",
              "Second Quadrant: Above HP, behind VP.",
              "Third Quadrant: Below HP, behind VP (3rd angle projection: Top view above XY, Front view below XY).",
              "Fourth Quadrant: Below HP, in front of VP."
            ],
            "keyFormula": "Position: Below HP (-y) and Behind VP (-x) ⟹ 3rd Quadrant."
          }
        },
        {
          "id": "q1c",
          "questionNumber": "Q1 (c)",
          "title": "Definition of Apparent and True Length of a Line",
          "marks": 2,
          "topic": "Projections of Lines",
          "prompt": "Define apparent length and true length of a straight line in engineering graphics.",
          "modelAnswer": {
            "summary": "True length is the actual 3D length measured when parallel to a projection plane; Apparent length is the foreshortened projected length when inclined.",
            "points": [
              "True Length (TL): The actual, true physical distance between two endpoints in space. A projection displays true length only when the line is parallel to that projection plane.",
              "Apparent Length: The foreshortened length of the line as seen in a projection when the line is inclined at an angle to the plane of projection (e.g., apparent length in TV = TL · cos θ)."
            ],
            "keyFormula": "Apparent Length (Plan/Elevation) = True Length × cos(angle of inclination)."
          }
        },
        {
          "id": "q1d",
          "questionNumber": "Q1 (d)",
          "title": "Symbols of First Angle and Third Angle Projection",
          "marks": 2,
          "topic": "Projection Symbols",
          "prompt": "Describe and sketch the standard ISO symbols for First Angle and Third Angle projections.",
          "modelAnswer": {
            "summary": "Both symbols depict a truncated cone (frustum) of diameter D and d, length L, with concentric circles indicating the end view.",
            "points": [
              "First Angle Projection Symbol: The side view (two concentric circles of diameter D and d) is drawn on the right-hand side of the frustum when viewed from the left (object between observer and plane).",
              "Third Angle Projection Symbol: The side view (concentric circles) is placed on the left-hand side, between the observer and the frustum (plane between observer and object)."
            ],
            "keyFormula": "Concentric circles position relative to trapezoid frustum defines 1st vs 3rd angle."
          }
        },
        {
          "id": "q1e",
          "questionNumber": "Q1 (e)",
          "title": "Definition and Principles of Orthographic Projection",
          "marks": 2,
          "topic": "Orthographic Projection",
          "prompt": "What do you mean by orthographic projection? Why are the 2nd and 4th quadrants avoided in practice?",
          "modelAnswer": {
            "summary": "Orthographic projection projects 3D features onto perpendicular 2D reference planes using parallel rays normal to the planes. 2nd & 4th quadrants cause overlapping views.",
            "points": [
              "Definition: A system of drawing in which parallel projection lines (projectors) are perpendicular (ortho = 90°) to the projection planes (HP and VP).",
              "Why 2nd and 4th angles are avoided: When HP is rotated by 90° clockwise to align with VP, both the Front View and Top View fall on the same side of the XY reference line (both above XY in 2nd angle, both below in 4th angle), causing views to overlap and create severe ambiguity."
            ],
            "keyFormula": "Orthogonal condition: Projectors ⊥ Projection Planes; Avoid overlap in 2nd & 4th quadrants."
          }
        }
      ]
    },
    "partB": {
      "title": "Part-B: Engineering Blueprint Drafting & Construction",
      "instructions": "Answer all 3 drafting problems. Each problem carries 10 marks.",
      "marks": 30,
      "problems": [
        {
          "id": "p2",
          "questionNumber": "Q2",
          "title": "Construction of Diagonal Scale",
          "marks": 10,
          "topic": "Scales Construction",
          "problemStatement": "Construct a diagonal scale, having Representative Fraction R.F. = 1/50, showing metres, decimetres and centimetres, to measure up to 5 metres. Mark a distance of 4.75 m on it.",
          "specifications": {
            "rf": "1/50",
            "maxMeasurement": "5 metres",
            "unitsShown": "Metres (Main), Decimetres (Subdivision), Centimetres (Diagonal)",
            "lengthToMark": "4.75 m"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Calculate Length of Scale (LOS)",
              "description": "LOS = R.F. × Maximum Length to be measured = (1/50) × 5 m = (1/50) × 500 cm = 10 cm."
            },
            {
              "step": 2,
              "title": "Draw the Outer Scale Boundary",
              "description": "Draw a horizontal line of length 10 cm. Construct a rectangle of height 5 cm (allowing 10 equal diagonal divisions of 5 mm each)."
            },
            {
              "step": 3,
              "title": "Primary Division for Metres",
              "description": "Divide the 10 cm length into 5 equal major divisions, each representing 1 metre (length of each part = 2 cm). Label the 0 mark after the first block: 0, 1, 2, 3, 4 to the right."
            },
            {
              "step": 4,
              "title": "Secondary Division for Decimetres",
              "description": "Divide the first 2 cm block (to the left of 0) into 10 equal parts of 2 mm each. Each sub-part represents 1 decimetre (0.1 m). Label 0 to 10 going left."
            },
            {
              "step": 5,
              "title": "Vertical Diagonal Division for Centimetres",
              "description": "Divide the 5 cm vertical edge into 10 equal parts of 5 mm each, representing 1 centimetre (0.01 m) each. Draw diagonal lines from division n on the bottom to (n+1) on the top line."
            },
            {
              "step": 6,
              "title": "Measure and Mark 4.75 m",
              "description": "Take 4 metres on the main scale to the right of 0. Move 7 decimetres to the left of 0 along the bottom line. Move vertically up along the 7th diagonal to the 5th horizontal centimetre line. Draw dimension line with arrowheads and label \"4.75 m\"."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Calculation of LOS (10 cm) & Formula",
              "marks": 2
            },
            {
              "criterion": "Equal division of main scale (5 parts) & decimetres (10 parts)",
              "marks": 3
            },
            {
              "criterion": "Accurate construction of diagonal lines (10 parts) & parallelism",
              "marks": 3
            },
            {
              "criterion": "Accurate marking of 4.75 m with standard dimensioning & lettering",
              "marks": 2
            }
          ]
        },
        {
          "id": "p3",
          "questionNumber": "Q3",
          "title": "Projections of Straight Line with Traces",
          "marks": 10,
          "topic": "Projections of Straight Lines",
          "problemStatement": "Represent the projection of line AB 60 mm long inclined to HP at 45° and parallel to VP. The nearest end A is 20 mm above HP and 25 mm in front of VP. Also locate and show the trace of the line.",
          "specifications": {
            "trueLength": "60 mm",
            "inclinationHP": "θ = 45°",
            "inclinationVP": "φ = 0° (Parallel to VP)",
            "positionA": "20 mm above HP, 25 mm in front of VP"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Draw Reference Line XY",
              "description": "Draw a horizontal reference line XY. Above XY represents VP (Front View); below XY represents HP (Top View) in 1st angle projection."
            },
            {
              "step": 2,
              "title": "Plot End A Coordinates",
              "description": "Draw a vertical projector perpendicular to XY. Mark front view point a' at 20 mm above XY. Mark top view point a at 25 mm below XY."
            },
            {
              "step": 3,
              "title": "Construct Front View (Elevation)",
              "description": "Since the line is parallel to VP, its front view exhibits True Length (60 mm). From a', draw line a'b' = 60 mm inclined at θ = 45° to XY. Measure vertical height of b' from XY = 20 + 60 sin(45°) = 20 + 42.43 = 62.43 mm."
            },
            {
              "step": 4,
              "title": "Construct Top View (Plan)",
              "description": "From a, draw a horizontal line parallel to XY (since line is parallel to VP, every point is 25 mm in front of VP). Drop a vertical projector from b' to intersect this horizontal line at b. Apparent length ab = 60 cos(45°) = 42.43 mm."
            },
            {
              "step": 5,
              "title": "Locate Traces of the Line",
              "description": "Extend front view line b'a' downward until it intersects XY at point h'. Drop a vertical projector from h' to meet the extension of top view line ba at H (Horizontal Trace). Distance of HT from XY = 25 mm. Since the line is parallel to VP, it does not pierce VP; hence, Vertical Trace (VT) does not exist (at infinity)."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Reference line XY and correct projection of point A",
              "marks": 2
            },
            {
              "criterion": "Front view a'b' drawn at 45° true length (60 mm)",
              "marks": 3
            },
            {
              "criterion": "Top view ab drawn parallel to XY with correct apparent length (42.4 mm)",
              "marks": 3
            },
            {
              "criterion": "Correct construction and labeling of Horizontal Trace (HT)",
              "marks": 2
            }
          ]
        },
        {
          "id": "p4",
          "questionNumber": "Q4",
          "title": "Orthographic Multi-View Drafting from 3D Isometric View",
          "marks": 10,
          "topic": "Orthographic Projection",
          "problemStatement": "Given the specified 3D isometric component (stepped slotted block: Base 60 mm × 35 mm, overall height 45 mm, step height 10 mm, upper block 35 mm × 35 mm). Draw the following views in First Angle Projection: (a) Front View looking in direction of arrow X, (b) Top View, (c) Left Side View. Include all visible outlines, hidden lines, and standard dimensioning.",
          "specifications": {
            "overallDimensions": "60 mm (Length) × 35 mm (Width) × 45 mm (Height)",
            "basePlate": "60 mm × 35 mm × 10 mm thick",
            "stepBlock": "35 mm length × 35 mm width × 35 mm height above base (total 45 mm)",
            "projectionSystem": "First Angle Projection (FV above XY, TV below XY, Left Side View on Right of FV)"
          },
          "draftingProcedure": [
            {
              "step": 1,
              "title": "Front View (Elevation - Looking along Arrow X)",
              "description": "Width = 60 mm, Height = 45 mm. Bottom base rectangle: 60 mm wide × 10 mm high. Right vertical step: 35 mm wide × 35 mm high rising from the base to total height 45 mm. Remaining left ledge: 25 mm wide at height 10 mm."
            },
            {
              "step": 2,
              "title": "Top View (Plan - Looking from directly above)",
              "description": "Length = 60 mm, Width = 35 mm. The top view is an enclosing rectangle of 60 mm × 35 mm. A vertical boundary line divides it into two surfaces: the lower step on the left (25 mm × 35 mm) and the elevated top surface on the right (35 mm × 35 mm)."
            },
            {
              "step": 3,
              "title": "Left Side View (Looking from left, drawn on right of FV)",
              "description": "Width = 35 mm, Height = 45 mm. From the left, the object appears as an upright L-profile or single enclosing block of 35 mm width × 45 mm total height, with a horizontal line at 10 mm height indicating the base step level."
            },
            {
              "step": 4,
              "title": "Projection Alignment & ISO Dimensioning",
              "description": "Align TV vertically under FV with continuous projection rays. Project horizontal coordinates from FV and 45° miter line from TV to form the Side View. Place dimensions 60, 35, 45, 10, and 25 using aligned system with 3:1 arrowheads."
            }
          ],
          "scoringRubric": [
            {
              "criterion": "Accurate Front View (FV) with correct stepped profile",
              "marks": 3
            },
            {
              "criterion": "Accurate Top View (TV) with correct boundary dividing line",
              "marks": 3
            },
            {
              "criterion": "Accurate Side View (SV) projected using 45° miter / alignment",
              "marks": 2
            },
            {
              "criterion": "Standard ISO dimensioning, projection alignment, and line quality",
              "marks": 2
            }
          ]
        }
      ]
    }
  }
];
