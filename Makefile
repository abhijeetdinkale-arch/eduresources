all: physics cse111 mth165 int108 cse326 ece249 ece279 mec136

physics:
	@echo "==> Building Engineering Physics Book..."
	$(MAKE) -C Physics

physics_qb:
	@echo "==> Building PHY110: 600 MCQs + 120 Theory Questions Question Bank..."
	$(MAKE) -C Physics_Question_Bank

physics_exam:
	@echo "==> Building PHY110: Complete Examination Companion (CA-1, CA-2, Mid-Term, End-Term)..."
	$(MAKE) -C Physics_Exam_Companion

physics_formula:
	@echo "==> Building PHY110: Formula & Quick Revision Book..."
	$(MAKE) -C Physics_Formula_Book

physics_essential:
	@echo "==> Building PHY110: Essential Conceptual Physics Book (~50 Pages)..."
	$(MAKE) -C Physics_Essential_Book

physics_all: physics_qb physics_exam physics_formula physics_essential
	@echo "==> All PHY110 Engineering Physics Suite Books Built Successfully!"

cse111:
	@echo "==> Building CSE111: Fundamentals of Computing Book..."
	$(MAKE) -C CSE111

mth165:
	@echo "==> Building MTH165: Engineering Mathematics Comprehensive Textbook..."
	$(MAKE) -C MTH165

mth165_papers:
	@echo "==> Building MTH165: Sample Question Papers Book (16 Complete Papers)..."
	$(MAKE) -C MTH165_Sample_Question_Papers

mth165_exam:
	@echo "==> Building MTH165: Examination Companion Suite..."
	$(MAKE) -C MTH165_Exam_Companion

mth165_qb:
	@echo "==> Building MTH165: Question Bank & PYQ Book..."
	$(MAKE) -C MTH165_Question_Bank

mth165_formula:
	@echo "==> Building MTH165: Master Formula & Rapid Revision Book..."
	$(MAKE) -C MTH165_Formula_Book

mth165_all: mth165 mth165_papers mth165_qb mth165_formula
	@echo "==> All MTH165 Books Built Successfully!"

int108:
	@echo "==> Building INT108: Python Programming Book..."
	$(MAKE) -C INT108

cse326:
	@echo "==> Building CSE326: Web Development Book..."
	$(MAKE) -C CSE326

ece249:
	@echo "==> Building ECE249: Digital Electronics & Arduino Interfacing Book..."
	$(MAKE) -C ECE249

ece279:
	@echo "==> Building ECE279: Basic Electrical & Electronics Practical Book..."
	$(MAKE) -C ECE279

mec136:
	@echo "==> Building MEC136: Engineering Graphics & AutoCAD Book..."
	$(MAKE) -C MEC136

clean:
	$(MAKE) -C Physics clean || true
	$(MAKE) -C Physics_Question_Bank clean || true
	$(MAKE) -C Physics_Exam_Companion clean || true
	$(MAKE) -C Physics_Formula_Book clean || true
	$(MAKE) -C Physics_Essential_Book clean || true
	$(MAKE) -C CSE111 clean || true
	$(MAKE) -C MTH165 clean || true
	$(MAKE) -C MTH165_Sample_Question_Papers clean || true
	$(MAKE) -C MTH165_Exam_Companion clean || true
	$(MAKE) -C MTH165_Question_Bank clean || true
	$(MAKE) -C MTH165_Formula_Book clean || true
	$(MAKE) -C INT108 clean || true
	$(MAKE) -C CSE326 clean || true
	$(MAKE) -C ECE249 clean || true
	$(MAKE) -C ECE279 clean || true
	$(MAKE) -C MEC136 clean || true

.PHONY: all physics physics_qb physics_exam physics_formula physics_essential physics_all cse111 mth165 mth165_papers mth165_exam mth165_qb mth165_formula mth165_all int108 cse326 ece249 ece279 mec136 clean
