# -*- coding: utf-8 -*-
import os

ch1_rev = r"""\chapter{Unit 1: Foundations of Learning, Creativity and Design Thinking}
\label{chap:unit1_rev}

\begin{revbox}[Unit 1 Essential Summary]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Design Thinking:} A non-linear, human-centred, iterative problem-solving methodology that starts with human empathy rather than technology.
    \item \textbf{Wicked Problems (Rittel \& Webber, 1973):} Ill-defined social/systemic problems with no definitive formulation, no immediate test, and no single correct answer.
    \item \textbf{Three Lenses of Innovation (IDEO):} Desirability (Human), Feasibility (Technical), and Viability (Business).
\end{itemize}
\end{revbox}

\section{Cognitive Dynamics \& Learning Models}

\begin{formulabox}[Kolb's Experiential Learning Cycle]
\begin{equation*}
\text{Concrete Experience} \longrightarrow \text{Reflective Observation} \longrightarrow \text{Abstract Conceptualization} \longrightarrow \text{Active Experimentation}
\end{equation*}
\end{formulabox}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Focused vs. Diffuse Thinking (Dr. Barbara Oakley):}
    \begin{itemize}
        \item *Focused Mode:* Concentrated attention, analytical step-by-step logic, error detection. (Trap: tunnel vision).
        \item *Diffuse Mode:* Relaxed resting-state default mode network; unconscious incubation, unexpected creative synthesis.
    \end{itemize}
    \item \textbf{Bloom's Revised Taxonomy Hierarchy:} Remember $\rightarrow$ Understand $\rightarrow$ Apply $\rightarrow$ Analyze $\rightarrow$ Evaluate $\rightarrow$ \textbf{Create} (Design Thinking operates at the peak: Create).
    \item \textbf{VARK Modalities:} Visual (V), Aural (A), Read/Write (R), Kinesthetic (K).
    \item \textbf{Functional Fixedness (Karl Duncker, 1945):} Cognitive bias where an object is perceived only in terms of its traditional use (e.g., Duncker's Candle Problem where the matchbox must be seen as a candle shelf).
\end{itemize}

\section{Creativity vs. Invention vs. Innovation}

\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{2.8cm}X X}
\toprule
\textbf{Term} & \textbf{Core Definition} & \textbf{Benchmark Example} \\
\midrule
\textbf{Creativity} & Psychological capacity to generate novel and contextually appropriate ideas. & Conceptualizing low-water sanitation methods. \\
\textbf{Invention} & Engineering a technically new device, process, or material (patentable). & Developing a micro-filtration membrane. \\
\textbf{Innovation} & Implementing, scaling, and driving commercial/social adoption of a solution. & Scaling low-cost drinking water kiosks in rural communities. \\
\bottomrule
\end{tabularx}
\caption{Distinction Between Creativity, Invention, and Innovation.}
\end{table}

\section{Milestones \& Landmark Case Studies}

\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{1919 (Bauhaus):} Walter Gropius unites form and functional manufacturing.
    \item \textbf{1969 (Herbert Simon):} *The Sciences of the Artificial* --- Design transforms existing situations into preferred ones.
    \item \textbf{1987 (Peter Rowe):} First book explicitly titled *Design Thinking*.
    \item \textbf{1991 (IDEO):} Commercialization of Human-Centred Design (Inspiration $\rightarrow$ Ideation $\rightarrow$ Implementation).
    \item \textbf{2005 (Stanford d.school):} 5-Stage Model (Empathize $\rightarrow$ Define $\rightarrow$ Ideate $\rightarrow$ Prototype $\rightarrow$ Test).
\end{itemize}

\begin{casebox}[Global Case Study Takeaways]
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{OXO Good Grips (1990):} Universal design (thick ribbed rubber handle) created for arthritis patients became a dominant consumer hit.
    \item \textbf{M-Pesa (Kenya, 2007):} SMS-based micro-banking using local corner agents democratized banking for unbanked populations.
    \item \textbf{Jaipur Foot (India):} Low-cost waterproof prosthetic designed for local cultural habits (squatting, barefoot farming).
    \item \textbf{Juicero Failure (2017):} \$700 Wi-Fi juice press collapsed because packets were easily hand-squeezed; over-engineered a non-existent need.
\end{itemize}
\end{casebox}
"""

ch2_rev = r"""\chapter{Unit 2: Empathy, Observation and Problem Identification}
\label{chap:unit2_rev}

\begin{revbox}[Unit 2 Essential Summary]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{User Empathy:} Stepping into the user's lived experience to discover motivations, emotions, and hidden needs.
    \item \textbf{Computational Empathy:} Designing software that adapts to human context, cognitive limits, emotional distress, and accessibility.
    \item \textbf{Need vs. Solution:} Needs are functional/emotional outcomes (e.g., ``timely arrival updates''); solutions are specific technical implementations (e.g., ``mobile GPS tracker'').
\end{itemize}
\end{revbox}

\section{Research Methods \& The AEIOU Framework}

\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{2.8cm}X X}
\toprule
\textbf{Dimension} & \textbf{Qualitative Research} & \textbf{Quantitative Research} \\
\midrule
\textbf{Focus} & Deep ``Why'' and ``How'' behind behaviors. & Measurable ``How many'' and ``How much''. \\
\textbf{Methods} & Semi-structured interviews, diary logs, observation. & Surveys ($N \ge 100$), clickstream telemetry, A/B tests. \\
\textbf{Sample} & Small, purposive sample ($N = 5 \text{ to } 15$). & Large, statistically representative sample. \\
\bottomrule
\end{tabularx}
\caption{Qualitative vs. Quantitative Research Comparison.}
\end{table}

\begin{formulabox}[The 5 AEIOU Field Observation Lenses]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{A --- Activities:} Purposeful actions and workflows people perform.
    \item \textbf{E --- Environments:} Physical/digital context (lighting, noise, clutter, connectivity).
    \item \textbf{I --- Interactions:} Exchanges between person-person, person-device, or person-system.
    \item \textbf{O --- Objects:} Physical/digital tools, improvised cheat-sheets, sticky notes, keycards.
    \item \textbf{U --- Users:} The individuals observed, their roles, behaviors, and relationships.
\end{itemize}
\end{formulabox}

\section{Inquiry Tactics, Needs, and Personas}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Interviewing Rules:} Use open-ended narrative questions (*``Tell me about the last time you...''*); avoid leading bias (*avoid ``Don't you love our fast app?''*); use Critical Incidents (extreme stories of success/failure); apply Laddering (5 Whys) to uncover root emotional drivers.
    \item \textbf{Explicit vs. Implicit Needs:}
    \begin{itemize}
        \item *Explicit Needs:* Directly stated requirements (e.g., ``I need an export button'').
        \item *Implicit (Latent) Needs:* Unspoken desires inferred through workarounds and hesitation (e.g., need for audit reassurance and data security).
    \end{itemize}
    \item \textbf{Pain Point Classes:} Time Pain (delays), Process Pain (fragmented apps), Financial Pain (hidden fees), Emotional Pain (anxiety/confusion).
    \item \textbf{User Personas:} Research-grounded archetypes representing goals, behaviors, frustrations, and context.
\end{itemize}

\section{Empathy Mapping, POV, and HMW}

\begin{center}
\small
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\textbf{SAYS} (Direct Quotes) & \textbf{THINKS} (Inferred Beliefs \& Doubts) \\
\textit{``I never know if the form was received.''} & \textit{``Will I be billed twice if I click submit again?''} \\
\hline
\textbf{DOES} (Observable Workarounds) & \textbf{FEELS} (Emotions) \\
\textit{Takes screenshots, calls customer support.} & \textit{Anxious, confused, hesitant.} \\
\hline
\multicolumn{2}{|c|}{\textbf{PAINS:} Financial uncertainty \quad\textbar\quad \textbf{GAINS:} Clear confirmation} \\
\hline
\end{tabularx}
\end{center}

\begin{formulabox}[POV and HMW Formulation]
$$\text{\textbf{POV}} = [\;\text{User Profile}\;] \;+\; [\;\text{Core Need}\;] \;+\; [\;\text{Surprising Insight}\;]$$
$$\text{\textbf{HMW Question}} = \text{``How might we [actionable challenge] without [prescribing exact solution]?''}$$
\end{formulabox}
"""

ch3_rev = r"""\chapter{Unit 3: Ideation and Creative Problem Solving}
\label{chap:unit3_rev}

\begin{revbox}[Unit 3 Essential Summary]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Ideation:} Transitioning from problem definition to wide candidate solution generation.
    \item \textbf{Golden Rule:} Defer judgment; strictly separate divergent generation from convergent selection.
    \item \textbf{4 Creativity Metrics:} Fluency (volume), Flexibility (diversity of categories), Originality (rarity), Elaboration (level of detail).
\end{itemize}
\end{revbox}

\section{Ideation Toolkits \& Associative Techniques}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Brainstorming Rules (Alex Osborn, 1953):} Defer judgment, go for quantity, encourage wild ideas, build on others using \textbf{``Yes, and...''}.
    \item \textbf{Brainwriting (6-3-5):} 6 participants write 3 ideas per sheet for 5 minutes, rotating sheets silently to eliminate dominant speaker bias (yields 108 ideas in 30 mins).
    \item \textbf{SCAMPER Framework:}
    \begin{itemize}
        \item \textbf{S --- Substitute:} Replace materials or actors (paper ticket $\rightarrow$ QR code).
        \item \textbf{C --- Combine:} Merge distinct tools (phone + camera = smartphone).
        \item \textbf{A --- Adapt:} Borrow from other domains (Kingfisher beak $\rightarrow$ bullet train nose).
        \item \textbf{M --- Modify / Magnify / Minify:} Alter size, speed, scale (enlarge emergency stop button).
        \item \textbf{P --- Put to Another Use:} Repurpose assets (shipping containers $\rightarrow$ mobile clinics).
        \item \textbf{E --- Eliminate:} Remove redundant complexity (remove physical keyboard).
        \item \textbf{R --- Reverse / Rearrange:} Invert roles/sequence (Uber drivers come to customer).
    \end{itemize}
    \item \textbf{Reverse Thinking (Inversion / Worst Idea):} Brainstorm ways to make the problem disastrous, then invert findings into robust design features.
\end{itemize}

\section{Organizing, Screening \& Prioritization}

\begin{formulabox}[Weighted Idea Screening Matrix Formula]
\begin{equation*}
T_i = \sum_{j=1}^n \left( w_j \times s_{ij} \right) \quad \text{where} \quad \sum w_j = 1.0, \quad s_{ij} \in [1, 5]
\end{equation*}
\textit{Example:} Desirability ($w=0.5, s=4$) + Feasibility ($w=0.3, s=5$) + Viability ($w=0.2, s=4$) = $2.0 + 1.5 + 0.8 = \mathbf{4.3}$.
\end{formulabox}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Impact-Effort 2x2 Matrix:}
    \begin{itemize}
        \item *High Impact, Low Effort:* **Quick Wins** (Implement first).
        \item *High Impact, High Effort:* **Major Projects / Strategic Bets** (Plan carefully).
        \item *Low Impact, Low Effort:* **Fill-ins** (Do if surplus time permits).
        \item *Low Impact, High Effort:* **Thankless Tasks / Money Pits** (Drop/Avoid).
    \end{itemize}
    \item \textbf{Dot Voting:} Democratic, visual heat-mapping of team preferences using colored adhesive dots.
\end{itemize}
"""

ch4_rev = r"""\chapter{Unit 4: Product Design and Prototyping}
\label{chap:unit4_rev}

\begin{revbox}[Unit 4 Essential Summary]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Prototyping Philosophy:} *``Build to think, test to learn''*. Fail early and cheaply to reduce risk.
    \item \textbf{Riskiest Assumptions First:} Always test whether users need and trust the core value before polishing UI colors.
    \item \textbf{Traceability:} Connect every wireframe element directly back to a validated user requirement.
\end{itemize}
\end{revbox}

\section{Fidelity Comparison \& Paper Prototyping}

\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{2.8cm}X X}
\toprule
\textbf{Dimension} & \textbf{Low-Fidelity (Lo-Fi)} & \textbf{High-Fidelity (Hi-Fi)} \\
\midrule
\textbf{Materials} & Paper, cardboard, sticky notes, sketches. & Clickable Figma mockups, coded frontend. \\
\textbf{Time \& Cost} & Minutes to hours; zero monetary cost. & Days to weeks; requires technical tools. \\
\textbf{Testing Focus} & Information architecture, layout, user flows. & Visual hierarchy, micro-interactions, metrics. \\
\textbf{Feedback} & Honest, conceptual, structural critique. & Detailed aesthetic and UI styling comments. \\
\bottomrule
\end{tabularx}
\caption{Lo-Fi vs. Hi-Fi Prototype Trade-Offs.}
\end{table}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Paper Prototyping Roles:}
    \begin{itemize}
        \item *User:* Interacts by pointing, tapping, and typing with a pen.
        \item *``Computer'' (Facilitator):* Silently swaps paper screens and popups.
        \item *Observer:* Silently records task time, hesitation, and errors.
    \end{itemize}
    \item \textbf{Storyboarding:} 4-frame comic-strip narrative showing user problem trigger $\rightarrow$ discovery $\rightarrow$ interaction $\rightarrow$ emotional resolution in context.
\end{itemize}

\section{Wireframing Conventions \& User Flows}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Grayscale Restraint:} Use only shades of gray to focus on structure, layout, and hierarchy without color distraction.
    \item \textbf{UI Control Rules:}
    \begin{itemize}
        \item \textbf{Radio Buttons ($\odot$):} Exactly ONE selection from a mutually exclusive list.
        \item \textbf{Checkboxes ($\boxtimes$):} Zero, one, or MULTIPLE independent selections.
        \item \textbf{Toggle Switch:} Immediate on/off binary setting.
        \item \textbf{Image Placeholder:} Crossed rectangle ($[\boxtimes]$).
    \end{itemize}
    \item \textbf{User Flowchart Symbols:}
    \begin{itemize}
        \item *Oval (Terminator):* Start / End of task.
        \item *Rectangle:* Screen, Step, or System Action.
        \item *Diamond:* Conditional decision point with branching logic (Yes/No).
    \end{itemize}
\end{itemize}

\section{Minimum Viable Product (MVP)}

\begin{formulabox}[MVP Core Definition \& Forms]
An MVP is the smallest coherent release that delivers \textbf{complete end-to-end value} and enables maximum validated learning.
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Landing Page MVP:} Web page measuring click-through demand before writing code.
    \item \textbf{Concierge MVP:} Delivering service manually behind the scenes to study user behavior.
    \item \textbf{Wizard of Oz MVP:} Appears automated on front-end, but operated manually by humans in backend.
\end{itemize}
\end{formulabox}
"""

ch5_rev = r"""\chapter{Unit 5: Testing, Validation and Customer Experience}
\label{chap:unit5_rev}

\begin{revbox}[Unit 5 Essential Summary]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Usability Testing:} Evaluates if users can use the interface effectively and efficiently (*``Did we build it right?''*).
    \item \textbf{Design Validation:} Evaluates if the product solves the real core human problem (*``Did we build the right thing?''*).
    \item \textbf{``Show, Don't Tell'' Doctrine:} Put the prototype in front of the user; observe natural behavior without pitching or explaining.
\end{itemize}
\end{revbox}

\section{Testing Conduct \& Feedback Capture Matrix}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Neutral Facilitation:} Reassure user (*``We are testing the product, not you''*); use non-leading neutral prompts (*``What did you expect to happen?''*); utilize the Think-Aloud Protocol.
    \item \textbf{Goal-Oriented Task Scenarios:} Provide realistic context, constraints, and end goals without revealing button names or navigation sequences.
    \item \textbf{Feedback Capture Matrix:}
    \begin{itemize}
        \item \textbf{Likes (+):} Elements users praised or found intuitive.
        \item \textbf{Wishes ($\Delta$):} Constructive criticisms and unmet expectations.
        \item \textbf{Questions (?):} Confusions and queries raised during testing.
        \item \textbf{Ideas (!):} New feature suggestions sparked during sessions.
    \end{itemize}
\end{itemize}

\section{Usability vs. Customer Experience (CX) \& Journey Mapping}

\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{2.8cm}X X}
\toprule
\textbf{Dimension} & \textbf{Usability (UI/UX)} & \textbf{Customer Experience (CX)} \\
\midrule
\textbf{Scope} & Interface-specific task interaction. & Holistic end-to-end relationship across all channels. \\
\textbf{Timeframe} & Minutes of active product usage. & Entire customer lifecycle (discovery to offboarding). \\
\textbf{Touchpoints} & Screen buttons, menus, mobile app. & Human (couriers), Digital (apps), Physical (packaging). \\
\textbf{Key Metrics} & Task Completion Rate, Time on Task, SEQ. & Net Promoter Score (NPS), CSAT, Retention Rate. \\
\bottomrule
\end{tabularx}
\caption{Usability vs. Customer Experience (CX) Comparison.}
\end{table}

\section{Digital Accessibility: WCAG POUR Principles}

\begin{formulabox}[The 4 WCAG Principles]
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Perceivable (P):} Provide text alternatives (\texttt{alt}-text) for non-text media; maintain minimum contrast ratio: \textbf{4.5:1} for normal body text, \textbf{3:1} for large text.
    \item \textbf{Operable (O):} Full keyboard navigation without requiring mouse gestures; no keyboard traps.
    \item \textbf{Understandable (U):} Predictable navigation, inline form validation, and clear error recovery.
    \item \textbf{Robust (R):} Compatibility across browsers and assistive screen readers.
\end{enumerate}
\end{formulabox}
"""

ch6_rev = r"""\chapter{Unit 6: Innovation Project, Re-Design and Product Presentation}
\label{chap:unit6_rev}

\begin{revbox}[Unit 6 Essential Summary]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Innovation Lifecycle:} Ongoing empirical loop of building, testing, learning, and refactoring.
    \item \textbf{Refactoring vs. Re-Design:} Refactoring improves internal quality without changing behavior; Re-design fundamentally overhauls core architecture.
    \item \textbf{NABC Model:} Pitching framework covering Need, Approach, Benefits per costs, and Competition.
\end{itemize}
\end{revbox}

\section{Iteration, Prioritization \& Pivots}

\begin{formulabox}[Feedback Priority Formula & PDCA Cycle]
\begin{equation*}
P = F \times S \times C
\end{equation*}
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item $F \in [1, 5]$: Frequency \quad\textbar\quad $S \in [1, 5]$: Severity \quad\textbar\quad $C \in [0.1, 1.0]$: Confidence.
    \item *Severe safety/task blockers ($S=5$) outrank common cosmetic tweaks ($S=1$).*
    \item \textbf{PDCA Continuous Improvement Loop:} \textbf{Plan} $\rightarrow$ \textbf{Do} $\rightarrow$ \textbf{Check} $\rightarrow$ \textbf{Act}.
\end{itemize}
\end{formulabox}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Regression Testing:} Retesting previously working features after any code or design change to ensure zero new defects were introduced.
    \item \textbf{Strategic Pivot:} Course correction changing target audience, channel, or value proposition while preserving validated past learning (e.g., YouTube video dating $\rightarrow$ universal video sharing).
\end{itemize}

\section{Product Presentation Frameworks}

\subsection{Audience Calibration}
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Users:} Highlight personal convenience, comfort, and direct problem relief.
    \item \textbf{Engineers:} Highlight technical feasibility, component specs, latency, and safety.
    \item \textbf{Investors / Executives:} Highlight business viability, unit economics, scalability, ROI, and NABC.
\end{itemize}

\subsection{The NABC Framework}
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{N --- Need:} Specific, quantitative, validated user pain point backed by research.
    \item \textbf{A --- Approach:} Unique, feasible technology mechanism or service model.
    \item \textbf{B --- Benefits per Costs:} Measurable net value delivered relative to user cost/friction.
    \item \textbf{C --- Competition / Alternatives:} Clear relative advantage over existing competitors and workarounds.
\end{itemize}

\subsection{The Elevator Pitch Template (30--60 Seconds)}
\begin{quote}
\textit{``For \textbf{[target user]} who experiences \textbf{[validated problem]}, our \textbf{[product name]} is a \textbf{[product category]} that delivers \textbf{[core benefit]}. Unlike \textbf{[existing competitor/workaround]}, our solution \textbf{[key differentiator]}. User testing shows \textbf{[empirical metric evidence]}. We seek \textbf{[actionable call-to-action]}.''}
\end{quote}
"""

with open("INT335_Revision_Book/chapters/chapter1_revision.tex", "w", encoding="utf-8") as f:
    f.write(ch1_rev)
with open("INT335_Revision_Book/chapters/chapter2_revision.tex", "w", encoding="utf-8") as f:
    f.write(ch2_rev)
with open("INT335_Revision_Book/chapters/chapter3_revision.tex", "w", encoding="utf-8") as f:
    f.write(ch3_rev)
with open("INT335_Revision_Book/chapters/chapter4_revision.tex", "w", encoding="utf-8") as f:
    f.write(ch4_rev)
with open("INT335_Revision_Book/chapters/chapter5_revision.tex", "w", encoding="utf-8") as f:
    f.write(ch5_rev)
with open("INT335_Revision_Book/chapters/chapter6_revision.tex", "w", encoding="utf-8") as f:
    f.write(ch6_rev)

print("All Revision Book chapters generated successfully.")
