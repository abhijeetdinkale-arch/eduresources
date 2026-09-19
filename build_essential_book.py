import os

# style.sty
style_sty = r"""\NeedsTeXFormat{LaTeX2e}
\ProvidesPackage{style}[2026/09/16 v1.0 CSE326 Essential Coursebook Style]

% Core Packages
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{lmodern}
\RequirePackage[margin=20mm,top=24mm,bottom=24mm,headheight=22pt]{geometry}
\RequirePackage{amsmath,amssymb,amsfonts}
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
\RequirePackage{listings}
\RequirePackage[hidelinks,colorlinks=true,linkcolor=DeepNavy,urlcolor=TealBlue,citecolor=DeepNavy]{hyperref}

% Color Palette - Student Friendly, High Contrast Theme
\definecolor{DeepNavy}{RGB}{15, 32, 67}
\definecolor{TealBlue}{RGB}{0, 128, 160}
\definecolor{AccentBlue}{RGB}{28, 90, 160}
\definecolor{LPUOrange}{RGB}{232, 90, 16}
\definecolor{DarkSlate}{RGB}{35, 45, 55}
\definecolor{LightBg}{RGB}{246, 248, 252}
\definecolor{BorderGray}{RGB}{205, 215, 225}
\definecolor{NoteYellow}{RGB}{254, 250, 235}
\definecolor{NoteBorder}{RGB}{230, 205, 140}
\definecolor{SuccessGreen}{RGB}{24, 134, 75}
\definecolor{CodeBg}{RGB}{245, 247, 250}

% Define JavaScript for listings
\lstdefinelanguage{JavaScript}{
  keywords={typeof, new, true, false, catch, function, return, null, catch, switch, var, if, in, while, do, else, case, break, const, let, document, window, alert, confirm, prompt, delete},
  keywordstyle=\color{AccentBlue}\bfseries,
  ndkeywords={class, export, boolean, throw, implements, import, this},
  ndkeywordstyle=\color{DeepNavy}\bfseries,
  identifierstyle=\color{black},
  sensitive=false,
  comment=[l]{//},
  morecomment=[s]{/*}{*/},
  commentstyle=\color{gray}\ttfamily,
  stringstyle=\color{LPUOrange}\ttfamily,
  morestring=[b]',
  morestring=[b]"
}

% Code Listing Settings
\lstset{
    basicstyle=\small\ttfamily,
    backgroundcolor=\color{CodeBg},
    frame=single,
    rulecolor=\color{BorderGray},
    keywordstyle=\color{AccentBlue}\bfseries,
    commentstyle=\color{gray},
    stringstyle=\color{LPUOrange},
    breaklines=true,
    showstringspaces=false
}

% Page Setup & Headers
\color{DarkSlate}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\sffamily\color{DeepNavy}\textbf{CSE326: Internet Programming} --- Essential Coursebook}
\fancyhead[R]{\small\sffamily\color{TealBlue}\textbf{Lovely Professional University}}
\fancyfoot[C]{\small\sffamily\thepage}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{DeepNavy}\leaders\hrule height \headrulewidth\hfill}}
\renewcommand{\footrulewidth}{0.3pt}

% Chapter & Section Formatting
\titleformat{\chapter}[display]
  {\normalfont\sffamily\huge\bfseries\color{DeepNavy}}
  {\Large\color{TealBlue}\chaptertitlename\ \thechapter}{8pt}
  {\titlerule[1.5pt]\vspace{4pt}}

\titleformat{\section}
  {\normalfont\sffamily\Large\bfseries\color{DeepNavy}}
  {\thesection}{1em}{}

\titleformat{\subsection}
  {\normalfont\sffamily\large\bfseries\color{TealBlue}}
  {\thesubsection}{0.8em}{}

% Custom Callout Boxes
\newtcolorbox{summarybox}[1][Key Concept / Summary]{%
  enhanced,
  breakable,
  colback=LightBg,
  colframe=TealBlue,
  arc=2mm,
  boxrule=0.9pt,
  fonttitle=\bfseries\sffamily\color{white},
  colbacktitle=TealBlue,
  title={#1},
  top=2.5mm, bottom=2.5mm, left=3.5mm, right=3.5mm
}

\newtcolorbox{notebox}[1][Important Rule / Note]{%
  enhanced,
  breakable,
  colback=NoteYellow,
  colframe=NoteBorder,
  arc=2mm,
  boxrule=0.9pt,
  fonttitle=\bfseries\sffamily\color{DarkSlate},
  colbacktitle=NoteBorder!60!NoteYellow,
  title={#1},
  top=2mm, bottom=2mm, left=3mm, right=3mm
}

\newtcolorbox{codeexample}[1][Code Example \& Output]{%
  enhanced,
  breakable,
  colback=white,
  colframe=DeepNavy,
  arc=2mm,
  boxrule=1pt,
  fonttitle=\bfseries\sffamily\color{white},
  colbacktitle=DeepNavy,
  title={#1},
  top=2.5mm, bottom=2.5mm, left=3.5mm, right=3.5mm
}

\newtcolorbox{quizbox}[1][Slide Quiz Question \& Trace]{%
  enhanced,
  breakable,
  colback=white,
  colframe=LPUOrange,
  arc=2mm,
  boxrule=1pt,
  fonttitle=\bfseries\sffamily\color{white},
  colbacktitle=LPUOrange,
  title={#1},
  top=2.5mm, bottom=2.5mm, left=3.5mm, right=3.5mm
}

\endinput
"""

with open("CSE326_Essential_Book/style.sty", "w") as f:
    f.write(style_sty)

# Cover
cover_tex = r"""\begin{titlepage}
\begin{center}
\vspace*{10mm}
{\Huge\sffamily\bfseries\color{DeepNavy} CSE326 / CSE236}\\[3mm]
{\LARGE\sffamily\bfseries\color{TealBlue} Internet Programming \& Web Technologies}\\[6mm]
{\Large\sffamily\bfseries Essential Coursebook: Short, Easy \& Comprehensive Study Guide}\\[4mm]
{\large\color{DarkSlate} Built Directly from LPU Lecture Slides (Dr. Navneet Kaur \& Prof. Lalit Verma) and Core Notes}\\[15mm]

\begin{tcolorbox}[enhanced,colback=LightBg,colframe=DeepNavy,arc=3mm,width=0.9\textwidth,boxrule=1.5pt]
\centering\vspace{2mm}
{\large\sffamily\bfseries\color{DeepNavy} WHAT MAKES THIS BOOK UNIQUE}\\[3mm]
\begin{itemize}[leftmargin=8mm,itemsep=1.5mm]
  \item \textbf{100\% Slide-Aligned}: Covers every single lecture slide, syntax, code sample, and explanation.
  \item \textbf{Short \& Easy to Grasp}: No unnecessary fluff; clean definitions, comparison tables, and quick summaries.
  \item \textbf{Complete Slide Quiz Walkthroughs}: Includes all slide quizzes with step-by-step code output traces.
  \item \textbf{Exam-Ready High-Yield Points}: Highlighted rules on semantic tags, Box Model formulas, and JS Scope.
\end{itemize}
\vspace{2mm}
\end{tcolorbox}

\vfill
{\large\sffamily\bfseries School of Computer Science \& Engineering}\\
{\large Lovely Professional University, Phagwara, Punjab}
\end{center}
\end{titlepage}
"""

with open("CSE326_Essential_Book/frontmatter/cover.tex", "w") as f:
    f.write(cover_tex)

print("Created style and cover.")
