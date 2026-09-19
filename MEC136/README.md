# MEC136: Engineering Graphics & Computer Aided Drafting (AutoCAD)

## Complete Exam Preparation & University Study Book

**Author**: University Engineering Open Courseware Initiative  
**License**: CC BY-NC-SA 4.0 (Text & Educational Material) / MIT License (Build Code)  
**Target Class**: First-Year Undergraduate Engineering Students (Mechanical, Civil, Electrical, ECE, CSE, IT, Robotics)

---

### Course Modules & Syllabus Architecture
- **Unit 1: Introduction to Engineering Drawing & AutoCAD Setup**  
  Conceptual framework of drawing instruments, Alphabet of Lines (ISO/ANSI), Dimensioning rules (Aligned vs Unidirectional), Single-Stroke Vertical Gothic Lettering, Scales (Plain & Diagonal scales based on similar triangles), and AutoCAD 2D Setup (`UNITS`, `LIMITS`, `OSNAP`, `ORTHO`).
- **Unit 2: Projection of Points & Lines (Manual & AutoCAD)**  
  Principal Planes ($VP, HP, PP$), Quadrants ($1^{\text{st}}$ vs $3^{\text{rd}}$ Angle), Point projections across 4 quadrants, Straight Line projections across 6 orientation cases, True Length vs Apparent Lengths, Rotating Line Method, Traces ($HT, VT$), and AutoCAD Line Commands (`LINE`, `PLINE`, `ARC`, `POLYGON`, `ELLIPSE`, `DIMALIGNED`).
- **Unit 3: Orthographic Projections of Objects (2D Views & Modifications)**  
  Multi-view projection theory, Glass Box concept, ISO First Angle vs ANSI Third Angle view arrangements, Miter-Line Method ($45^\circ$), Layer Management, and Modification Commands (`MOVE`, `COPY`, `ROTATE`, `TRIM`, `MIRROR`, `SCALE`, `FILLET`, `CHAMFER`, `ARRAY`).
- **Unit 4: Sectional Views & Hatching Standards**  
  Purpose of sectioning, Cutting plane lines, Hatching standards ($45^\circ$ thin continuous, `ANSI31`), Full Sections, Half Sections, Offset Sections, Non-hatching exceptions (webs/ribs, fasteners, shafts, pins, solid rods), and AutoCAD Editing/Hatching Commands (`STRETCH`, `EXPLODE`, `OFFSET`, `EXTEND`, `REGION`, `HATCH`, `HATCHEDIT`).
- **Unit 5: Isometric Views & 3D Modeling Fundamentals**  
  Isometric principles ($120^\circ$ axes, $30^\circ$ receding axes), Isometric Lines vs Non-Isometric Lines, Isometric Scale derivation factor ($0.816$), Isometric View (True Scale $1:1$) vs Isometric Projection, Box Method for prisms/pyramids/composite solids, 3D Coordinate Systems (`3P UCS`), 3D Primitives, Extrude (`EXTRUDE`), Revolve (`REVOLVE`), and Presspull (`PRESSPULL`).
- **Unit 6: Development of Surfaces & 3D Solid Editing**  
  Surface development theory, Stretch-out line, True Length ($TL$) rules, Parallel Line Method (Prisms/Cylinders), Radial Line Method (Pyramids/Cones, $\theta = \frac{r}{L} \times 360^\circ$), Triangulation Method, Truncated solids, 3D Boolean Operations (`UNION`, `SUBTRACT`, `INTERSECT`), 3D Navigation (`3DORBIT`, Visual Styles), and `VIEWBASE` 2D extraction.
- **Chapter 7: Master Revision Sheet & Formula Reference**  
  Comprehensive unit-wise formula summary, derivation steps, definition index, AutoCAD command cheat sheet, and last-day exam checklists.
- **Chapter 8: Cross-Unit Practical & Synthesis Problems**  
  Integrated multi-concept problems combining Scales, Line Projections, Orthographic Views, Sectioning, Isometric Views, and Surface Development with complete step-by-step solutions.
- **Chapter 9: Complete Full-Length Mock Examinations**  
  Two full university-style 100-mark examination papers with complete marking rubrics, answer keys, and detailed solutions.

---

### Compilation Instructions

To compile the textbook PDF using `make`:

```bash
make clean
make
```

The compiled PDF artifact will be generated at `MEC136/main.pdf`.
