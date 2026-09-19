# -*- coding: utf-8 -*-
import os

# CHAPTER 2
ch2 = r"""\chapter{Empathy, Observation and Problem Identification}
\label{chap:empathy_observation}

\begin{tcolorbox}[enhanced, colback=boxnavybg, colframe=brandnavy, boxrule=1.2pt, arc=4pt, title={\Large\bfseries\sffamily Unit 2 Overview \& Learning Objectives}]
\sffamily\normalsize
This unit covers the foundational phase of understanding users, observing real behaviors in context, and framing actionable problem definitions. By the end of this unit, students will be able to:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt, topsep=3pt]
    \item Understand User Empathy and distinguish between empathy, sympathy, and projection.
    \item Apply \textbf{Computational Empathy} to design responsive, human-aware software interfaces.
    \item Compare \textbf{Qualitative} and \textbf{Quantitative} user research methods and implement data triangulation.
    \item Conduct structured field observations using the 5-lens \textbf{AEIOU Framework}.
    \item Execute user interviews using open inquiry, critical incidents, and the \textbf{5 Whys / Laddering} technique.
    \item Differentiate between \textbf{Explicit} (stated) and \textbf{Implicit/Latent} (unstated) user needs.
    \item Diagnose functional, financial, process, and emotional \textbf{User Pain Points}.
    \item Construct research-grounded \textbf{User Personas} and behavioural target archetypes.
    \item Synthesize research data using 4-quadrant \textbf{Empathy Maps} and formulate actionable \textbf{Point-of-View (POV)} and \textbf{How Might We (HMW)} prompts.
\end{itemize}
\end{tcolorbox}

\section{Orientation: The Primacy of Empathy}

Empathy is the intellectual and emotional discipline of stepping into the user's world to experience their environment, feelings, motivations, and constraints. In Design Thinking, empathy is not passive pity (sympathy), but an active empirical investigation that replaces internal designer assumptions with observed user reality.

\begin{definition}[Computational Empathy]
The engineering philosophy and practice of designing software architectures, UI flows, and algorithms that dynamically detect, respect, and adapt to the cognitive limits, physical accessibility needs, emotional states, and environmental context of human users.
\end{definition}

\subsection{Key Principles of Computational Empathy}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Context Awareness:} Systems adapt gracefully to adverse conditions (e.g., poor network bandwidth, one-handed mobile use, high ambient glare).
    \item \textbf{Calm Error Handling:} Cryptic error codes (e.g., ``Error 0x800F'') are replaced with empathetic, actionable plain-language explanations (e.g., ``Your card was declined. Please verify your billing PIN'').
    \item \textbf{Universal Accessibility:} Full compliance with WCAG principles (keyboard navigation, screen-reader semantic landmarks, high contrast) ensuring no user is excluded.
    \item \textbf{Human Override:} Automated AI or recommendation systems must provide clear escape hatches and human escalation paths when automated decisions fail.
\end{itemize}

\section{User Research Methodologies: Depth vs. Breadth}

\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{3.2cm}X X}
\toprule
\textbf{Attribute} & \textbf{Qualitative Research} & \textbf{Quantitative Research} \\
\midrule
\textbf{Core Question} & ``Why and how do users experience this?'' & ``How many / How much / How often?'' \\
\textbf{Data Type} & Descriptive narratives, quotes, field video. & Numerical data, percentages, clickstream logs. \\
\textbf{Methods} & Semi-structured interviews, diary studies. & Surveys ($N \ge 100$), telemetry analytics, A/B tests. \\
\textbf{Sample Size} & Small, purposive sample ($N = 5 \text{ to } 15$). & Large, statistically representative sample. \\
\textbf{Primary Value} & Discovers non-obvious root causes \& pain points. & Validates the scale and statistical frequency of findings. \\
\bottomrule
\end{tabularx}
\caption{Comparison of Qualitative and Quantitative User Research.}
\end{table}

\begin{keyequation}[Data Triangulation]
To prevent subjective bias, design teams must triangulate at least three distinct data sources:
\begin{equation}
\text{Validated Insight} = \text{Observational Behavior (Field)} \;\cap\; \text{Self-Reported Quotes (Interviews)} \;\cap\; \text{Telemetry Data (Analytics)}
\end{equation}
\end{keyequation}

\section{The AEIOU Field Observation Framework}

The AEIOU framework, developed by Rick Robinson at E-Lab, provides five systematic observation lenses:
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Activities (A):} General actions and purposeful pathways people carry out (e.g., searching for a doctor, scanning an ID card).
    \item \textbf{Environments (E):} The physical and digital space (lighting, acoustic noise, crowded waiting rooms, distraction levels).
    \item \textbf{Interactions (I):} The building blocks of relationships between person-to-person, person-to-device, or person-to-system.
    \item \textbf{Objects (O):} Physical and digital tools, improvised cheat-sheets, sticky notes, keycards, or customized hardware.
    \item \textbf{Users (U):} The people observed, their roles, team hierarchies, physical postures, and social dynamics.
\end{itemize}

\section{User Interviewing \& Inquiry Techniques}

\subsection{The Art of the Non-Leading Interview}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Open-Ended Inquiry:} Always ask for historical narrative stories (*``Tell me about the last time you booked a train ticket...''*) rather than speculative opinions (*``Would you use an app that...?''*).
    \item \textbf{Critical Incident Technique:} Ask users to recount extreme moments of extreme satisfaction or catastrophic failure (*``Tell me about the worst experience you had with customer support''*).
    \item \textbf{Laddering (The 5 Whys):} Progressively asking ``Why'' to drill down from a surface behavior to the fundamental emotional and psychological driver.
\end{itemize}

\begin{example}[Laddering Technique in Action]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item *Observation:* User keeps paper receipts in an envelope inside their desk.
    \item *Why 1:* ``Why do you keep paper receipts?'' $\rightarrow$ ``In case I need to claim reimbursement.''
    \item *Why 2:* ``Why do you keep the physical paper rather than phone photos?'' $\rightarrow$ ``Because our accounting portal often rejects image uploads.''
    \item *Why 3:* ``Why does it reject them?'' $\rightarrow$ ``The file size limit is 200 KB and it fails silently without telling me.''
    \item *Why 4:* ``Why does that worry you?'' $\rightarrow$ ``Because if I miss the month-end deadline, the money is deducted from my personal salary.''
    \item *Core Insight:* The user's need is not a physical envelope; it is **financial security and certainty of successful receipt submission**.
\end{itemize}
\end{example}

\section{Needs, Pain Points, and Personas}

\subsection{Explicit vs. Implicit User Needs}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Explicit Needs:} Directly stated and verbalized (e.g., ``I need an export-to-PDF button'').
    \item \textbf{Implicit / Latent Needs:} Unstated desires inferred through observation of friction, workarounds, and hesitation (e.g., need for tamper-proof document verification and audit trail reassurance).
\end{itemize}

\subsection{Classification of User Pain Points}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Time Pain:} Unnecessary delays, redundant data entry, sluggish page loads.
    \item \textbf{Process Pain:} Fragmented workflows, forced switching between multiple apps.
    \item \textbf{Financial Pain:} Hidden transaction fees, unexpected subscription charges.
    \item \textbf{Emotional Pain:} Anxiety, embarrassment, fear of data loss, confusion.
\end{enumerate}

\subsection{User Personas & Target Archetypes}
A \textbf{User Persona} is a composite, research-backed archetype representing a key user segment sharing common goals, mental models, frustrations, and technical context.
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Primary Persona:} The core target whose needs drive the product architecture. Satisfying their needs must not be compromised.
    \item \textbf{Secondary Persona:} Additional user groups whose requirements are addressed as long as they do not hinder the primary persona.
    \item \textbf{Anti-Persona:} Profiles of users for whom the product is explicitly *not* designed.
\end{itemize}

\section{Empathy Mapping \& Problem Definition}

\subsection{The 4-Quadrant Empathy Map}
\begin{center}
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\textbf{SAYS} (Direct Quotes) & \textbf{THINKS} (Inferred Beliefs \& Doubts) \\
\textit{``I never know if my payment went through.''} & \textit{``If I click submit again, will I be charged twice?''} \\
\hline
\textbf{DOES} (Observable Actions \& Workarounds) & \textbf{FEELS} (Emotional States) \\
\textit{Takes screenshot of screen, calls bank customer care.} & \textit{Anxious, frustrated, vulnerable, hesitant.} \\
\hline
\multicolumn{2}{|c|}{\textbf{PAINS:} Financial uncertainty, duplicate charges \quad\textbar\quad \textbf{GAINS:} Instant verification, clear receipt} \\
\hline
\end{tabularx}
\end{center}

\subsection{Formulating POV Statements and HMW Questions}
\begin{keyequation}[Point-of-View (POV) Formula]
\begin{equation}
\text{\textbf{POV Statement}} = [\;\text{\textbf{User Profile}}\;] \quad+\quad [\;\text{\textbf{Core Need}}\;] \quad+\quad [\;\text{\textbf{Surprising Insight}}\;]
\end{equation}
\textit{Example:} ``A first-time hostel student (User) needs an unambiguous, real-time laundry tracking indicator (Need) because when washing machines fail silently, they waste 40 minutes sitting in the basement out of fear their clothes will be stolen (Insight).''
\end{keyequation}

\noindent From the POV statement, the team generates **How Might We (HMW)** questions:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item *HMW ensure students know machine status before leaving their dorm room?*
    \item *HMW guarantee laundry security without requiring physical human presence?*
\end{itemize}

\section{Unit 2 Self-Assessment Test}

\begin{chaptertest}[Empathy, Observation \& Problem Identification]
\textbf{Time Allowed: 30 Minutes \hfill Maximum Marks: 25}

\vspace{0.4cm}
\noindent\textbf{Part A: Conceptual Multiple Choice (5 $\times$ 1 = 5 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item What does the ``I'' represent in the AEIOU observation framework?
    \item Why are leading questions strictly avoided during user interviews?
    \item In an empathy map, where do observed physical workarounds belong?
    \item What type of pain point is caused by unexpected hidden fees at the final payment step?
    \item What are the three core components of a Point-of-View (POV) statement?
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part B: Short Analytical Questions (2 $\times$ 5 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{5}
    \item Differentiate between \textbf{Explicit Needs} and \textbf{Implicit/Latent Needs} with concrete software engineering examples.
    \item Explain the concept of \textbf{Computational Empathy} and detail three architectural features that embody it.
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part C: Practical Application Scenario (1 $\times$ 10 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{7}
    \item You are tasked with designing an ATM interface for senior citizens with mild vision and motor impairments.
    \begin{enumerate}[label=(\alph*)]
        \item Construct a 4-quadrant Empathy Map (Says, Thinks, Does, Feels).
        \item Draft a formal Point-of-View (POV) statement.
        \item Generate three divergent ``How Might We'' (HMW) challenge questions.
    \end{enumerate}
\end{enumerate}
\end{chaptertest}

\begin{solutionbox}[Step-by-Step Unit Test Solutions]
\textbf{Part A Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item Interactions (exchanges between humans, devices, and systems).
    \item They introduce severe confirmation bias by nudging the user toward a desired answer.
    \item The ``DOES'' quadrant.
    \item Financial Pain Point.
    \item User + Need + Surprising Insight.
\end{enumerate}

\textbf{Part B Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{5}
    \item \textbf{Explicit vs. Implicit Needs:}
    \begin{itemize}
        \item *Explicit Needs:* Directly verbalized by users (e.g., ``I need a dark mode toggle'').
        \item *Implicit Needs:* Unspoken expectations discovered through behavioral analysis (e.g., need for reduced eye strain during late-night shifts and reassurance that battery power is conserved).
    \end{itemize}
    \item \textbf{Computational Empathy Features:}
    \begin{itemize}
        \item *Graceful Degradation:* Caching data locally when network connectivity drops.
        \item *Context-Aware Input:* Adjusting touch target sizes when vehicle vibration is detected.
        \item *Empathetic Error Messaging:* Clearly stating what failed, why it failed, and providing an instant one-click recovery button.
    \end{itemize}
\end{enumerate}

\textbf{Part C Solution:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{7}
    \item \textbf{Senior Citizen ATM Solution:}
    \begin{itemize}
        \item *(a) Empathy Map:*
        \begin{itemize}
            \item **Says:** ``The screen text is too small and the timer counts down too fast.''
            \item **Thinks:** ``What if my card gets swallowed because I took too long to type my PIN?''
            \item **Does:** Squints closely, shields screen with hand, asks strangers for help.
            \item **Feels:** Vulnerable, rushed, anxious about financial theft.
        \end{itemize}
        \item *(b) POV Statement:* ``Elderly banking customers (User) need an unhurried, high-contrast withdrawal flow with tactile feedback (Need) because rapid countdown timers and glare create intense anxiety that leads to transaction abandonment or dangerous reliance on strangers (Insight).''
        \item *(c) HMW Questions:*
        \begin{enumerate}
            \item HMW eliminate time-based anxiety during PIN entry?
            \item HMW provide discrete, private audio guidance without drawing attention?
            \item HMW confirm physical cash dispensing through multi-sensory feedback?
        \end{enumerate}
    \end{itemize}
\end{enumerate}
\end{solutionbox}
"""

with open("INT335/chapters/chapter-02-empathy-observation-and-problem-identification.tex", "w", encoding="utf-8") as f:
    f.write(ch2)

# CHAPTER 3
ch3 = r"""\chapter{Ideation and Creative Problem Solving}
\label{chap:ideation_creative_solving}

\begin{tcolorbox}[enhanced, colback=boxnavybg, colframe=brandnavy, boxrule=1.2pt, arc=4pt, title={\Large\bfseries\sffamily Unit 3 Overview \& Learning Objectives}]
\sffamily\normalsize
This unit explores methods for expanding the solution space and systematically converging on high-potential concepts. By the conclusion of this chapter, students will be able to:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt, topsep=3pt]
    \item Understand the fundamental principles of the \textbf{Ideation Phase}.
    \item Measure creative outputs across the 4 dimensions: \textbf{Fluency, Flexibility, Originality, and Elaboration}.
    \item Apply \textbf{Alex Osborn's Brainstorming Rules} and silent \textbf{Brainwriting (6-3-5)}.
    \item Transform existing ideas using the 7 prompts of the \textbf{SCAMPER} framework.
    \item Utilize \textbf{Mind Mapping} and \textbf{Reverse Thinking (Inversion / Worst Idea)} to break mental sets.
    \item Organize unstructured ideas using \textbf{Affinity Diagramming} and Concept Bundling.
    \item Construct and calculate \textbf{Weighted Idea Screening Matrices}.
    \item Prioritize concepts using the \textbf{Impact-Effort 2x2 Matrix} and Dot Voting.
\end{itemize}
\end{tcolorbox}

\section{Foundations of Ideation}

Ideation is the creative engine of Design Thinking, where insights extracted during Empathy and Definition are synthesized into diverse candidate solutions. 

\begin{definition}[The Golden Rule of Ideation]
\textbf{Strictly separate idea generation (divergence) from idea evaluation (convergence).} Premature criticism kills novelty; unconstrained generation without structured convergence leads to paralysis.
\end{definition}

\subsection{The Four Dimensions of Creativity (Torrance Framework)}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Fluency:} The sheer total quantity of ideas generated within a specified timeframe.
    \item \textbf{Flexibility:} The number of distinctly different conceptual categories or domains represented.
    \item \textbf{Originality:} The statistical rarity, uniqueness, and unconventional nature of the idea.
    \item \textbf{Elaboration:} The depth of detail, mechanics, and operational clarity added to a concept.
\end{enumerate}

\section{Ideation Techniques and Toolkits}

\subsection{Classic Brainstorming Rules (Alex Osborn, 1953)}
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Defer Judgment:} No criticism, evaluation, or negative facial expressions permitted during generation.
    \item \textbf{Go for Quantity:} High volume increases the statistical probability of generating breakthrough solutions.
    \item \textbf{Encourage Wild Ideas:} Outlandish concepts often contain the seeds of radical innovation.
    \item \textbf{Build on Others' Ideas:} Use the improv principle \textbf{``Yes, and...''} to combine and expand concepts.
    \item \textbf{One Conversation at a Time:} Keep the entire team focused on a single prompt.
\end{itemize}

\subsection{Brainwriting (6-3-5 Method)}
To eliminate *production blocking* (where loud speakers dominate and quiet members suppress ideas), the 6-3-5 method is used:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{6 Participants} $\times$ \textbf{3 Ideas per sheet} $\times$ \textbf{5 Minutes per round}.
    \item Sheets are passed silently to the adjacent teammate who builds upon the previous ideas, yielding $6 \times 3 \times 6 = 108$ ideas in 30 minutes.
\end{itemize}

\subsection{The SCAMPER Framework}
SCAMPER is an associative transformation tool that applies 7 distinct cognitive operators to an existing system:
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{S --- Substitute:} Replace materials, components, rules, or actors (e.g., plastic cups $\rightarrow$ edible seaweed pods).
    \item \textbf{C --- Combine:} Merge distinct functions or technologies (e.g., phone + camera + GPS = smartphone).
    \item \textbf{A --- Adapt:} Borrow mechanisms from unrelated domains (e.g., applying bullet train aerodynamics inspired by the Kingfisher bird's beak).
    \item \textbf{M --- Modify / Magnify / Minify:} Alter scale, frequency, speed, or thickness (e.g., magnifying high-priority emergency buttons).
    \item \textbf{P --- Put to Another Use:} Repurpose an existing asset for a new problem (e.g., using shipping containers as modular medical clinics).
    \item \textbf{E --- Eliminate:} Strip away complexity, non-essential steps, or parts (e.g., removing physical keyboards from smartphones).
    \item \textbf{R --- Reverse / Rearrange:} Invert sequences, roles, or layouts (e.g., Uber having drivers come to the customer rather than customers waving down taxis).
\end{itemize}

\subsection{Reverse Thinking (Inversion / Worst Possible Idea)}
Instead of asking how to solve a problem, ask: *``How could we make this problem completely catastrophic?''*
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item *Challenge:* Improve hospital patient satisfaction.
    \item *Worst Idea:* Make patients wait in the rain with zero information and lose their medical records.
    \item *Inversion:* Provide an indoor heated lounge with real-time SMS queue status and cloud-synced digital health records.
\end{itemize}

\section{Idea Organization, Screening \& Prioritization}

\subsection{Affinity Diagramming}
Unstructured collections of ideas (hundreds of sticky notes) are clustered bottom-up into natural thematic groupings without predefined rigid labels.

\subsection{Weighted Idea Screening Matrix}
To evaluate competing concepts objectively against multi-dimensional criteria, teams apply weighted mathematical scoring:

\begin{keyequation}[Screening Matrix Formulation]
The total weighted score $T_i$ for idea $i$ across $n$ evaluation criteria is:
\begin{equation}
T_i = \sum_{j=1}^n \left( w_j \times s_{ij} \right) \quad \text{where} \quad \sum_{j=1}^n w_j = 1.0
\end{equation}
$w_j$ is the normalized importance weight of criterion $j$, and $s_{ij} \in [1, 5]$ is the rating of idea $i$ on criterion $j$.
\end{keyequation}

\begin{example}[Scoring Matrix Table]
\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.2}
\begin{tabularx}{\linewidth}{X c c c c}
\toprule
\textbf{Idea Candidate} & \textbf{Desirability ($w=0.5$)} & \textbf{Feasibility ($w=0.3$)} & \textbf{Viability ($w=0.2$)} & \textbf{Total Score ($T_i$)} \\
\midrule
\textbf{Concept A (AI Drone)} & $5$ & $2$ & $3$ & $(0.5\times 5)+(0.3\times 2)+(0.2\times 3) = \mathbf{3.7}$ \\
\textbf{Concept B (SMS Service)} & $4$ & $5$ & $4$ & $(0.5\times 4)+(0.3\times 5)+(0.2\times 4) = \mathbf{4.3}$ \\
\textbf{Concept C (Kiosk)} & $3$ & $4$ & $4$ & $(0.5\times 3)+(0.3\times 4)+(0.2\times 4) = \mathbf{3.5}$ \\
\bottomrule
\end{tabularx}
\caption{Weighted Matrix Evaluation indicating Concept B as the top candidate.}
\end{table}
\end{example}

\subsection{The Impact--Effort 2$\times$2 Grid}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{High Impact, Low Effort (Quick Wins):} High-priority candidates to implement immediately for fast validated return.
    \item \textbf{High Impact, High Effort (Major Projects):} Core strategic bets; require rigorous architectural planning and staged prototyping.
    \item \textbf{Low Impact, Low Effort (Fill-Ins):} Minor optimizations to tackle only when surplus time permits.
    \item \textbf{Low Impact, High Effort (Money Pits / Thankless Tasks):} Ideas to discard immediately.
\end{itemize}

\section{Unit 3 Self-Assessment Test}

\begin{chaptertest}[Ideation and Creative Problem Solving]
\textbf{Time Allowed: 30 Minutes \hfill Maximum Marks: 25}

\vspace{0.4cm}
\noindent\textbf{Part A: Conceptual Multiple Choice (5 $\times$ 1 = 5 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item What creative dimension measures the total volume of ideas produced?
    \item What does the ``6-3-5'' stand for in the Brainwriting technique?
    \item In SCAMPER, replacing plastic packaging with biodegradable mycelium is which operator?
    \item In an Impact-Effort matrix, what are High Impact + Low Effort ideas called?
    \item What is the main danger of production blocking in verbal brainstorming?
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part B: Short Calculation \& Method Questions (2 $\times$ 5 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{5}
    \item A team evaluates an IoT Water Purifier with weights: Desirability ($w=0.4$), Feasibility ($w=0.4$), Viability ($w=0.2$). The idea scores $4$ on Desirability, $3$ on Feasibility, and $5$ on Viability. Compute the total weighted score.
    \item Explain the 7 operators of SCAMPER with one original software/hardware example for each.
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part C: Creative Inversion Scenario (1 $\times$ 10 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{7}
    \item Use the \textbf{Reverse Thinking (Inversion)} methodology to tackle: *``How to reduce student dropout rates in online engineering courses.''* Formulate 4 worst-case ideas and invert them into 4 actionable design features.
\end{enumerate}
\end{chaptertest}

\begin{solutionbox}[Step-by-Step Unit Test Solutions]
\textbf{Part A Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item Fluency.
    \item 6 participants, 3 ideas per sheet, 5 minutes per round.
    \item Substitute (S).
    \item Quick Wins.
    \item Extroverts dominate while others forget or self-censor their ideas while waiting.
\end{enumerate}

\textbf{Part B Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{5}
    \item \textbf{Matrix Score Calculation:}
    $$T = (0.4 \times 4) + (0.4 \times 3) + (0.2 \times 5) = 1.6 + 1.2 + 1.0 = \mathbf{3.8} \text{ out of } 5.0$$
    \item \textbf{SCAMPER Summary:} S (Substitute material), C (Combine features), A (Adapt from biology/other field), M (Modify/Magnify touch targets), P (Put sensor to new use), E (Eliminate login screens), R (Reverse/Rearrange checkout order).
\end{enumerate}

\textbf{Part C Solution:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{7}
    \item \textbf{Reverse Thinking Inversion for Online Course Dropouts:}
    \begin{enumerate}[label=(\roman*)]
        \item *Worst 1:* Make lectures 3-hour unbroken monologues with no interaction. $\rightarrow$ **Inversion:** Micro-learning 7-minute chunked modules with active code quizzes.
        \item *Worst 2:* Hide student progress so they never know how much is left. $\rightarrow$ **Inversion:** Gamified visual progress bars and milestone completion badges.
        \item *Worst 3:* Offer zero feedback when a student gets stuck on an assignment. $\rightarrow$ **Inversion:** Integrated 24/7 peer debugging lounge and automated hint engine.
        \item *Worst 4:* Isolate students so they feel completely alone. $\rightarrow$ **Inversion:** Virtual study cohorts and collaborative pair-programming rooms.
    \end{enumerate}
\end{enumerate}
\end{solutionbox}
"""

with open("INT335/chapters/chapter-03-ideation-and-creative-problem-solving.tex", "w", encoding="utf-8") as f:
    f.write(ch3)

print("Chapters 2 & 3 generated.")
