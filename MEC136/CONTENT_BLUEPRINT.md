# MEC136 Master Content Blueprint & Syllabus Specifications

## 1. Core Subject Information
- **Course Code**: MEC136
- **Course Title**: Engineering Graphics / Engineering Drawing & Computer Aided Drafting (AutoCAD)
- **Institution**: Lovely Professional University (LPU)
- **Primary Source Material**: Official MEC136 Courseware Notes (Units 1 to 6)

---

## 2. Unit-by-Unit Blueprint

### Unit 1: Introduction to Engineering Drawing & AutoCAD Setup
- Drawing Instruments: Drawing board, Mini-drafter / T-square, Set squares ($45^\circ, 30^\circ\text{--}60^\circ$), Compass, Dividers, Pencil lead grades ($4\text{H--}6\text{H}$ hard, $\text{H--}2\text{H}$ medium, $\text{HB--B}$ soft), French curves.
- Alphabet of Lines (ISO/ANSI): Visible/Object line, Hidden line, Center line, Construction line, Dimension/Extension line, Cutting plane line.
- Dimensioning Mechanics: Extension line, Dimension line, Arrowheads ($3:1$ ratio), Leader lines. Systems: Aligned vs. Unidirectional.
- Single Stroke Vertical Gothic Lettering: Aspect ratio $7:4$ ($M/W$ $7:5$ or $7:6$, $I$ single stroke), uppercase, stability rule, letter spacing $\frac{1}{5}h$, word spacing $1h$, line spacing $\frac{1}{2}h\text{--}1h$.
- Scales: Representative Fraction ($R.F. = \frac{\text{Drawing Length}}{\text{Actual Length}}$), Length of Scale ($L.O.S. = R.F. \times \text{Max Length}$), Full scale ($1:1$), Reducing scale ($1:X$), Enlarging scale ($X:1$), Plain scales (2 units / 1st subdivision), Diagonal scales (3 units / 2 decimal places using Similar Triangles principle).
- AutoCAD Interface & Setup: Application menu, Ribbon, Viewport, UCS icon, Command line, Status bar. Setup commands: `UNITS` (`UN`), `LIMITS` ($0,0$ to $210,297$ for A4), `ZOOM ALL` (`Z` $\to$ `A`). Navigation: Pan (`P`), Zoom (`Z`). Drawing aids: `OSNAP` (`F3`), `ORTHO` (`F8`), UCS ($WCS$ vs $UCS$). Function keys `F1--F12`.

### Unit 2: Projection of Points & Lines (Manual & AutoCAD)
- Orthographic Projection Principles: Principal Planes (VP $\to$ Front View/Elevation, HP $\to$ Top View/Plan, Reference line $XY$, Profile Plane PP $\to$ Side View).
- Quadrant Principles & Projection Systems: First Angle (ISO: Observer $\to$ Object $\to$ Plane, FV above $XY$, TV below $XY$) vs Third Angle (ANSI: Observer $\to$ Plane $\to$ Object, TV above $XY$, FV below $XY$).
- Point Projections: Notation (Actual $A$, FV $a'$, TV $a$). Rules for $1^{\text{st}}, 2^{\text{nd}}, 3^{\text{rd}}, 4^{\text{th}}$ quadrants.
- Straight Line Projections: 6 Orientation Cases (Parallel to both, Perpendicular to one, Inclined to one, Inclined to both). True length ($TL$), Apparent lengths ($a'b', ab$), True angles ($\theta, \phi$), Apparent angles ($\alpha, \beta$). Rotating Line Method & Trapezoidal Method.
- Traces of Lines: Horizontal Trace (HT) and Vertical Trace (VT) location.
- AutoCAD Point/Line Drafting: `LINE` (`L`), `CIRCLE` (`C`), `ARC` (`A`), `PLINE` (`PL`), `RECTANG` (`REC`), `POLYGON` (`POL`), `ELLIPSE` (`EL`). Dimensioning: `DIMSTYLE` (`D`), `DIMLINEAR` (`DLI`), `DIMALIGNED` (`DAL`), `DIMANGULAR` (`DAN`).

### Unit 3: Orthographic Projections of Objects (2D Views & Modifications)
- Multi-View Principles: Projectors, Planes of Projection, "Glass Box" concept and unfolding.
- View Arrangements: First Angle (FV above $XY$, TV below FV, Left Side View to right of FV) vs Third Angle (FV below $XY$, TV above FV, Right Side View to right of FV).
- Miter-Line Method: $45^\circ$ line projection for transferring depth dimensions between TV and Side View.
- AutoCAD Layers & Modification Commands: `LINETYPE`, `LTSCALE`, `MOVE` (`M`), `COPY` (`CO`/`CP`), `ROTATE` (`RO`), `TRIM` (`TR`), `ERASE` (`E`), `MIRROR` (`MI`), `SCALE` (`SC`), `FILLET` (`F`), `CHAMFER` (`CHA`), `ARRAY` (`AR`). Complete 2D Drafting Workflow.

### Unit 4: Sectional Views & Hatching Standards
- Purpose & Fundamentals: Reveal internal features, reduce hidden lines, facilitate dimensioning.
- Cutting Plane & Section Lines: Cutting Plane Line (thick chain with arrows pointing in viewing direction), Section Lines ($45^\circ$ thin continuous lines, ANSI31).
- Types of Sections: Full Section (passes straight through), Half Section (quarter removed, symmetrical objects, center line division), Offset Section (bends/steps through offset features, bends not shown in section).
- Non-Hatching Exceptions: Thin webs/ribs cut longitudinally, fasteners (bolts, nuts, screws), shafts, pins, solid rods.
- AutoCAD Sectioning Commands: `STRETCH` (`S`), `EXPLODE` (`X`), `OFFSET` (`O`), `EXTEND` (`EX`), `JOIN` (`J`), `REGION` (`REG`), `BREAK` (`BR`), `HATCH` (`H` - ANSI31, scale, Pick Points vs Select Objects), `HATCHEDIT` (`HE`).

### Unit 5: Isometric Views & 3D Modeling Fundamentals
- Isometric Principles: Axonometric projection, 3 principal axes at $120^\circ$, 2 receding at $30^\circ$ to horizontal line.
- Terminology: Isometric Axes (Vertical, Right $30^\circ$, Left $30^\circ$), Isometric Lines (parallel to axes, directly measurable), Non-Isometric Lines (not parallel, cannot be measured directly), Isometric Planes.
- Isometric Scale: Ratio $\frac{\text{Isometric Length}}{\text{True Length}} = \frac{\cos 45^\circ}{\cos 30^\circ} = \sqrt{\frac{2}{3}} \approx 0.816$. Isometric View/Drawing (True Scale $1:1$) vs. Isometric Projection (Reduced Scale $0.816$).
- Solid Construction: Box Method (enclosing box), Composite/Stacked Solids (e.g., cylinder on cube, sphere on cylinder). Isometric Dimensioning (Aligned system, obliqued text $-30^\circ / +30^\circ$).
- AutoCAD 3D Commands: `3P UCS` (`UCS` $\to$ `3`), Primitives (`BOX`, `CYLINDER`, `CONE`, `SPHERE`, `WEDGE`, `TORUS`), `EXTRUDE`, `REVOLVE`, `PRESSPULL`.

### Unit 6: Development of Surfaces & 3D Solid Editing
- Principles of Surface Development: Unfolding/unrolling 3D surface into 2D flat pattern. Applications: sheet metal, ducts, hoppers, pipes, funnels, chimneys.
- Governing Rules: Stretch-out line (full perimeter), True Length ($TL$) required for all edges, Seam selection along shortest edge.
- Methods of Development:
  - Parallel Line Method: Prisms and Cylinders ($L = \text{Perimeter}$).
  - Radial Line Method: Pyramids and Cones ($\theta = \frac{r}{L} \times 360^\circ$).
  - Triangulation Method: Transition pieces (square-to-round adapters).
- Truncated Solids: Projecting cut points from Front View horizontally (Parallel Line Method) or via concentric arcs (Radial Line Method).
- AutoCAD 3D Solid Editing: Boolean operations (`UNION` / `UNI`, `SUBTRACT` / `SU`, `INTERSECT` / `IN`), `3DORBIT` (`3DO`), Visual Styles (`VS`), `VIEWBASE` (2D drawings from 3D models).
