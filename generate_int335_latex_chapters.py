# -*- coding: utf-8 -*-
import os

ch1 = r"""\chapter{Foundations of Learning, Creativity and Design Thinking}
\label{chap:foundations_design_thinking}

\begin{tcolorbox}[enhanced, colback=boxnavybg, colframe=brandnavy, boxrule=1.2pt, arc=4pt, title={\Large\bfseries\sffamily Unit 1 Overview \& Learning Objectives}]
\sffamily\normalsize
This unit explores the cognitive science, historical roots, and foundational frameworks of Design Thinking. By the conclusion of this chapter, students will be able to:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt, topsep=3pt]
    \item Define Design Thinking as an iterative, human-centred methodology for resolving complex problems.
    \item Analyze the characteristics of \textbf{Wicked Problems} as formulated by Horst Rittel and Melvin Webber.
    \item Contrast \textbf{Desirability}, \textbf{Feasibility}, and \textbf{Viability} across the IDEO innovation framework.
    \item Understand cognitive dynamics: active retrieval, deliberate practice, focused vs. diffuse modes, and neuroplasticity.
    \item Apply experiential learning models (Kolb's Cycle, Bloom's Taxonomy, VARK) to structured problem-solving.
    \item Identify and overcome cognitive barriers including \textbf{Functional Fixedness} (Duncker's Candle Problem) and mental sets.
    \item Trace the chronological evolution of Design Thinking from the Bauhaus school (1919) to Stanford d.school (2005).
    \item Evaluate global case studies of design successes (OXO Good Grips, M-Pesa, Jaipur Foot) and commercial failures (Ford Edsel, Google Glass, Juicero).
\end{itemize}
\end{tcolorbox}

\section{Orientation: Human-Centred Problem Solving}

Design Thinking is an iterative, human-centred paradigm for tackling ambiguous, multi-dimensional challenges. Rather than starting from a predetermined technical artifact or business mandate, Design Thinking anchors the entire problem-solving trajectory in the lived experiences, constraints, and unmet needs of human beings.

\begin{definition}[Design Thinking]
A non-linear, evidence-driven methodology that integrates human empathy, problem reframing, divergent-convergent ideation, rapid prototyping, and empirical user testing to create solutions that are desirable, feasible, and viable.
\end{definition}

\subsection{Core Axioms \& Governing Principles}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Human Primacy:} Design begins with human needs and behavioral observation, not technology looking for an application.
    \item \textbf{Wicked Problems:} First articulated by social scientists \textbf{Horst Rittel and Melvin Webber (1973)}, wicked problems are complex systemic issues (e.g., poverty, healthcare accessibility, traffic congestion) characterized by:
    \begin{itemize}
        \item No definitive or final problem formulation.
        \item Interconnected causal networks where solving one aspect may create new challenges.
        \item No immediate or ultimate test of a solution; solutions are ``better or worse'' rather than strictly ``true or false''.
    \end{itemize}
    \item \textbf{Action-Based Epistemology:} Knowledge is developed through tangible action. Building rough prototypes generates critical feedback that pure analytical contemplation cannot reveal.
    \item \textbf{Failure as Evidence:} In design practice, early failure is treated as an inexpensive experimental probe that invalidates incorrect hypotheses early in the lifecycle.
\end{itemize}

\begin{keyequation}[The Three Lenses of Innovation (IDEO)]
A resilient and sustainable innovation sits at the intersection of three fundamental criteria:
\begin{equation}
\text{Innovation} = \text{Desirability (Human)} \;\cap\; \text{Feasibility (Technical)} \;\cap\; \text{Viability (Business)}
\end{equation}
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Desirability:} Do people genuinely need, want, and value this solution?
    \item \textbf{Feasibility:} Can we realistically build, operate, and maintain this using available technology and engineering capability?
    \item \textbf{Viability:} Can the organization sustain this economically and operationally over time?
\end{itemize}
\end{keyequation}

\section{Cognitive Science: Learning \& Brain Processing Dynamics}

Design Thinking leverages human cognitive processing. Understanding how the brain encodes information, alternates attention modes, and forms mental associations is vital for creative mastery.

\subsection{Memory Networks \& Deliberate Practice}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Working Memory vs. Long-Term Memory:} Working memory temporarily holds $4 \pm 1$ informational chunks under active attention. Long-term memory stores complex associative schemas. Effective design minimizes extraneous cognitive load by externalizing memory into visual diagrams and physical mockups.
    \item \textbf{Encoding \& Active Retrieval:} Passive review creates the illusion of mastery; active recall physically strengthens synaptic connections, ensuring durable knowledge transfer.
    \item \textbf{Neuroplasticity:} Neural pathways physically rewire through repeated deliberate practice, establishing that creative problem solving is a trainable discipline rather than a fixed genetic trait.
\end{itemize}

\subsection{Focused vs. Diffuse Thinking Modes}
Modern cognitive neuroscience (popularized by Dr. Barbara Oakley) identifies two complementary operational modes of the human brain:

\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{3.2cm}X X}
\toprule
\textbf{Dimension} & \textbf{Focused Mode} & \textbf{Diffuse Mode} \\
\midrule
\textbf{Brain State} & Highly focused, analytical concentration. & Relaxed resting-state default mode network. \\
\textbf{Function} & Sequential reasoning, rule execution, error checking. & Subconscious incubation, broad association, big-picture synthesis. \\
\textbf{Design Role} & Dimensioning prototypes, coding logic, verifying constraints. & Gaining unexpected creative insights during walks, breaks, or sleep. \\
\textbf{Limitation} & Can cause cognitive fixation or tunnel vision. & Requires prior focused study; cannot calculate precise formulas. \\
\bottomrule
\end{tabularx}
\caption{Comparison of Focused and Diffuse Cognitive Modes.}
\end{table}

\section{Pedagogical Frameworks \& Cognitive Blocks}

\subsection{Kolb's Experiential Learning Cycle}
Educational theorist David Kolb proposed that comprehensive learning occurs through a 4-stage cyclical continuum:
\begin{equation}
\text{Concrete Experience} \longrightarrow \text{Reflective Observation} \longrightarrow \text{Abstract Conceptualization} \longrightarrow \text{Active Experimentation}
\end{equation}
In Design Thinking, building and testing prototypes provides the *Concrete Experience*, team debriefs supply *Reflective Observation*, synthesizing insights forms *Abstract Conceptualization*, and iterating designs drives *Active Experimentation*.

\subsection{Bloom's Revised Taxonomy}
Bloom's hierarchical taxonomy categorizes cognitive objectives from foundational to advanced:
\begin{center}
\textbf{Remember} $\;\rightarrow\;$ \textbf{Understand} $\;\rightarrow\;$ \textbf{Apply} $\;\rightarrow\;$ \textbf{Analyze} $\;\rightarrow\;$ \textbf{Evaluate} $\;\rightarrow\;$ \textbf{Create}
\end{center}
Design Thinking operates predominantly at the highest tier---\textbf{Create}---which requires students to synthesize, evaluate, and generate novel value.

\subsection{VARK Modalities}
The VARK framework identifies four sensory modalities for processing information:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Visual (V):} Diagrams, spatial maps, color coding, charts.
    \item \textbf{Aural (A):} Spoken discussions, audio debriefs, collaborative dialogue.
    \item \textbf{Read/Write (R):} Textual synthesis, lists, problem briefs, documented specifications.
    \item \textbf{Kinesthetic (K):} Tactile paper models, physical role-playing, hands-on assembly.
\end{itemize}

\subsection{Functional Fixedness \& Cognitive Biases}
\begin{definition}[Functional Fixedness]
A cognitive bias first documented experimentally by \textbf{Karl Duncker (1945)} in which an individual is mentally constrained to perceive an object solely in terms of its customary, traditional function.
\end{definition}

\begin{example}[Duncker's Candle Problem (1945)]
Participants are provided a candle, a box of thumb-tacks, and a book of matches, and tasked with mounting the candle onto a cork wall so wax does not drip onto the table below. 
\begin{itemize}[leftmargin=1.2em]
    \item \textbf{The Fixation Trap:} Most participants attempt to tack the candle directly to the wall or melt its base against the wall.
    \item \textbf{The Creative Resolution:} Empty the box of tacks, tack the empty cardboard box to the wall as a shelf, and place the candle inside it. Overcoming functional fixedness requires seeing the box as a *platform* rather than merely a *container*.
\end{itemize}
\end{example}

\begin{examtip}[Countermeasures Against Cognitive Blocks]
To overcome mental sets and functional fixedness in engineering examinations and design reviews:
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{First-Principles Deconstruction:} Break every tool or system down into its basic physical properties (e.g., surface, mass, volume) rather than its named identity.
    \item \textbf{Assumption Reversal:} Explicitly list every assumed rule and ask: ``What if the opposite were true?''
    \item \textbf{Analogy Transfer:} Borrow mechanisms from unrelated domains (e.g., studying burrs on dog fur to invent Velcro).
\end{enumerate}
\end{examtip}

\section{Creativity, Invention, and Innovation}

These three related terms have distinct operational definitions in engineering and business:
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Creativity:} The psychological and cognitive capacity to conceive ideas that are both novel and contextually appropriate.
    \item \textbf{Invention:} The physical or algorithmic creation of a technically new device, composition, or process (frequently patentable).
    \item \textbf{Innovation:} The successful implementation, social adoption, and economic scaling of a new solution that creates measurable real-world impact.
\end{itemize}

\begin{equation}
\text{Innovation} = \text{Invention} \;\times\; \text{Commercial / Social Adoption}
\end{equation}

\section{Historical Evolution \& Core Process Models}

\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{1919 --- Bauhaus (Germany):} Walter Gropius unites fine art and industrial manufacturing, establishing the principle that form follows human function.
    \item \textbf{1969 --- Herbert Simon:} Publishes *The Sciences of the Artificial*, defining design as the transformation of existing conditions into preferred ones.
    \item \textbf{1973 --- Horst Rittel \& Melvin Webber:} Define the characteristics of Wicked Problems in social policy.
    \item \textbf{1987 --- Peter Rowe:} Formally introduces the term *Design Thinking* in his architectural treatise.
    \item \textbf{1991 --- IDEO Formation:} David Kelley, Bill Moggridge, and Mike Nuttall establish IDEO, commercializing Human-Centred Design.
    \item \textbf{2005 --- Stanford d.school:} Founded by David Kelley to teach multidisciplinary innovation.
\end{itemize}

\subsection{Stanford d.school 5-Stage Framework}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Empathize:} Immerse in the user's environment; observe behaviors and conduct open interviews.
    \item \textbf{Define:} Synthesize research into an actionable \textbf{Point-of-View (POV)} statement ($User + Need + Insight$).
    \item \textbf{Ideate:} Diverge broadly to generate innovative possibilities without premature judgment.
    \item \textbf{Prototype:} Construct rapid, low-fidelity tangible models to explore specific questions.
    \item \textbf{Test:} Put prototypes in front of real users in real context to gather empirical behavioral evidence.
\end{enumerate}

\subsection{IDEO 3I Framework}
\textbf{Inspiration} (problem research and immersion) $\;\rightarrow\;$ \textbf{Ideation} (synthesis, brainstorming, prototyping) $\;\rightarrow\;$ \textbf{Implementation} (piloting, engineering, scaling).

\section{Landmark Global Case Studies}

\begin{example}[Design Successes]
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{OXO Good Grips (1990):} Sam Farber observed his arthritic wife struggling with standard metal potato peelers. By collaborating with Smart Design, they engineered a thick, non-slip, ribbed rubber handle. The resulting universal design benefited not only arthritis patients but all consumers, capturing market leadership.
    \item \textbf{M-Pesa (Kenya, 2007):} Safaricom identified that millions of Kenyans lacked bank accounts but owned basic mobile phones. They built an SMS-based digital wallet supported by corner-shop retail agents for physical cash-in/cash-out. It revolutionized African financial inclusion.
    \item \textbf{Jaipur Foot (India):} Developed by Dr. P.K. Sethi and master craftsman Ram Chander Sharma, this low-cost, waterproof prosthetic limb allows amputees to walk barefoot, squat, climb trees, and work in wet agricultural fields at a fraction of Western prosthetic costs.
\end{itemize}
\end{example}

\begin{example}[Design Failures \& Critical Lessons]
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Ford Edsel (1957--1960):} Flawed market segmentation, overpromoted styling that alienated buyers, and poor build quality resulted in a \$350M failure.
    \item \textbf{Google Glass Consumer Edition (2013):} Ignored social empathy; public fears of unauthorized recording, nerd-stereotyping (``Glassholes''), and lack of clear everyday utility led to consumer withdrawal.
    \item \textbf{Juicero (2017):} A \$700 Wi-Fi-connected juice press collapsed after reporters proved that the proprietary organic fruit packets could be squeezed just as quickly and effectively by bare human hands. Over-engineering a non-existent user need is fatal.
\end{itemize}
\end{example}

\section{Unit 1 Self-Assessment Test}

\begin{chaptertest}[Foundations of Learning, Creativity \& Design Thinking]
\textbf{Time Allowed: 30 Minutes \hfill Maximum Marks: 25}

\vspace{0.4cm}
\noindent\textbf{Part A: Conceptual Multiple Choice (5 $\times$ 1 = 5 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item Who formulated the concept of ``Wicked Problems'' in 1973?
    \item Which brain mode is responsible for unconscious incubation and big-picture synthesis?
    \item In Duncker's candle problem, what cognitive bias prevents seeing the tack box as a shelf?
    \item Which three lenses form IDEO's innovation sweet spot?
    \item In what year was the Stanford d.school founded?
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part B: Short Analytical Questions (2 $\times$ 5 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{5}
    \item Differentiate between \textbf{Divergent} and \textbf{Convergent} thinking with respect to purpose, cognitive behavior, and typical outputs.
    \item Explain the four stages of Kolb's Experiential Learning Cycle and map them to the Design Thinking process.
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part C: Comprehensive Case Study Analysis (1 $\times$ 10 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{7}
    \item Analyze the commercial failure of \textbf{Juicero} using IDEO's Three Lenses of Innovation (Desirability, Feasibility, Viability). Detail how proper empathy research and low-fidelity prototyping could have prevented this multi-million dollar failure.
\end{enumerate}
\end{chaptertest}

\begin{solutionbox}[Step-by-Step Unit Test Solutions]
\textbf{Part A Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item Horst Rittel and Melvin Webber.
    \item Diffuse Mode.
    \item Functional Fixedness.
    \item Desirability, Feasibility, and Viability.
    \item 2005.
\end{enumerate}

\textbf{Part B Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{5}
    \item \textbf{Divergent vs. Convergent Thinking:}
    \begin{itemize}
        \item *Divergent Thinking:* Purpose is to expand the solution space; defers judgment, embraces ambiguity, focuses on fluency and flexibility; output is a wide volume of unvetted possibilities.
        \item *Convergent Thinking:* Purpose is to narrow down and decide; applies constraints, critical analysis, and prioritization matrices; output is a defensible, ranked shortlist or single prototype candidate.
    \end{itemize}
    \item \textbf{Kolb's Cycle Mapped to Design Thinking:}
    \begin{itemize}
        \item *Concrete Experience:* User testing or field immersion.
        \item *Reflective Observation:* Debriefing and analyzing user reactions.
        \item *Abstract Conceptualization:* Developing insights and POV problem definitions.
        \item *Active Experimentation:* Building and modifying iterative prototypes.
    \end{itemize}
\end{enumerate}

\textbf{Part C Solution:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{7}
    \item \textbf{Juicero Failure Analysis via IDEO's Three Lenses:}
    \begin{itemize}
        \item *Feasibility (Passed):* Highly engineered aluminum press with custom motors, optical QR scanner, and Wi-Fi chip. Technically viable, but over-engineered.
        \item *Viability (Failed):* Required expensive precision manufacturing (\$700 retail price) and recurring proprietary packet subscription, creating unsustainable unit economics.
        \item *Desirability (Catastrophically Failed):* Users did not have a real problem that required a motorized 4-ton press. Hand-squeezing delivered juice in the exact same time without plugging in an appliance.
        \item *Prototyping Remediation:* A simple paper or manual low-fidelity concierge test (handing users packets and observing them) would have immediately revealed that human hands exert sufficient force, invalidating the entire product premise for zero engineering cost.
    \end{itemize}
\end{enumerate}
\end{solutionbox}
"""

with open("INT335/chapters/chapter-01-foundations-of-learning-creativity-and-design-thinking.tex", "w", encoding="utf-8") as f:
    f.write(ch1)

print("Chapter 1 generated.")
