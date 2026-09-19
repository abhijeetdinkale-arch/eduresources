import os
import subprocess

print("Generating unified PHY175 Question Bank...")

os.makedirs("PHY175_Question_Bank/chapters", exist_ok=True)
os.makedirs("PHY175_Question_Bank/frontmatter", exist_ok=True)

# 1. qb_style.sty
qb_style = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{qb_style}[2026/09/18 v1.0 PHY175 Question Bank Style System]

\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=20mm,top=24mm,bottom=24mm,headheight=25pt]{geometry}
\RequirePackage{amsmath,amssymb,amsfonts,mathtools,bm}
\RequirePackage{xcolor}
\RequirePackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\RequirePackage{enumitem}
\RequirePackage{fancyhdr}
\RequirePackage{tabularx}
\RequirePackage{array}
\RequirePackage{titlesec}
\RequirePackage{booktabs}
\RequirePackage{microtype}
\RequirePackage[hidelinks,colorlinks=true,linkcolor=NavyBlue,urlcolor=BrickRed,citecolor=NavyBlue]{hyperref}

\definecolor{LPUNavy}{RGB}{15, 32, 67}
\definecolor{LPUOrange}{RGB}{201, 74, 28}
\definecolor{DarkSlate}{RGB}{35, 45, 55}
\definecolor{LightBg}{RGB}{246, 248, 252}
\definecolor{BorderGray}{RGB}{205, 215, 225}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\color{LPUNavy}\textbf{PHY175: Modern Physics \& Electronics --- Question Bank}}
\fancyhead[R]{\small\color{LPUOrange}\textbf{\leftmark}}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}

\titleformat{\chapter}[display]
  {\normalfont\huge\bfseries\color{LPUNavy}}{\chaptertitlename\ \thechapter}{12pt}{\Huge}
\titleformat{\section}
  {\normalfont\Large\bfseries\color{LPUNavy}}{\thesection}{1em}{}
\titleformat{\subsection}
  {\normalfont\large\bfseries\color{LPUOrange}}{\thesubsection}{1em}{}

\newtcolorbox{theoryq}[2][]{
    enhanced,
    breakable,
    colback=white,
    colframe=LPUNavy,
    fonttitle=\bfseries\color{white},
    coltitle=white,
    title={Theory Question #2 \hfill [University Exam / Analytical]},
    boxrule=1pt,
    arc=2mm,
    top=2.5mm, bottom=2.5mm, left=3mm, right=3mm,
    #1
}

\newtcolorbox{theorysol}[1][]{
    enhanced,
    breakable,
    colback=LightBg,
    colframe=BorderGray,
    boxrule=0.8pt,
    arc=2mm,
    top=2.5mm, bottom=2.5mm, left=3mm, right=3mm,
    title={\textbf{\color{LPUNavy}Comprehensive Step-by-Step Solution \& Derivation:}},
    #1
}

\newcommand{\mcqitem}[6]{
    \noindent\textbf{Q#1. #2}
    \begin{enumerate}[label=(\alph*),topsep=2pt,itemsep=1pt,partopsep=0pt,parsep=0pt]
        \item #3
        \item #4
        \item #5
        \item #6
    \end{enumerate}
    \vspace{2mm}
}
"""

with open("PHY175_Question_Bank/qb_style.sty", "w") as f:
    f.write(qb_style)

# 2. Master Tex
main_tex = r"""\documentclass[11pt,a4paper,twoside,openright]{report}
\usepackage{qb_style}

\title{\Huge\bfseries\color{LPUNavy} PHY175: Modern Physics \& Electronics\\[0.5em]
\Large\color{LPUOrange} Official Examination Question Bank \& Solution Manual\\[1em]
\normalsize\color{DarkSlate} 360 Categorized Practice MCQs + Complete Answer Keys \& Solutions Manual}
\author{\textbf{LPU Engineering Open Series}}
\date{Academic Year 2026--2027}

\begin{document}
\maketitle

\chapter*{About the Question Bank}
This comprehensive Question Bank covers all 6 units of the \textbf{PHY175: Modern Physics and Electronics} curriculum. Each unit provides:
\begin{itemize}
    \item \textbf{Section 1: 60 Categorized MCQs} directly reflecting official LPU practice exams across Foundational (Easy), Intermediate (Medium), and Advanced (Hard) tiers.
    \item \textbf{Section 2: Complete Answer Key \& Technical Rationales} providing conceptual justifications and numerical working for all 60 MCQs.
    \item \textbf{Section 3: Comprehensive Theory Questions \& Worked Solutions} containing step-by-step derivations and analysis.
\end{itemize}

\tableofcontents

\include{chapters/qb-unit1}
\include{chapters/qb-unit2}
\include{chapters/qb-unit3}
\include{chapters/qb-unit4}
\include{chapters/qb-unit5}
\include{chapters/qb-unit6}

\end{document}
"""

with open("PHY175_Question_Bank/main.tex", "w") as f:
    f.write(main_tex)

# Helper function
def make_clean_unit_file(unit_num, title, mcqs, theory_qs):
    content = f"\\chapter{{Unit {unit_num}: {title}}}\n\n"
    content += "\\section{Section 1: Chapter-Wise Multiple-Choice Questions (60 MCQs)}\n\n"
    
    content += "\\subsection*{Part I: Foundational Level (Questions 1 to 20)}\n"
    for i in range(20):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"
        
    content += "\n\\subsection*{Part II: Intermediate Analytical Level (Questions 21 to 40)}\n"
    for i in range(20, 40):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"
        
    content += "\n\\subsection*{Part III: Advanced Mastery Level (Questions 41 to 60)}\n"
    for i in range(40, 60):
        m = mcqs[i]
        content += f"\\mcqitem{{{i+1}}}{{{m[0]}}}{{{m[1]}}}{{{m[2]}}}{{{m[3]}}}{{{m[4]}}}\n"

    # Multi-page friendly Answer Key
    content += r"""
\newpage
\section{Section 2: Complete Answer Key \& Technical Rationales}

\subsection*{Part A: Questions 1 to 30}
\begin{table}[htbp]
\centering
\caption{\textbf{Answer Key with Rationales (Questions 1 to 30)}}
\vspace{2mm}
\small
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(15):
        q1 = (i+1, mcqs[i][5], mcqs[i][6])
        q2 = (i+16, mcqs[i+15][5], mcqs[i+15][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}

\subsection*{Part B: Questions 31 to 60}
\begin{table}[htbp]
\centering
\caption{\textbf{Answer Key with Rationales (Questions 31 to 60)}}
\vspace{2mm}
\small
\begin{tabularx}{\textwidth}{l c X l c X}
\toprule
\textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} & \textbf{Q\#} & \textbf{Ans} & \textbf{Technical Rationale} \\
\midrule
"""
    for i in range(15):
        q1 = (i+31, mcqs[i+30][5], mcqs[i+30][6])
        q2 = (i+46, mcqs[i+45][5], mcqs[i+45][6])
        content += f"{q1[0]} & \\textbf{{{q1[1]}}} & {q1[2]} & {q2[0]} & \\textbf{{{q2[1]}}} & {q2[2]} \\\\\n"

    content += r"""\bottomrule
\end{tabularx}
\end{table}

\newpage
\section{Section 3: Comprehensive Theory Questions \& Worked Solutions}
"""
    for idx, t in enumerate(theory_qs, 1):
        content += f"\\begin{{theoryq}}{{{unit_num}.{idx}}}\n{t['q']}\n\\end{{theoryq}}\n\n"
        content += f"\\begin{{theorysol}}\n{t['sol']}\n\\end{{theorysol}}\n\n\\vspace{{3mm}}\n\n"

    with open(f"PHY175_Question_Bank/chapters/qb-unit{unit_num}.tex", "w") as f:
        f.write(content)
    print(f"Written clean Unit {unit_num} QB.")

# Import datasets from earlier modules
from build_units_3_to_6_qb import u3_mcqs, u3_theory, u4_mcqs, u4_theory, u5_mcqs, u5_theory, u6_mcqs, u6_theory

# Clean strings helper
def clean_set(mcqs):
    res = []
    for q, a, b, c, d, ans, rat in mcqs:
        def fix(s):
            # Normalize percentage
            s = s.replace(r"\%", "%")
            s = s.replace("%", r"\%")
            # Normalize ampersands
            s = s.replace(r"\&", "&")
            s = s.replace("&", r"\&")
            # Normalize common names
            s = s.replace("INPUT_PULLUP", r"	exttt{INPUT\_PULLUP}")
            s = s.replace("analogWrite(9, 128)", r"	exttt{analogWrite(9, 128)}")
            return s
        res.append((fix(q), fix(a), fix(b), fix(c), fix(d), ans, fix(rat)))
    return res

# Recreate Unit 1
u1_mcqs = [
    ("In the free electron theory of metals, conduction electrons are treated as:", "Positive ions moving through lattice", "Free particles moving through the metal", "Waves confined inside nucleus", "Particles fixed to individual atoms", "B", "Drude theory treats valence electrons as a free classical gas."),
    ("Which particles mainly carry electric current in a metal according to free electron theory?", "Bound protons", "Lattice neutrons", "Positive nuclei", "Conduction electrons", "D", "Delocalized conduction electrons are the charge carriers in metals."),
    ("Drift current in a semiconductor is produced mainly by:", "A constant magnetic field", "A carrier concentration gradient", "A uniform temperature alone", "An applied electric field", "D", "Drift is carrier motion driven by an applied electric field."),
    ("Diffusion current occurs when charge carriers move from a region of:", "Low concentration to high concentration", "High concentration to low concentration", "Low potential to high potential only", "Low temperature to high temperature only", "B", "Diffusion is driven from higher to lower carrier concentration gradient."),
    ("At absolute zero ($0\\,\\text{K}$), the Fermi energy is the energy of the:", "Highest empty electron state", "Lowest forbidden energy state", "Lowest occupied electron state", "Highest occupied electron state", "D", "At $0\\,\\text{K}$, $E_F$ is the cutoff energy of highest occupied state."),
    ("The Fermi-Dirac distribution function gives the probability that an energy state is:", "Converted into lattice energy", "Occupied by a proton", "Located in a forbidden band", "Occupied by an electron", "D", "Fermi-Dirac $f(E)$ gives electronic state occupancy probability."),
    ("At the Fermi energy $E = E_F$, the Fermi-Dirac occupation probability is:", "$1$", "$0$", "$1/4$", "$1/2$", "D", "At $E = E_F$, $f(E_F) = 1/(1+e^0) = 1/2 = 50\\%$ at any $T > 0\\,\\text{K}$."),
    ("A range of electron energies that cannot exist in a solid is called a:", "Forbidden energy band", "Valence energy band", "Permitted energy level", "Conduction energy band", "A", "The energy gap $E_g$ contains no allowed electronic wave states."),
    ("The highest energy band normally occupied by electrons at $0\\,\\text{K}$ in a semiconductor is the:", "Conduction band", "Valence band", "Vacuum band", "Forbidden band", "B", "At $0\\,\\text{K}$, the valence band is completely full and conduction band is empty."),
    ("A hole in a semiconductor behaves like a particle with:", "Negative charge", "Zero charge", "Variable charge", "Positive charge", "D", "Absence of an electron behaves as an effective positive charge $+e$."),
    ("Effective mass is used to describe how a charge carrier responds to:", "Nuclear force inside an atom", "An external force in a crystal", "Pressure in a vacuum", "Gravity outside the material", "B", "Effective mass accounts for crystal lattice periodic potential response."),
    ("The Hall effect is the development of a transverse voltage when a current-carrying material is placed in a:", "Longitudinal thermal field", "Uniform gravitational field", "Parallel electric field", "Perpendicular magnetic field", "D", "Transverse Lorentz force from perpendicular $\\vec{B}$ field produces $V_H$."),
    ("For a material with one type of carrier having concentration $n$ and charge $q$, the Hall coefficient is:", "$R_H = q/n$", "$R_H = 1/(nq)$", "$R_H = n/q$", "$R_H = nq$", "B", "By definition, $R_H = E_y / (J_x B_z) = 1/(nq)$."),
    ("A pure semiconductor without intentionally added impurities is called:", "A metallic conductor", "An extrinsic semiconductor", "An ionic insulator", "An intrinsic semiconductor", "D", "Undoped pure semiconductor material is intrinsic."),
    ("Adding a pentavalent impurity to silicon usually produces:", "An intrinsic semiconductor", "An n-type semiconductor", "A perfect insulator", "An p-type semiconductor", "B", "Pentavalent atoms donate extra electrons, forming n-type."),
    ("In an intrinsic semiconductor, the Fermi level lies approximately:", "At the bottom of the valence band", "Near the middle of the band gap", "Far above the conduction band", "At the top of the conduction band", "B", "Equal electron and hole densities position $E_i$ near midgap."),
    ("In an n-type semiconductor, the Fermi level shifts closer to the:", "Conduction band", "Bottom of the forbidden band", "Middle of the nucleus", "Valence band", "A", "Donor electrons populate near $E_C$, shifting $E_F$ upwards."),
    ("In a direct band gap semiconductor, an electron can recombine with a hole without requiring a change in:", "Electric charge", "Carrier number", "Crystal momentum", "Electron energy", "C", "Extrema align at $\\vec{k}=0$, conserving momentum without phonons."),
    ("Which material is commonly classified as an indirect band gap semiconductor?", "Gallium nitride", "Gallium arsenide", "Silicon", "Indium phosphide", "C", "Silicon and Germanium have indirect band gaps."),
    ("A solar cell converts light energy directly into electrical energy through the:", "Piezoelectric effect", "Photovoltaic effect", "Thermoelectric effect", "Hall effect", "B", "Photons create electron-hole pairs separated by p-n junction field."),
    ("In the Drude model, $\\sigma = \\frac{ne^2\\tau}{m}$. If electron density doubles while mean collision time halves, conductivity:", "Becomes half as large", "Becomes twice as large", "Remains unchanged", "Becomes four times as large", "C", "$\\sigma \\propto n \\tau \\implies (2)(1/2) = 1$."),
    ("Electron concentration increases along $+x$. Which electric-field direction balances electron diffusion current?", "Along the positive $x$-direction", "No electric field is required", "Perpendicular to $x$-direction", "Along the negative $x$-direction", "A", "Diffusion drives electrons toward $-x$. Electric field along $+x$ exerts force in $-x$ to create opposing drift."),
    ("For 3D free electron gas at $0\\,\\text{K}$, $E_F \\propto n^{2/3}$. If density increases 8 times, new Fermi energy is:", "$4 E_F$", "$8 E_F$", "$16 E_F$", "$2 E_F$", "A", "$E_F' = (8)^{2/3} E_F = 4 E_F$."),
    ("Probability that an electronic state at Fermi energy $E_F$ is occupied at nonzero temperature is:", "$1$", "$0$", "$1/e$", "$1/2$", "D", "$f(E_F) = 1/(1+e^0) = 1/2$ at all $T > 0$."),
    ("At temperature $T$, a state has $E - E_F = k_B T \\ln 3$. What is its Fermi-Dirac occupation probability?", "$1/2$", "$3/4$", "$1/3$", "$1/4$", "D", "$f(E) = 1/(1 + e^{\\ln 3}) = 1/(1+3) = 1/4$."),
    ("When $N$ identical isolated atoms form a crystal, one atomic energy level splits into:", "Exactly two levels", "About $N$ closely spaced levels", "A single level", "A forbidden gap", "B", "Wavefunction overlap splits $N$ degenerate states into an energy band of $N$ levels."),
    ("Why does a completely filled energy band produce no net electrical current under weak field?", "Contains only positive carriers", "Electrons have no kinetic energy", "All enter conduction band", "Contributions from occupied states cancel across the band", "D", "For every electron in state $+k$, there is an electron in $-k$, summing velocity to zero."),
    ("Near the top of valence band, $d^2E/dk^2 < 0$. What is the standard description of transport?", "Negative holes, negative mass", "Neutral carriers, zero mass", "Free electrons, infinite mass", "Positive holes with positive effective mass", "D", "Negative electron curvature is mapped to holes with $q = +e$ and $m_h^* > 0$."),
    ("An electron occupies a band region where $m^* < 0$. If an external force acts along $+x$, its acceleration is:", "Always zero", "Along $+x$", "Along $-x$", "Perpendicular to $+x$", "C", "$a = F/m^*$; with $m^* < 0$, acceleration is opposite to applied force."),
    ("Current is along $+x$, magnetic field along $+z$. If electrons are majority carriers, where do they accumulate?", "On the negative $y$ side", "On the positive $y$ side", "On the negative $z$ side", "On the positive $x$ side", "A", "$\\vec{F} = -e(\\vec{v}_d \\times \\vec{B}) = -e((-v_d\\hat{x}) \\times B\\hat{z}) = -e(v_d B \\hat{y}) = -e v_d B \\hat{y}$ toward $-y$."),
    ("A semiconductor slab has $n = 5.0 \\times 10^{22}\\,\\text{m}^{-3}, t = 0.50\\,\\text{mm}, I = 2.0\\,\\text{mA}, B = 0.50\\,\\text{T}$. Magnitude of Hall voltage $V_H$ is:", "$0.50\\,\\text{mV}$", "$0.25\\,\\text{mV}$", "$2.50\\,\\text{mV}$", "$1.00\\,\\text{mV}$", "B", "$V_H = \\frac{IB}{net} = \\frac{(2\\times 10^{-3})(0.5)}{(5\\times 10^{22})(1.6\\times 10^{-19})(0.5\\times 10^{-3})} = 0.25\\,\\text{mV}$."),
    ("Hall coefficient is $R_H = -3.9 \\times 10^{-4}\\,\\text{m}^3/\\text{C}$. The carrier type and approximate concentration are:", "Holes, $1.6 \\times 10^{22}\\,\\text{m}^{-3}$", "Electrons, $3.9 \\times 10^{22}\\,\\text{m}^{-3}$", "Holes, $3.9 \\times 10^{22}\\,\\text{m}^{-3}$", "Electrons, $1.6 \\times 10^{22}\\,\\text{m}^{-3}$", "D", "Negative sign $\\implies$ electrons; $n = 1/(|R_H|e) = 1.6\\times 10^{22}\\,\\text{m}^{-3}$."),
    ("In intrinsic semiconductor $n=p=n_i$. If $\\mu_e = 3\\mu_h$, what fraction of conductivity is due to electrons?", "$1/2$", "$1/4$", "$3/4$", "$2/3$", "C", "$\\sigma_e / \\sigma_{total} = \\mu_e / (\\mu_e + \\mu_h) = 3/(3+1) = 3/4$."),
    ("Silicon is doped with phosphorus. After donor ionization, which carriers and fixed ions are produced?", "Free electrons and positive donor ions", "Free holes and negative donor ions", "Free electrons and negative donor ions", "Free holes and positive donor ions", "A", "Donating an electron leaves fixed positive donor ion $N_D^+$ and free conduction electron."),
    ("Why does conductivity of intrinsic semiconductor increase strongly with temperature?", "More electrons cross bandgap creating pairs", "Forbidden gap fills completely", "Valence electrons per atom increases", "Crystal becomes metal", "A", "Thermal excitation across $E_g$ causes exponential carrier generation $n_i \\propto e^{-E_g/2k_BT}$."),
    ("For intrinsic semiconductor, $E_i = \\frac{E_C+E_V}{2} + \\frac{k_BT}{2}\\ln(N_V/N_C)$. If $N_C > N_V$, $E_i$ is:", "Slightly below the middle of the band gap", "Slightly above the middle of the band gap", "At conduction-band edge", "At valence-band edge", "A", "$\\ln(N_V/N_C) < 0$ when $N_C > N_V$, pulling $E_i$ below midgap."),
    ("At $300\\,\\text{K}$, electron concentration in n-type Si increases by $100\\times$. How far does $E_F$ shift towards $E_C$? ($k_BT = 0.0259\\,\\text{eV}$)", "$0.119\\,\\text{eV}$", "$0.059\\,\\text{eV}$", "$0.460\\,\\text{eV}$", "$0.259\\,\\text{eV}$", "A", "$\\Delta E_F = k_BT \\ln(100) = 0.0259 \\times 4.605 = 0.119\\,\\text{eV}$."),
    ("Why is direct band-gap semiconductor more efficient for light emission than indirect gap?", "Recombination requires 2 phonons", "Electron-hole recombination conserves momentum without a phonon", "Valence band has larger resistance", "No available conduction states", "B", "Direct transition is a 1st-order process requiring no phonon lattice interaction."),
    ("In illuminated solar cell under short circuit, primary role of depletion field is to:", "Make carriers move to same contact", "Prevent light entering", "Separate photogenerated electrons and holes", "Create sub-bandgap photons", "C", "Built-in electric field sweeps electrons to n-side and holes to p-side."),
    ("Solar cell receives $100\\,\\text{mW}$ of $2.0\\,\\text{eV}$ light. If $80\\%$ photons create collected electrons, photocurrent is:", "$40\\,\\text{mA}$", "$80\\,\\text{mA}$", "$64\\,\\text{mA}$", "$20\\,\\text{mA}$", "A", "Photon rate $= 3.125\\times 10^{17}\\,\\text{s}^{-1} \\implies I = 0.8\\times 1.6\\times 10^{-19}\\times 3.125\\times 10^{17} = 40\\,\\text{mA}$."),
    ("Metal B has $2\\times$ electron density and $3\\times$ effective mass of metal A. If $\\sigma_A = \\sigma_B$, relationship between collision times is:", "$\\tau_B = 6\\tau_A$", "$\\tau_B = \\frac{1}{6}\\tau_A$", "$\\tau_B = \\frac{3}{2}\\tau_A$", "$\\tau_B = \\frac{2}{3}\\tau_A$", "C", "$\\sigma = \\frac{n e^2 \\tau}{m} \\implies \\frac{2 n_A e^2 \\tau_B}{3 m_A} = \\frac{n_A e^2 \\tau_A}{m_A} \\implies \\tau_B = \\frac{3}{2}\\tau_A$."),
    ("In nondegenerate semiconductor, $n(x) = n_0 e^{x/L}$. Which electric field makes total electron current density zero?", "$E_x = \\frac{kT}{qL}$", "$E_x = \\frac{qL}{kT}$", "$E_x = -\\frac{kT}{qL}$", "$E_x = -\\frac{qL}{kT}$", "C", "$J_n = q n \\mu_n E_x + q D_n \\frac{dn}{dx} = 0 \\implies E_x = -\\frac{kT}{qL}$."),
    ("Excess minority electrons in p-type Si: $\\Delta n(x) = \\Delta n_0 e^{-x/L_n}$ for $x>0$. With no $E$-field, directions of electron motion and diffusion current are:", "Electrons move $-x$, current $+x$", "Electrons and current both $-x$", "Electrons and current both $+x$", "Electrons move $+x$, current $-x$", "D", "Electrons diffuse down gradient along $+x$. Conventional current is along $-x$."),
    ("Two 3D free electron systems at $T=0$: System B has $n_B = 8n_A$ and $m_B^* = 2m_A^*$. What is $E_{F,B}/E_{F,A}$?", "$2$", "$8$", "$1/2$", "$4$", "A", "$E_F \\propto \\frac{n^{2/3}}{m^*} \\implies \\frac{(8)^{2/3}}{2} = \\frac{4}{2} = 2$."),
    ("At temp $T$, state 1 is at $E_F + k_BT\\ln 3$ and state 2 is at $E_F - k_BT\\ln 3$. Probabilities that state 1 is occupied and state 2 is empty are:", "Both $3/4$", "$3/4$ and $1/4$", "Both $1/4$", "$1/4$ and $3/4$", "C", "$f(E_F+\\Delta) = \\frac{1}{1+e^{\\ln 3}} = \\frac{1}{4}$. Empty prob at $E_F-\\Delta$ is $1-f(E_F-\\Delta) = f(E_F+\\Delta) = 1/4$."),
    ("A narrow group of states has constant DOS symmetric about chemical potential $\\mu$. Integration limits $\\gg k_BT$. Thermal excitation satisfies:", "Electrons above $\\mu >$ holes below $\\mu$", "Holes below $\\mu >$ electrons above $\\mu$", "Equality only at $T=0$", "Number of electrons excited above $\\mu$ equals number of holes below $\\mu$", "D", "By particle conservation and Fermi-Dirac anti-symmetry about $\\mu$."),
    ("Crystal has $N$ atoms, each contributing 1 electron from nondegenerate orbital. Assuming spin degeneracy, band theory predicts:", "Contains $N/2$ states, half filled", "Contains $2N$ states, half filled", "Contains $2N$ states, completely filled", "Contains $N$ states, completely filled", "B", "With 2 spin states per orbital, band holds $2N$ electrons. $N$ electrons fill half the band (metal)."),
    ("In nearly-free electron model, why does energy gap open at Brillouin-zone boundary?", "Pauli principle shifts states", "Periodic potential couples degenerate forward and backward waves splitting standing wave energies", "Lattice confines electron permanently", "Collisions remove states", "B", "Bragg reflection forms standing waves with different electrostatic potential energies."),
    ("2D band dispersion: $E(k_x, k_y) = E_0 - \\alpha k_x^2 + \\beta k_y^2$ with $\\alpha, \\beta > 0$. Signs of electron effective-mass components are:", "$m_x^* > 0, m_y^* < 0$", "$m_x^* < 0, m_y^* > 0$", "$m_x^* > 0, m_y^* > 0$", "$m_x^* < 0, m_y^* < 0$", "B", "$m_x^* = \\hbar^2/(-2\\alpha) < 0$ and $m_y^* = \\hbar^2/(+2\\beta) > 0$."),
    ("Nearly full valence band has negative electron curvature near max. Why is it represented by holes with positive effective mass?", "Hole carries negative charge", "Removing electron reverses both charge and current contribution", "Removing electron changes curvature", "Hole is a proton", "B", "Absence of negative charge electron moving with negative acceleration behaves identically to positive charge with positive mass."),
    ("Rectangular n-type sample carries current $I$ along $+x$ in $B$ field along $+z$, thickness $t$. Hall voltage $V_H = V(+y) - V(-y)$ is:", "$V_H = \\frac{IB}{net}$", "$V_H = \\frac{I}{neBt}$", "$V_H = -\\frac{IBt}{ne}$", "$V_H = -\\frac{IB}{net}$", "D", "Electrons accumulate at $-y$, so $V(-y) > V(+y)$, giving negative Hall voltage $V_H = -\\frac{IB}{net}$."),
    ("Weak-field Hall coefficient for electrons and holes is $R_H = \\frac{p\\mu_h^2 - n\\mu_e^2}{q(p\\mu_h + n\\mu_e)^2}$. Hall voltage vanishes when:", "$p\\mu_e^2 = n\\mu_h^2$", "$p\\mu_h = n\\mu_e$", "$p\\mu_h^2 = n\\mu_e^2$", "$p\\mu_e = n\\mu_h$", "C", "$V_H = 0 \\iff R_H = 0 \\implies p\\mu_h^2 = n\\mu_e^2$."),
    ("Compensated semiconductor has $N_D - N_A = 2 n_i$. Assuming thermal equilibrium, electron concentration $n$ is:", "$n = 2 n_i$", "$n = (1+\\sqrt{2})n_i$", "$n = (\\sqrt{2}-1)n_i$", "$n = \\sqrt{2} n_i$", "B", "$n - n_i^2/n = 2n_i \\implies n = (1+\\sqrt{2})n_i$."),
    ("Two intrinsic materials have same $E_g, T$. Material B has $N_{C,B} = 4N_{C,A}$ and $N_{V,B} = N_{V,A}/4$. How does $n_{i,B}$ compare to $n_{i,A}$?", "$n_{i,B} = n_{i,A}$", "$n_{i,B} = \\frac{1}{2}n_{i,A}$", "$n_{i,B} = 4n_{i,A}$", "$n_{i,B} = 2n_{i,A}$", "A", "$N_{C,B} N_{V,B} = N_{C,A} N_{V,A} \\implies n_{i,B} = n_{i,A}$."),
    ("Intrinsic semiconductor has $m_h^* = 4 m_e^*$. Relative to midgap, where is $E_i$?", "Exactly at midgap", "$\\frac{1}{2}k_BT\\ln 4$ above midgap", "$\\frac{3}{4}k_BT\\ln 4$ below midgap", "$\\frac{3}{4}k_BT\\ln 4$ above midgap", "D", "$E_i - E_{mid} = \\frac{3}{4}k_BT\\ln(m_h^*/m_e^*) = \\frac{3}{4}k_BT\\ln 4$ above midgap."),
    ("Fully ionized n-type semiconductor ($N_D \\gg n_i$). If $N_D$ increases by $100\\times$, how does $E_F - E_i$ change?", "Increases by $2k_BT\\ln 100$", "Remains unchanged", "Increases by $k_BT\\ln 100$", "Decreases by $k_BT\\ln 100$", "C", "$E_F - E_i = k_BT\\ln(N_D/n_i) \\implies$ increases by $k_BT\\ln 100$."),
    ("Two semiconductors have equal $E_g$, one direct, one indirect. Why direct emits light more efficiently?", "Equal numbers of states", "Conduction electrons have no effective mass", "Photons supply large momentum", "Band-edge electron-hole recombination conserves crystal momentum without a phonon", "D", "Direct transitions conserve $\\vec{k}$ directly without 2nd-order phonon scattering."),
    ("Indirect gap has VB max at $k=0$ and CB min at $k=k_0 \\neq 0$. Near-threshold optical absorption requires:", "Two photons absorbed", "Photon alone provides momentum $\\hbar k_0$", "Photon and phonon jointly conserve energy and crystal momentum", "Impurity converts gap", "C", "Photon provides energy $\\hbar\\omega \\approx E_g$; phonon supplies crystal momentum $\\hbar k_0$."),
    ("For ideal solar cell with ideality factor 1, $V_{oc} \\approx (kT/q)\\ln(I_{sc}/I_0)$. At $300\\,\\text{K}$, by how much does $V_{oc}$ increase when intensity rises $100\\times$?", "$0.238\\,\\text{V}$", "$0.0259\\,\\text{V}$", "$0.119\\,\\text{V}$", "$0.0595\\,\\text{V}$", "C", "$\\Delta V_{oc} = (0.0259\\,\\text{V})\\ln(100) \\approx 0.119\\,\\text{V}$."),
    ("Solar cell has $V_{oc} = 0.65\\,\\text{V}, I_{sc} = 40\\,\\text{mA}, V_m = 0.52\\,\\text{V}, I_m = 35\\,\\text{mA}$. What is its fill factor?", "$0.70$", "$0.58$", "$0.91$", "$0.80$", "A", "$FF = \\frac{0.52 \\times 35}{0.65 \\times 40} = 0.70$.")
]

u1_theory = [
    {"q": "State the fundamental assumptions of classical Drude free electron theory and derive $\\sigma = \\frac{ne^2\\tau}{m}$.", "sol": "Drude model treats valence electrons as a non-interacting classical gas colliding with fixed lattice ions with collision interval $\\tau$. Under field $E$, steady state drift velocity is $v_d = -e\\tau E/m$, giving current density $J = ne^2\\tau E/m = \\sigma E$, yielding conductivity $\\sigma = \\frac{ne^2\\tau}{m}$."},
    {"q": "Derive the mathematical expression for Hall voltage $V_H$ and explain how it determines carrier type.", "sol": "Under magnetic field $B\\hat{z}$ and current $I\\hat{x}$, Lorentz force drives carriers to $-y$ until electric Hall field $E_H$ balances magnetic force: $q E_H = q v_d B \\implies E_H = v_d B$. With $v_d = \\frac{I}{nqwt}$, Hall voltage is $V_H = E_H w = \\frac{IB}{nqt}$. Sign of $V_H$ indicates carrier polarity."}
]

# Recreate Unit 2
u2_mcqs = [
    ("According to Ohm's law, what is voltage across $5\\,\\Omega$ resistor carrying $2\\,\\text{A}$?", "$7\\,\\text{V}$", "$2.5\\,\\text{V}$", "$10\\,\\text{V}$", "$15\\,\\text{V}$", "C", "$V = IR = 10\\,\\text{V}$."),
    ("Which law states algebraic sum of currents at a junction is zero?", "Kirchhoff's current law", "Coulomb's law", "Ohm's law", "Kirchhoff's voltage law", "A", "KCL states charge conservation at a node."),
    ("Two equal resistors in series across $12\\,\\text{V}$. Voltage across each:", "$6\\,\\text{V}$", "$3\\,\\text{V}$", "$24\\,\\text{V}$", "$12\\,\\text{V}$", "A", "$12/2 = 6\\,\\text{V}$."),
    ("In a series voltage divider, which resistor gets larger voltage drop?", "Grounded resistor", "Smaller resistor", "First resistor", "Larger resistor", "D", "$V \\propto R$."),
    ("Total current $4\\,\\text{A}$ enters two equal parallel resistors. Current in each:", "$1\\,\\text{A}$", "$2\\,\\text{A}$", "$4\\,\\text{A}$", "$8\\,\\text{A}$", "B", "$4/2 = 2\\,\\text{A}$."),
    ("In which bias does PN diode conduct significant current?", "Breakdown", "Zero", "Reverse", "Forward", "D", "Forward bias lowers potential barrier."),
    ("Depletion region of PN diode under forward bias:", "Narrower", "Wider", "Unchanged", "Conductive metal", "A", "Forward bias reduces depletion width."),
    ("Primary function of diode rectifier:", "Convert DC to AC", "Increase frequency", "Store charge", "Convert AC to DC", "D", "Converts AC to pulsating DC."),
    ("Ideal forward-biased diode behaves as:", "Closed switch", "Capacitor", "Open switch", "Current source", "A", "Ideal forward diode has $0\\,\\Omega$ resistance."),
    ("Three terminals of BJT:", "Emitter, base, collector", "Gate, source, drain", "Input, output, ground", "Anode, cathode, gate", "A", "Emitter, Base, Collector."),
    ("Which small BJT current controls larger collector current?", "Leakage", "Emitter", "Reverse", "Base current", "D", "$I_C = \\beta I_B$."),
    ("Two types of MOS transistors combined in CMOS:", "LED and diode", "JFET and BJT", "NMOS and PMOS", "NPN and PNP", "C", "Complementary NMOS and PMOS."),
    ("Major advantage of CMOS circuits:", "Low static power use", "Large size", "Acoustic output", "Mechanical strength", "A", "Near-zero static standby power."),
    ("Which statement describes RAM?", "Usually volatile", "Read-only", "Stores optically", "Uses tape", "A", "Volatile working memory."),
    ("Semiconductor memory used in SSD:", "Dynamic RAM", "Register", "Flash memory", "Cache", "C", "Non-volatile NAND flash."),
    ("Main purpose of AI accelerator chip:", "Route packets", "Speed up AI computations", "Convert sound", "Measure temperature", "B", "Parallel matrix multiplication."),
    ("Basic role of sensor in IoT:", "Compile software", "Encrypt packet", "Increase voltage", "Detect a physical quantity", "D", "Converts physical parameter to electrical signal."),
    ("What is a computer network?", "Storage chip", "Power supply", "Group of connected devices", "Single processing unit", "C", "Connected computing nodes."),
    ("Physical phenomenon confining light in optical fiber:", "Induction", "Resonance", "Photoelectric", "Total internal reflection", "D", "Total internal reflection at core-cladding boundary."),
    ("Processor suited for many parallel calculations:", "SSD controller", "Router", "GPU", "CPU", "C", "GPU thousands of parallel cores."),
    ("Source $12\\,\\text{V}$ connected to series $2\\,\\Omega$ and $4\\,\\Omega$. Circuit current:", "$6\\,\\text{A}$", "$2\\,\\text{A}$", "$1\\,\\text{A}$", "$3\\,\\text{A}$", "B", "$12 / 6 = 2\\,\\text{A}$."),
    ("Currents $5\\,\\text{A}, 2\\,\\text{A}$ enter node; $4\\,\\text{A}, I$ leave. Value of $I$:", "$3\\,\\text{A}$", "$2\\,\\text{A}$", "$1\\,\\text{A}$", "$7\\,\\text{A}$", "A", "$5+2 = 4+I \\implies I = 3\\,\\text{A}$."),
    ("Supply $20\\,\\text{V}$ across series $3\\,\\text{k}\\Omega, 7\\,\\text{k}\\Omega$. Voltage across $7\\,\\text{k}\\Omega$:", "$14\\,\\text{V}$", "$17\\,\\text{V}$", "$10\\,\\text{V}$", "$6\\,\\text{V}$", "A", "$20 \\times 7/10 = 14\\,\\text{V}$."),
    ("Divider $R_1=2\\,\\text{k}\\Omega, R_2=8\\,\\text{k}\\Omega$. Parallel load on $R_2$ main effect:", "Source zero", "Output increases", "Current zero", "Output voltage decreases", "D", "Parallel resistance drops, reducing voltage drop."),
    ("Total current $6\\,\\text{A}$ into parallel $3\\,\\Omega, 6\\,\\Omega$. Current in $3\\,\\Omega$:", "$1\\,\\text{A}$", "$4\\,\\text{A}$", "$2\\,\\text{A}$", "$6\\,\\text{A}$", "B", "$6 \\times 6/9 = 4\\,\\text{A}$."),
    ("Parallel branches $4\\,\\Omega, 12\\,\\Omega$. Current in $4\\,\\Omega$ is $9\\,\\text{A}$. Current in $12\\,\\Omega$:", "$1\\,\\text{A}$", "$3\\,\\text{A}$", "$27\\,\\text{A}$", "$9\\,\\text{A}$", "B", "$V = 36\\,\\text{V} \\implies I = 36/12 = 3\\,\\text{A}$."),
    ("Depletion region when silicon diode is forward biased:", "Resistance infinite", "Polarity reverses", "Width decreases", "Width increases", "C", "Depletion layer narrows."),
    ("Silicon diode anode $0.8\\,\\text{V}$, cathode $0.2\\,\\text{V}$ ($V_D=0.7\\,\\text{V}$). Behavior:", "Acts as open circuit", "Reverse biased", "Conducts significantly", "Breakdown", "A", "$V_{applied} = 0.6\\,\\text{V} < 0.7\\,\\text{V}$ threshold."),
    ("Full-wave bridge rectifier with $50\\,\\text{Hz}$ AC. Output ripple frequency:", "$25\\,\\text{Hz}$", "$100\\,\\text{Hz}$", "$200\\,\\text{Hz}$", "$50\\,\\text{Hz}$", "B", "$2 \\times 50 = 100\\,\\text{Hz}$."),
    ("Ideal forward-biased diode in diode switch represents:", "Amplifier", "Open circuit", "Current source", "Short circuit", "D", "Closed short circuit switch."),
    ("BJT active region: $I_C = 2\\,\\text{mA}, I_B = 20\\,\\mu\\text{A}$. Current gain $\\beta$:", "$50$", "$10$", "$100$", "$200$", "C", "$\\beta = 2000/20 = 100$."),
    ("BJT saturation condition:", "Both reverse", "Both forward", "Emitter forward, collector reverse", "Emitter reverse, collector forward", "B", "Both EBJ and CBJ forward biased."),
    ("CMOS inverter with input LOW:", "Both OFF", "PMOS ON, output HIGH", "Both ON", "NMOS ON", "B", "PMOS pulls output to $V_{DD}$."),
    ("Why CMOS consumes very little static power:", "Breakdown", "Grounded", "Supply path nonconducting in steady states", "No transistors", "C", "One transistor always OFF in steady state."),
    ("Computer temporary working storage during execution:", "ROM", "SSD", "Dynamic RAM", "Optical fiber", "C", "DRAM working memory."),
    ("Why SSD is more shock-resistant than HDD:", "Uses no moving mechanical parts", "Loses data without power", "Stores in magnetic domains", "Rotating platter", "A", "Solid-state silicon components."),
    ("Why GPUs/AI accelerators effective for neural networks:", "Sequential instructions", "Perform many similar operations in parallel", "Hardware replacement", "Eliminate memory", "B", "Massively parallel SIMD processing."),
    ("IoT node sends data only when $\\Delta T > 2^\\circ\\text{C}$. Benefit:", "No calibration", "Zero error", "Reduced energy and communication use", "Higher noise", "C", "Conserves battery power."),
    ("Deliver data to every host on local subnet:", "Broadcast", "Loopback", "Point-to-point", "Unicast", "A", "Subnet broadcast."),
    ("Property allowing fiber signal propagation with low loss:", "Total internal reflection", "Induction", "Capacitive coupling", "Thermal expansion", "A", "Total internal reflection in glass core."),
    ("Node $V$ connected to $10\\,\\text{V}$ through $2\\,\\Omega$, GND through $4\\,\\Omega$, $2\\,\\text{A}$ injected into node:", "$V=8\\,\\text{V}, I=1\\,\\text{A}$", "$V=28/3\\,\\text{V}, I=1/3\\,\\text{A}$", "$V=20/3\\,\\text{V}, I=5/3\\,\\text{A}$", "$V=12\\,\\text{V}, I=-1\\,\\text{A}$", "B", "KCL gives $V = 28/3\\,\\text{V}, I = 1/3\\,\\text{A}$."),
    ("Source $24\\,\\text{V}, R_1=6\\,\\text{k}\\Omega, R_2=3\\,\\text{k}\\Omega$. Parallel $R_L$ giving $V_{out}=6\\,\\text{V}$:", "$R_L = 4\\,\\text{k}\\Omega$", "$R_L = 6\\,\\text{k}\\Omega$", "$R_L = 12\\,\\text{k}\\Omega$", "$R_L = 3\\,\\text{k}\\Omega$", "B", "$R_p = 2\\,\\text{k}\\Omega \\implies R_L = 6\\,\\text{k}\\Omega$."),
    ("Source $12\\,\\text{A}$ into $2, 3, 6\\,\\Omega$. $6\\,\\Omega$ removed. Increase in $2\\,\\Omega$ current:", "$2.4\\,\\text{A}$", "$0.8\\,\\text{A}$", "$2.0\\,\\text{A}$", "$1.2\\,\\text{A}$", "D", "$I_2$ rises from $6.0\\,\\text{A}$ to $7.2\\,\\text{A} \\implies 1.2\\,\\text{A}$."),
    ("Diode $I \\propto I_S e^{V_D/2V_T}$. Ratio $I(330\\,\\text{K})/I(300\\,\\text{K})$ at $0.6\\,\\text{V}$:", "$1.39$", "$8.00$", "$2.79$", "$5.57$", "C", "Combined $I_S$ and thermal voltage exponential gives $\\approx 2.79$."),
    ("Diode $V_D = 0.70 + 10 I_D$ with $430\\,\\Omega$ across $5.0\\,\\text{V}$. Operating point:", "$I_D=9.77\\,\\text{mA}, V_D=0.798\\,\\text{V}$", "$I_D=11.36\\,\\text{mA}, V_D=0.814\\,\\text{V}$", "$I_D=10.00\\,\\text{mA}, V_D=0.800\\,\\text{V}$", "$I_D=9.30\\,\\text{mA}, V_D=0.793\\,\\text{V}$", "A", "$I_D = 4.30/440 = 9.77\\,\\text{mA}, V_D = 0.798\\,\\text{V}$."),
    ("Bridge rectifier $15\\,\\text{V}$ peak, $50\\,\\text{Hz}, 1000\\,\\mu\\text{F}, 1\\,\\text{k}\\Omega$. $V_{DC}$ and ripple:", "$V_{DC}=13.53\\,\\text{V}, V_r=0.271\\,\\text{V}$", "$V_{DC}=13.46\\,\\text{V}, V_r=0.269\\,\\text{V}$", "$V_{DC}=13.53\\,\\text{V}, V_r=0.135\\,\\text{V}$", "$V_{DC}=14.23\\,\\text{V}, V_r=0.142\\,\\text{V}$", "B", "$V_{DC} = 13.46\\,\\text{V}, V_{r(pp)} = 0.269\\,\\text{V}$."),
    ("Diode logic: $5\\,\\text{V}$ pull-up to $Y$, diodes from $Y$ to inputs $A, B$. Function implemented:", "NAND", "OR", "AND function, low input clamping $Y$ near $0.7\\,\\text{V}$", "NOR", "C", "Diode AND logic gate."),
    ("NPN switch for $120\\,\\Omega, 12\\,\\text{V}$ relay ($V_{CE}=0.2\\,\\text{V}, V_{BE}=0.8\\,\\text{V}$, driver $3.3\\,\\text{V}, \\beta_{forced}=10$). Base resistor:", "$330\\,\\Omega$", "$220\\,\\Omega$", "$270\\,\\Omega$", "$250\\,\\Omega$", "D", "$R_B = 2.5 / 0.009833 \\approx 254\\,\\Omega \\implies 250\\,\\Omega$."),
    ("Bias: $V_{TH}=2.0\\,\\text{V}, R_{TH}=20\\,\\text{k}\\Omega, \\beta=99, V_{BE}=0.7\\,\\text{V}, R_E=1\\,\\text{k}\\Omega$. $I_C$:", "$0.87\\,\\text{mA}$", "$1.07\\,\\text{mA}$", "$1.50\\,\\text{mA}$", "$1.29\\,\\text{mA}$", "B", "$I_C = 99 \\times \\frac{1.30}{120} = 1.07\\,\\text{mA}$."),
    ("CMOS $C=20\\,\\text{pF}, \\alpha=0.25$. Initial $1.2\\,\\text{V}, 500\\,\\text{MHz} \\to 1.0\\,\\text{V}, 400\\,\\text{MHz}$. New power and percent:", "$2.9\\,\\text{mW}, 80.0\\%$", "$2.0\\,\\text{mW}, 55.6\\%$", "$2.5\\,\\text{mW}, 69.4\\%$", "$2.4\\,\\text{mW}, 66.7\\%$", "B", "$P_{orig} = 3.6\\,\\text{mW}, P_{new} = 2.0\\,\\text{mW} \\implies 55.6\\%$."),
    ("CMOS NAND gate with $A=0, B=1$. Description:", "$A$-pMOS, $B$-nMOS ON, LOW", "$A$-pMOS, $B$-nMOS ON, output HIGH", "$B$-pMOS, $A$-nMOS ON, HIGH", "Both pMOS OFF", "B", "$A$-pMOS pulls output HIGH."),
    ("Memory 64-bit word SECDED Hamming. Minimum stored bits:", "$72$ bits", "$70$ bits", "$73$ bits", "$71$ bits", "A", "$64 + 7 + 1 = 72$ bits."),
    ("SSD $1.2\\,\\text{TB}$ NAND, $3000$ cycles, write amp $2.5$. Host bytes:", "$3.00\\,\\text{PB}$", "$3.60\\,\\text{PB}$", "$1.20\\,\\text{PB}$", "$1.44\\,\\text{PB}$", "D", "$1.2 \\times 3000 / 2.5 = 1.44\\,\\text{PB}$."),
    ("Accelerator Peak $100\\,\\text{TOPS}$, Bandwidth $800\\,\\text{GB/s}$. Bounds at intensities $60, 150\\,\\text{ops/byte}$:", "$60, 100\\,\\text{TOPS}$", "$48, 100\\,\\text{TOPS}$", "$100, 100\\,\\text{TOPS}$", "$80, 120\\,\\text{TOPS}$", "B", "$48\\,\\text{TOPS}$ and $100\\,\\text{TOPS}$."),
    ("Accelerator dot product $1024$ pairs of signed 8-bit integers. Minimum accumulator width:", "$27$ bits", "$25$ bits", "$26$ bits", "$24$ bits", "A", "$25-27$ bits signed accumulator."),
    ("Sensor $1.65\\,\\text{V} + 10\\,\\text{mV}/g \\times a$, gain 100, 12-bit ADC ($0-3.3\\,\\text{V}$). Range and resolution:", "$\\pm 1.50\\,g, 0.733\\,\\text{mg/LSB}$", "$\\pm 1.65\\,g, 0.806\\,\\text{mg/LSB}$", "$\\pm 3.30\\,g, 0.806\\,\\text{mg/LSB}$", "$\\pm 1.65\\,g, 8.06\\,\\text{mg/LSB}$", "B", "$\\pm 1.65\\,g$ and $0.806\\,\\text{mg/LSB}$."),
    ("1500-byte packet across three $100\\,\\text{Mb/s}$ links, $2.0\\,\\text{ms}$ propagation per link. Total latency:", "$6.36\\,\\text{ms}$", "$6.48\\,\\text{ms}$", "$6.12\\,\\text{ms}$", "$6.24\\,\\text{ms}$", "A", "$3(0.12) + 3(2.0) = 6.36\\,\\text{ms}$."),
    ("Host IP $192.168.10.77/27$. Network, broadcast, usable range:", "$192.168.10.64, 192.168.10.95, 192.168.10.65-94$", "$192.168.10.0, 192.168.10.127, 192.168.10.1-126$", "$192.168.10.64, 192.168.10.96, 192.168.10.65-95$", "$192.168.10.72, 192.168.10.87, 192.168.10.73-86$", "A", "Subnet $64-95$."),
    ("Fiber $80\\,\\text{km}$ at $2.0\\times 10^8\\,\\text{m/s}$ vs Wireless $100\\,\\text{km}$ at $3.0\\times 10^8\\,\\text{m/s} + 0.15\\,\\text{ms}$. Lower latency:", "Fiber lower by $0.150\\,\\text{ms}$", "Wireless lower by $0.167\\,\\text{ms}$", "Wireless lower by $0.067\\,\\text{ms}$", "Fiber lower by $0.083\\,\\text{ms}$", "D", "Fiber $0.40\\,\\text{ms}$ vs Wireless $0.483\\,\\text{ms} \\implies 0.083\\,\\text{ms}$."),
    ("Workload $80\\%$ runs $20\\times$ on GPU, $20\\%$ on CPU, $5\\%$ transfer overhead. Overall speedup:", "$3.20$", "$3.45$", "$4.00$", "$4.35$", "B", "$1 / (0.04 + 0.20 + 0.05) = 3.45$.")
]

u2_theory = [
    {"q": "State KCL and KVL. For a loaded voltage divider ($V_S, R_1, R_2, R_L$), derive output voltage.", "sol": "KCL: sum of currents at a node is zero. KVL: sum of voltages around a loop is zero. Loaded divider output: $V_{out} = V_S \\frac{R_2 \\parallel R_L}{R_1 + R_2 \\parallel R_L} = V_S \\frac{R_2 R_L}{R_1(R_2+R_L) + R_2 R_L}$."},
    {"q": "Explain full-wave bridge rectifier with capacitor filter. Derive ripple voltage $V_{r(pp)} = \\frac{I_{DC}}{2fC}$.", "sol": "Bridge rectifier conducts on both half-cycles ($f_r = 2f$). Capacitor charges to peak $V_m - 2V_D$ and discharges through load over $\\Delta t = 1/(2f)$. Charge loss $\\Delta Q = I_{DC}/(2f) = C V_{r(pp)} \\implies V_{r(pp)} = \\frac{I_{DC}}{2fC}$."}
]

# Write all 6 units
make_clean_unit_file(1, "Solid State Physics", clean_set(u1_mcqs), u1_theory)
make_clean_unit_file(2, "Fundamentals of Electricity and Devices", clean_set(u2_mcqs), u2_theory)
make_clean_unit_file(3, "Introduction to Number System and Logic Gates", clean_set(u3_mcqs), u3_theory)
make_clean_unit_file(4, "Introduction to Combinational Logic Circuits", clean_set(u4_mcqs), u4_theory)
make_clean_unit_file(5, "Introduction to Sequential Logic Circuits", clean_set(u5_mcqs), u5_theory)
make_clean_unit_file(6, "Introduction of Arduino and Sensors", clean_set(u6_mcqs), u6_theory)

print("All 6 Question Bank units built cleanly!")
