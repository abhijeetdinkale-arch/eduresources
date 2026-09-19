# -*- coding: utf-8 -*-
import os

# CHAPTER 4
ch4 = r"""\chapter{Product Design and Prototyping}
\label{chap:product_design_prototyping}

\begin{tcolorbox}[enhanced, colback=boxnavybg, colframe=brandnavy, boxrule=1.2pt, arc=4pt, title={\Large\bfseries\sffamily Unit 4 Overview \& Learning Objectives}]
\sffamily\normalsize
This unit covers the philosophy, techniques, and toolkits for transforming abstract ideas into testable, tangible artifacts. By the end of this chapter, students will be able to:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt, topsep=3pt]
    \item Understand the core prototyping philosophy: *``Build to think, test to learn''*.
    \item Contrast the speed, cost, and testing goals of \textbf{Low-Fidelity} vs. \textbf{High-Fidelity} prototypes.
    \item Execute realistic \textbf{Paper Prototyping} tests with defined participant, computer, and observer roles.
    \item Create narrative \textbf{Storyboards} visualizing user touchpoints and emotional context over time.
    \item Apply UI/UX \textbf{Wireframing Conventions} (grayscale, visual hierarchy, radio buttons vs. checkboxes, screen states).
    \item Map structured \textbf{User Flows} using standard flowchart symbols (ovals, rectangles, diamonds, arrows).
    \item Define and construct \textbf{Minimum Viable Products (MVPs)} including Landing Page, Concierge, and Wizard of Oz models.
\end{itemize}
\end{tcolorbox}

\section{Prototyping Philosophy \& Rapid Learning}

A prototype is a tangible, testable simulation or experimental artifact created to answer specific hypotheses and discover unknown unknowns before full engineering investment.

\begin{definition}[The Prototyping Mindset]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Build to Think:} Tangible models reveal logical inconsistencies and structural gaps that abstract mental reasoning misses.
    \item \textbf{Test the Riskiest Assumptions First:} Never spend weeks polishing visual details if the fundamental user value proposition remains unvalidated.
    \item \textbf{Separate Ego from the Artifact:} Low-fidelity materials ensure team members and users feel comfortable pointing out flaws and suggesting radical revisions.
\end{itemize}
\end{definition}

\section{Prototype Fidelity: Trade-Offs \& Decision Matrix}

\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{2.8cm}X X}
\toprule
\textbf{Dimension} & \textbf{Low-Fidelity (Lo-Fi)} & \textbf{High-Fidelity (Hi-Fi)} \\
\midrule
\textbf{Materials} & Paper, cardboard, sticky notes, block wireframes. & Clickable Figma mockups, functional frontend code, 3D prints. \\
\textbf{Creation Time} & Minutes to hours; negligible monetary cost. & Days to weeks; requires specialized design/code skills. \\
\textbf{Primary Goal} & Validate mental models, workflows, information architecture. & Validate micro-interactions, visual hierarchy, timing, and aesthetics. \\
\textbf{Feedback Type} & Broad, structural, honest conceptual feedback. & Fine-grained feedback on typography, colors, and button placement. \\
\textbf{Risk} & Cannot test microsecond interaction or responsive gestures. & Risk of sunk-cost fallacy and premature attachment to flawed ideas. \\
\bottomrule
\end{tabularx}
\caption{Comparative Analysis of Prototype Fidelity Levels.}
\end{table}

\section{Paper Prototyping \& Storyboarding}

\subsection{Paper Prototyping Mechanics}
Paper prototyping uses physical paper cutouts, sticky notes, and acetate sheets to simulate a digital application.
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{The User:} Interacts with the paper screen by touching, pointing, or writing with a pen.
    \item \textbf{The ``Computer'' (Facilitator):} Silently swaps screens, drops popup sticky notes, and slides lists in response to user actions.
    \item \textbf{The Observer:} Records user hesitation, misclicks, and verbal confusion without offering assistance.
\end{itemize}

\subsection{Interaction Storyboarding}
Storyboards adapt comic-strip visual narratives to show how a user experiences a product within their physical and social environment over time.
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Panel 1 (Trigger / Problem):} User in context experiencing friction (e.g., student rushing to print an assignment before class).
    \item \textbf{Panel 2 (Discovery / Entry):} User encounters the solution (e.g., spots a cloud-connected campus printer kiosk).
    \item \textbf{Panel 3 (Core Action):} User interacts with the core feature (e.g., scans phone QR code to instantly release print queue).
    \item \textbf{Panel 4 (Outcome / Resolution):} User achieves their goal with emotional relief (e.g., submits assignment on time).
\end{itemize}

\section{Wireframing Conventions \& UI Rules}

A wireframe is a grayscale architectural blueprint that defines content hierarchy, layout geometry, and UI controls before applying visual styling.

\begin{keyequation}[Wireframing Best Practices]
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Grayscale Restraint:} Use only black, white, and gray shades to keep feedback focused on layout and functionality rather than color debates.
    \item \textbf{Control Semantics:}
    \begin{itemize}
        \item \textbf{Radio Buttons ($\odot$):} Exactly ONE selection from a mutually exclusive list (e.g., Gender: Male $\odot$ Female $\bigcirc$).
        \item \textbf{Checkboxes ($\boxtimes$):} Zero, one, or MULTIPLE independent selections (e.g., Toppings: Cheese $\boxtimes$ Olives $\boxtimes$).
        \item \textbf{Toggle Switch:} Immediate binary state change (e.g., Airplane Mode: ON/OFF).
    \end{itemize}
    \item \textbf{Image Placeholders:} A rectangle with diagonal crossing lines ($[\boxtimes]$) universally indicates an image or video placeholder.
    \item \textbf{State Completeness:} Wireframes must specify Default, Loading, Empty, Error, and Success states.
\end{itemize}
\end{keyequation}

\section{User Flows \& Flowchart Conventions}

A **User Flow** tracks the step-by-step navigational sequence required to accomplish a specific user goal.
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Oval / Pill (Terminator):} Indicates the Start or End of a task (e.g., ``Start: App Launch'', ``End: Order Placed'').
    \item \textbf{Rectangle (Process / Screen):} Represents a screen, system action, or user step (e.g., ``Enter Shipping Details'').
    \item \textbf{Diamond (Decision Point):} Represents a conditional branch (e.g., ``Is User Logged In?'' $\rightarrow$ Yes / No).
    \item \textbf{Arrow:} Indicates the directional flow of user movement.
\end{itemize}

\section{The Minimum Viable Product (MVP)}

\begin{definition}[Minimum Viable Product (Eric Ries)]
That version of a new product which allows a team to collect the maximum amount of validated learning about customers with the least effort.
\end{definition}

\begin{keyequation}[The Core MVP Principle]
An MVP is NOT an incomplete, half-built product (e.g., a car chassis without wheels). An MVP is the simplest coherent product that delivers \textbf{complete end-to-end functional value} (e.g., a skateboard that solves personal transport, followed iteratively by a scooter, bicycle, motorcycle, and car).
\end{keyequation}

\subsection{Types of Prototyping MVPs}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Landing Page MVP:} A single web page detailing the core value proposition with a call-to-action (``Pre-order / Join Waitlist'') to empirically measure market demand before writing code.
    \item \textbf{Concierge MVP:} Delivering the service entirely manually and personally to early adopters to directly observe friction and expectations before building automated software.
    \item \textbf{Wizard of Oz MVP:} The front-end appears fully automated, but behind the scenes, humans perform all the heavy backend operations manually (e.g., Zappos founder Nick Swinmurn taking shoe orders online and physically purchasing them from local stores).
\end{enumerate}

\section{Unit 4 Self-Assessment Test}

\begin{chaptertest}[Product Design and Prototyping]
\textbf{Time Allowed: 30 Minutes \hfill Maximum Marks: 25}

\vspace{0.4cm}
\noindent\textbf{Part A: Conceptual Multiple Choice (5 $\times$ 1 = 5 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item What is the main goal of low-fidelity paper prototyping?
    \item In a flowchart, which geometric shape represents a conditional decision point?
    \item Which UI control should be used when a user can select multiple toppings on a pizza order?
    \item What is a Wizard of Oz prototype?
    \item Why are early wireframes strictly designed in grayscale?
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part B: Short Analytical Questions (2 $\times$ 5 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{5}
    \item Contrast \textbf{Low-Fidelity} and \textbf{High-Fidelity} prototypes across four dimensions: creation time, cost, testing objective, and user feedback quality.
    \item Explain the three roles in a paper prototyping test session (User, Facilitator/``Computer'', Observer).
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part C: Practical User Flow Design (1 $\times$ 10 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{7}
    \item Design a complete User Flow for a **Campus Bike Sharing App**. Map both the *Happy Path* (successful unlock and payment) and at least two *Alternate/Error Paths* (e.g., Bike Battery Low, Payment Gateway Failure) using formal flowchart symbols.
\end{enumerate}
\end{chaptertest}

\begin{solutionbox}[Step-by-Step Unit Test Solutions]
\textbf{Part A Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item Rapid, low-cost exploration of structural layout, mental models, and navigational flows.
    \item Diamond shape.
    \item Checkboxes ($\boxtimes$).
    \item A prototype that appears fully automated on the frontend but is operated manually by humans in the backend.
    \item To prevent premature debates on color/aesthetics and keep attention focused on layout and hierarchy.
\end{enumerate}

\textbf{Part B Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{5}
    \item \textbf{Lo-Fi vs. Hi-Fi Comparison:}
    \begin{itemize}
        \item *Time \& Cost:* Lo-Fi is crafted in minutes at zero cost; Hi-Fi takes days/weeks with significant resource investment.
        \item *Testing Objective:* Lo-Fi validates information architecture and user flows; Hi-Fi validates visual design, micro-interactions, and usability metrics.
        \item *Feedback Quality:* Lo-Fi elicits broad conceptual critique; Hi-Fi elicits detailed aesthetic and micro-interaction feedback.
    \end{itemize}
    \item \textbf{Paper Prototyping Roles:}
    \begin{itemize}
        \item *User:* Attempts the realistic task by pointing and tapping paper cutouts.
        \item *Computer (Facilitator):* Manipulates paper states, screens, and dialogs dynamically without speaking.
        \item *Observer:* Silently records time, hesitation, errors, and think-aloud statements.
    \end{itemize}
\end{enumerate}

\textbf{Part C Solution:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{7}
    \item \textbf{Campus Bike Sharing User Flow:}
    \begin{itemize}
        \item *Terminator:* Start $\rightarrow$ [Scan Bike QR Code].
        \item *Decision 1:* [Is QR Code Valid?] $\rightarrow$ No $\rightarrow$ [Show ``Invalid QR'' + Option to enter Bike ID manually].
        \item *Decision 2:* [Is Bike Battery $\ge 20\%$?] $\rightarrow$ No $\rightarrow$ [Display ``Battery Low, please select nearby Bike B-12''].
        \item *Process:* [Unlock Lock Mechanism] $\rightarrow$ [Ride in Progress Timer] $\rightarrow$ [Dock at Destination Station].
        \item *Decision 3:* [Payment Successful?] $\rightarrow$ No $\rightarrow$ [Trigger Retry / Alternative UPI Gateway] $\rightarrow$ Yes $\rightarrow$ [Show Receipt] $\rightarrow$ Terminator (End).
    \end{itemize}
\end{enumerate}
\end{solutionbox}
"""

with open("INT335/chapters/chapter-04-product-design-and-prototyping.tex", "w", encoding="utf-8") as f:
    f.write(ch4)

# CHAPTER 5
ch5 = r"""\chapter{Testing, Validation and Customer Experience}
\label{chap:testing_validation_cx}

\begin{tcolorbox}[enhanced, colback=boxnavybg, colframe=brandnavy, boxrule=1.2pt, arc=4pt, title={\Large\bfseries\sffamily Unit 5 Overview \& Learning Objectives}]
\sffamily\normalsize
This unit covers the scientific execution of user testing, metrics of usability, customer experience mapping, and digital accessibility standards. By the conclusion of this chapter, students will be able to:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt, topsep=3pt]
    \item Differentiate between \textbf{Usability Testing} and \textbf{Design Validation}.
    \item Conduct neutral, unbiased testing using the \textbf{``Show, Don't Tell''} approach and \textbf{Think-Aloud Protocol}.
    \item Construct realistic, goal-oriented \textbf{Task Scenarios} without prescribing interface steps.
    \item Capture and categorize testing data using the 4-quadrant \textbf{Feedback Capture Matrix}.
    \item Compare \textbf{Usability (UI/UX)} with holistic \textbf{Customer Experience (CX)}.
    \item Construct comprehensive \textbf{Customer Journey Maps} tracking actions, emotions, touchpoints, and pain points.
    \item Classify human, digital, and physical \textbf{Touchpoints}.
    \item Apply the WCAG \textbf{POUR} principles (Perceivable, Operable, Understandable, Robust) and contrast ratio standards.
\end{itemize}
\end{tcolorbox}

\section{Orientation: Testing as an Empirical Learning Loop}

Testing is the fifth stage of Design Thinking. Rather than serving as a final rubber-stamp validation, testing is an iterative inquiry that puts prototypes in front of real users to uncover behavioral breakdowns and test underlying hypotheses.

\begin{definition}[Usability Testing vs. Design Validation]
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Usability Testing:} Evaluates whether users can interact with the interface effectively, efficiently, and with satisfaction (*``Did we build the product correctly?''*).
    \item \textbf{Design Validation:} Evaluates whether the product solves the real, validated core human need (*``Did we build the correct product?''*).
\end{itemize}
\end{definition}

\section{Principles of Neutral User Testing}

\begin{keyequation}[The ``Show, Don't Tell'' Doctrine]
Never explain, defend, or pitch your prototype to a user during a testing session. Place the prototype in front of the participant, present a realistic task scenario, and observe their natural behavior and cognitive struggle.
\end{keyequation}

\subsection{Facilitation Rules \& Bias Control}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Reassure the Participant:} State explicitly: *``We are testing the product, not you. There are no wrong answers; every error helps us fix the design.''*
    \item \textbf{Non-Leading Probing:} If a user pauses or asks for help, respond neutrally: *``What would you expect to happen next?''* or *``What are you looking for right now?''*
    \item \textbf{Think-Aloud Protocol:} Instruct participants to continuously verbalize their thoughts, doubts, expectations, and visual impressions as they navigate.
    \item \textbf{Separate Observation from Interpretation:}
    \begin{itemize}
        \item *Observation (Fact):* User tapped the ``Support'' icon 4 times.
        \item *Interpretation (Hypothesis):* User cannot find the refund policy under ``Settings''.
    \end{itemize}
\end{itemize}

\subsection{Constructing Task Scenarios}
\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{3.2cm}X X}
\toprule
\textbf{Attribute} & \textbf{Poor Task Scenario (Leading)} & \textbf{Strong Task Scenario (Goal-Oriented)} \\
\midrule
\textbf{Wording} & ``Click the red filter button, select 'Price Low to High', and tap Apply.'' & ``You want to buy a pair of running shoes under ₹2,000 for Friday's race. Complete the purchase.'' \\
\textbf{Focus} & Tests mechanical obedience to instructions. & Tests discoverability, mental models, and information architecture. \\
\textbf{Prescription} & Gives away UI button names and sequence. & Provides realistic context, constraints, and end goal only. \\
\bottomrule
\end{tabularx}
\caption{Formulating Effective Usability Testing Scenarios.}
\end{table}

\section{The Feedback Capture Matrix}

During and immediately following testing sessions, raw observations are sorted into a 4-quadrant grid:
\begin{center}
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\textbf{LIKES (+)} & \textbf{WISHES ($\Delta$)} \\
\textit{Things users appreciated, found intuitive, or praised.} & \textit{Constructive critiques, friction points, unmet expectations.} \\
\textit{e.g., Instant SMS order confirmation receipt.} & \textit{e.g., Wish there was an option to edit address at payment screen.} \\
\hline
\textbf{QUESTIONS (?)} & \textbf{IDEAS (!)} \\
\textit{Confusions, uncertainties, and queries raised by users.} & \textit{New feature concepts or modifications sparked during testing.} \\
\textit{e.g., Is weekend delivery included in standard shipping?} & \textit{e.g., Enable recurring monthly auto-reorder with one tap.} \\
\hline
\end{tabularx}
\end{center}

\section{Customer Experience (CX) \& Journey Mapping}

\subsection{Usability vs. Customer Experience (CX)}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Usability:} Focuses on task performance on a specific product interface (e.g., speed of booking a doctor appointment on an app).
    \item \textbf{Customer Experience (CX):} The holistic, cumulative perception across the entire lifecycle and every touchpoint (e.g., app booking $\rightarrow$ clinic parking $\rightarrow$ reception queue $\rightarrow$ doctor interaction $\rightarrow$ billing clarity $\rightarrow$ post-visit medication delivery).
\end{itemize}

\subsection{Customer Journey Map Architecture}
A Customer Journey Map visualizes a user's experience over time across sequential stages:
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Journey Stages:} Awareness $\rightarrow$ Consideration $\rightarrow$ Purchase $\rightarrow$ Onboarding $\rightarrow$ Usage $\rightarrow$ Support $\rightarrow$ Offboarding.
    \item \textbf{Horizontal Map Layers:}
    \begin{itemize}
        \item \textbf{User Actions:} What the customer physically does at each step.
        \item \textbf{Thoughts \& Emotions:} Emotional highs and lows plotted as a sentiment curve ($+2$ delight to $-2$ frustration).
        \item \textbf{Touchpoints \& Channels:} The interface medium used (Human, Digital, Physical).
        \item \textbf{Pain Points:} Breakdowns, delays, hidden costs, or confusing transitions.
        \item \textbf{Opportunities:} Actionable engineering and design interventions to eliminate pain points.
    \end{itemize}
\end{enumerate}

\section{Digital Accessibility: WCAG \& POUR Principles}

The Web Content Accessibility Guidelines (WCAG 2.1) require digital systems to satisfy four core principles:
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Perceivable (P):} Information and UI components must be presentable to users in ways they can perceive.
    \begin{itemize}
        \item Provide descriptive text alternatives (\texttt{alt} attributes) for non-text content.
        \item Provide captions and transcripts for multimedia.
        \item Maintain minimum color contrast ratio: **4.5:1** for standard body text, **3:1** for large text (Level AA).
    \end{itemize}
    \item \textbf{Operable (O):} UI components and navigation must be operable via keyboard-only access without requiring precise mouse gestures. No keyboard traps.
    \item \textbf{Understandable (U):} Information and UI operation must be predictable, clear, and error-tolerant. Provide inline validation and clear error correction instructions.
    \item \textbf{Robust (R):} Content must be interpretable reliably by a wide variety of user agents, including modern assistive screen readers (NVDA, VoiceOver, JAWS).
\end{enumerate}

\section{Unit 5 Self-Assessment Test}

\begin{chaptertest}[Testing, Validation and Customer Experience]
\textbf{Time Allowed: 30 Minutes \hfill Maximum Marks: 25}

\vspace{0.4cm}
\noindent\textbf{Part A: Conceptual Multiple Choice (5 $\times$ 1 = 5 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item What is the core rule of the ``Show, Don't Tell'' testing approach?
    \item Which quadrant of the Feedback Capture Matrix captures user confusion and queries?
    \item According to WCAG AA standards, what is the minimum color contrast ratio for normal text?
    \item What does the Think-Aloud Protocol require participants to do?
    \item Give one example of a Human touchpoint in an e-commerce shopping journey.
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part B: Short Analytical Questions (2 $\times$ 5 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{5}
    \item Differentiate between \textbf{Usability} and \textbf{Customer Experience (CX)} across scope, timeframe, and measurement metrics.
    \item Explain the 4 principles of WCAG \textbf{POUR} and describe one technical violation for each.
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part C: Usability Scenario Analysis (1 $\times$ 10 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{7}
    \item You are conducting a usability test for a new **Hospital Emergency Room Patient Intake Kiosk**.
    \begin{enumerate}[label=(\alph*)]
        \item Write one poor (leading) task scenario and rewrite it as an effective goal-oriented task scenario.
        \item Populate a 4-quadrant Feedback Capture Matrix with 4 realistic findings from testing this kiosk with stressed patients.
    \end{enumerate}
\end{enumerate}
\end{chaptertest}

\begin{solutionbox}[Step-by-Step Unit Test Solutions]
\textbf{Part A Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item Observe natural interaction without explaining, pitching, or defending the prototype.
    \item Questions (?) quadrant.
    \item 4.5:1.
    \item Verbalize internal thoughts, feelings, doubts, and expectations aloud during task execution.
    \item Customer support call agent or delivery delivery courier.
\end{enumerate}

\textbf{Part B Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{5}
    \item \textbf{Usability vs. CX Comparison:}
    \begin{itemize}
        \item *Scope:* Usability measures interface performance on a specific tool; CX measures the cumulative end-to-end journey across all digital, physical, and human channels.
        \item *Metrics:* Usability uses Task Success Rate, Time on Task, and Single Ease Question; CX uses Net Promoter Score (NPS), Customer Satisfaction (CSAT), and Retention Rate.
    \end{itemize}
    \item \textbf{POUR Violations:}
    \begin{itemize}
        \item *Perceivable Violation:* Light gray text on white background failing 4.5:1 contrast.
        \item *Operable Violation:* A modal popup that traps keyboard focus, preventing tab navigation.
        \item *Understandable Violation:* Cryptic error messages like ``Fatal exception 0x4B''.
        \item *Robust Violation:* Non-standard HTML tags that screen readers fail to parse.
    \end{itemize}
\end{enumerate}

\textbf{Part C Solution:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{7}
    \item \textbf{Hospital Kiosk Usability Analysis:}
    \begin{itemize}
        \item *(a) Task Scenario Comparison:*
        \begin{itemize}
            \item *Poor Task:* ``Click the red 'Emergency Check-in' button, type your national ID, and press confirm.''
            \item *Effective Task:* ``You are experiencing severe chest pain and arrived at the ER alone. Check yourself in so the triage nurse is notified immediately.''
        \end{itemize}
        \item *(b) Feedback Capture Matrix:*
        \begin{itemize}
            \item **Likes (+):** Large physical tactile emergency button instantly recognized.
            \item **Wishes ($\Delta$):** Patients wished they could scan their insurance QR code rather than typing long 16-digit policy numbers while in pain.
            \item **Questions (?):** Patients asked: ``Does this guarantee a doctor has seen my alert?''
            \item **Ideas (!):** Integrate biometric fingerprint scanner for instant one-touch medical history lookup.
        \end{itemize}
    \end{itemize}
\end{enumerate}
\end{solutionbox}
"""

with open("INT335/chapters/chapter-05-testing-validation-and-customer-experience.tex", "w", encoding="utf-8") as f:
    f.write(ch5)

# CHAPTER 6
ch6 = r"""\chapter{Innovation Project, Re-Design and Product Presentation}
\label{chap:innovation_redesign_presentation}

\begin{tcolorbox}[enhanced, colback=boxnavybg, colframe=brandnavy, boxrule=1.2pt, arc=4pt, title={\Large\bfseries\sffamily Unit 6 Overview \& Learning Objectives}]
\sffamily\normalsize
This unit synthesizes the complete Design Thinking lifecycle into iterative refinement, structured re-design, and high-impact stakeholder communication. By the end of this chapter, students will be able to:
\begin{itemize}[leftmargin=1.2em, itemsep=2pt, topsep=3pt]
    \item Execute the \textbf{Design Iteration Loop} from feedback analysis to re-testing.
    \item Contrast \textbf{Design Refactoring} (improving internal structure) with \textbf{Product Re-Design} (overhauling core architecture).
    \item Apply the feedback priority formula: $P = F \times S \times C$.
    \item Recognize triggers for \textbf{Strategic Pivoting} vs. Continuous Improvement using the \textbf{PDCA Cycle}.
    \item Tailor product presentations to specific audiences: users, engineers, and executive investors.
    \item Structure value propositions using SRI International's \textbf{NABC Model} (Need, Approach, Benefits per costs, Competition).
    \item Deliver compelling 30--60 second \textbf{Elevator Pitches}.
    \item Assemble a complete \textbf{Technical Design Case Study} with requirement traceability.
\end{itemize}
\end{tcolorbox}

\section{Orientation: The Iterative Refinement Lifecycle}

Innovation in Design Thinking is an ongoing cycle of empirical refinement. A product is never truly complete after the first build; it matures through disciplined feedback analysis, refactoring, and clear stakeholder advocacy.

\begin{keyequation}[The Iteration Progression Cycle]
\begin{equation}
\text{Define Assumption} \longrightarrow \text{Build Prototype} \longrightarrow \text{Test with Users} \longrightarrow \text{Analyze Evidence} \longrightarrow \text{Refactor / Re-design} \longrightarrow \text{Retest}
\end{equation}
\end{keyequation}

\section{Iteration, Refactoring, and Strategic Pivoting}

\subsection{Design Refactoring vs. Product Re-Design}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Design Refactoring:} Improving the internal consistency, layout alignment, typography hierarchy, component modularity, or code structure of a product \textbf{without altering its fundamental functional behavior}.
    \item \textbf{Product Re-Design:} Fundamental structural and functional overhaul triggered when user testing proves that the foundational problem definition, value proposition, or mechanical/software architecture has failed.
    \item \textbf{Regression Testing:} After any refactoring or re-design, the team must retest previously validated workflows to ensure new modifications did not break existing features.
\end{itemize}

\subsection{User Feedback Prioritization Formula}
To prevent subjective debates about which user critiques to implement first, engineering teams calculate a quantitative Priority Score:

\begin{keyequation}[Priority Score Calculation]
\begin{equation}
P = F \times S \times C
\end{equation}
\begin{itemize}[leftmargin=1.2em, itemsep=2pt]
    \item $F \in [1, 5]$: **Frequency** of the issue observed across test participants.
    \item $S \in [1, 5]$: **Severity** of the issue ($1 = \text{minor cosmetic preference}$; $5 = \text{complete task blocker / safety hazard}$).
    \item $C \in [0.1, 1.0]$: **Confidence** in the research evidence.
\end{itemize}
\end{keyequation}

\subsection{Strategic Pivots vs. Continuous Improvement (PDCA)}
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Strategic Pivot:} A structured course correction testing a new fundamental hypothesis regarding customer segment, delivery channel, or value proposition while preserving validated past learnings (e.g., YouTube pivoting from video dating to general video sharing).
    \item \textbf{Continuous Improvement (PDCA Cycle):} Incremental quality enhancement following:
    $$\textbf{Plan} \;\rightarrow\; \textbf{Do} \;\rightarrow\; \textbf{Check} \;\rightarrow\; \textbf{Act}$$
\end{itemize}

\section{Product Presentation \& Design Communication}

\subsection{Audience-Centred Communication}
An effective pitch is calibrated specifically to the stakeholder's primary decision criteria:
\begin{table}[h!]
\centering
\small
\renewcommand{\arraystretch}{1.3}
\begin{tabularx}{\linewidth}{p{3.2cm}X X}
\toprule
\textbf{Audience} & \textbf{Primary Concerns} & \textbf{Presentation Focus} \\
\midrule
\textbf{End Users} & Usability, convenience, personal value, privacy. & Intuitive workflows, comfort, immediate problem relief. \\
\textbf{Engineers / Builders} & Technical feasibility, scalability, safety, stack. & System architecture diagrams, component specs, latency, test metrics. \\
\textbf{Investors / Executives} & Business viability, market size, unit economics, ROI. & Customer acquisition cost, scalable revenue, competitive moat, NABC. \\
\bottomrule
\end{tabularx}
\caption{Tailoring Design Presentations to Key Stakeholders.}
\end{table}

\subsection{High-Impact Presentation Rules}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{The Compelling Hook:} Open with a startling real-world statistic, video clip, or user story that immediately demonstrates an urgent, unsolved human pain point.
    \item \textbf{The Rule of One:} Every slide must convey exactly ONE dominant concept with high-contrast, uncluttered visuals.
    \item \textbf{Live Representative Task Demo:} Demonstrate a complete, authentic user flow rather than clicking through boring settings menus (*``Show, Don't Tell''*).
    \item \textbf{Radical Candor (Stating Limitations):} Explicitly state known product limitations and future milestones. Acknowledging boundaries builds immense credibility with technical evaluators.
\end{enumerate}

\section{The NABC Pitching Model}

Developed by Curtis Carlson at SRI International, the NABC framework organizes innovation proposals into 4 fundamental pillars:
\begin{itemize}[leftmargin=1.2em, itemsep=3pt]
    \item \textbf{Need (N):} What is the specific, quantitative, validated customer pain point? Back it with user research evidence.
    \item \textbf{Approach (A):} What is your unique, feasible solution, technology mechanism, or service model?
    \item \textbf{Benefits per Costs (B):} What measurable benefits (time saved, errors reduced, revenue gained) does the user receive relative to the financial, behavioral, and time costs incurred?
    \item \textbf{Competition / Alternatives (C):} How does your solution provide clear relative advantage compared to existing market competitors, manual workarounds, and non-consumption?
\end{itemize}

\section{The Elevator Pitch}

\begin{definition}[Elevator Pitch]
A high-density 30--60 second spoken narrative designed to create sufficient clarity and excitement to secure a follow-up demonstration or partnership.
\end{definition}

\begin{keyequation}[The Universal Product Positioning Template]
\begin{quote}
\textit{``For \textbf{[target user]} who experiences \textbf{[validated problem]}, our \textbf{[product name]} is a \textbf{[product category]} that delivers \textbf{[compelling core benefit]}. Unlike \textbf{[primary competitor / current workaround]}, our solution \textbf{[key differentiator]}. User tests demonstrate \textbf{[validated metric / empirical evidence]}.''}
\end{quote}
\end{keyequation}

\section{The Technical Case Study Deliverable}

A comprehensive INT335 capstone design portfolio integrates the entire engineering lifecycle:
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item \textbf{Executive Summary \& Context}
    \item \textbf{Empathy Research Findings \& POV Definition}
    \item \textbf{Divergent Concepts \& Screening Matrix}
    \item \textbf{Prototype Evolution (Lo-Fi to Hi-Fi)}
    \item \textbf{Usability Testing Logs \& Feedback Capture Matrices}
    \item \textbf{Requirement Traceability Matrix}
    \item \textbf{Final Technical Architecture, Safety Specs \& Viability Plan}
\end{enumerate}

\section{Unit 6 Self-Assessment Test}

\begin{chaptertest}[Innovation Project, Re-Design \& Product Presentation]
\textbf{Time Allowed: 30 Minutes \hfill Maximum Marks: 25}

\vspace{0.4cm}
\noindent\textbf{Part A: Conceptual Multiple Choice (5 $\times$ 1 = 5 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item What does $P = F \times S \times C$ calculate in user feedback analysis?
    \item What is the main difference between Design Refactoring and Product Re-Design?
    \item What do the four letters in the NABC pitching framework represent?
    \item What is the standard duration of an effective elevator pitch?
    \item What is regression testing in the context of design iteration?
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part B: Short Calculation \& Method Questions (2 $\times$ 5 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{5}
    \item Calculate the priority score for two usability bugs:
    \begin{itemize}
        \item Bug 1: A broken checkout button affecting $F=4$ users, Severity $S=5$, Confidence $C=0.9$.
        \item Bug 2: A font misalignment affecting $F=5$ users, Severity $S=1$, Confidence $C=0.8$.
    \end{itemize}
    Explain which bug must be prioritized and why.
    \item Explain the 4 stages of the continuous improvement PDCA cycle.
\end{enumerate}

\vspace{0.3cm}
\noindent\textbf{Part C: Practical Elevator Pitch Formulation (1 $\times$ 10 = 10 Marks)}
\begin{enumerate}[leftmargin=1.2em, itemsep=4pt]
    \setcounter{enumi}{7}
    \item Write a complete, professional 45-second **Elevator Pitch** for an *IoT Smart Pill Dispenser for Alzheimer's Patients* using the Universal Positioning Template. Ensure it highlights Target User, Urgent Need, Category, Core Benefit, Differentiator, Empirical Evidence, and Call-to-Action.
\end{enumerate}
\end{chaptertest}

\begin{solutionbox}[Step-by-Step Unit Test Solutions]
\textbf{Part A Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=2pt]
    \item User feedback Priority Score ($F = \text{Frequency}, S = \text{Severity}, C = \text{Confidence}$).
    \item Refactoring improves internal quality without altering behavior; Re-design overhauls core functional architecture.
    \item Need, Approach, Benefits per costs, Competition/alternatives.
    \item 30 to 60 seconds.
    \item Retesting previously validated features to ensure recent changes have not introduced new defects.
\end{enumerate}

\textbf{Part B Solutions:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{5}
    \item \textbf{Bug Priority Calculation:}
    \begin{itemize}
        \item Bug 1: $P_1 = 4 \times 5 \times 0.9 = \mathbf{18.0}$.
        \item Bug 2: $P_2 = 5 \times 1 \times 0.8 = \mathbf{4.0}$.
        \item *Decision:* Bug 1 must be prioritized immediately because it is a critical task blocker ($S=5$) that prevents completed purchases, whereas Bug 2 is a minor cosmetic defect ($S=1$).
    \end{itemize}
    \item \textbf{PDCA Cycle:}
    \begin{itemize}
        \item *Plan:* Formulate hypothesis and design the modification.
        \item *Do:* Execute the prototype modification or test pilot.
        \item *Check:* Measure performance against success criteria.
        \item *Act:* Standardize successful changes or iterate further.
    \end{itemize}
\end{enumerate}

\textbf{Part C Solution:}
\begin{enumerate}[leftmargin=1.2em, itemsep=3pt]
    \setcounter{enumi}{7}
    \item \textbf{IoT Smart Pill Dispenser Elevator Pitch:}
    \begin{quote}
    ``For **elderly Alzheimer's patients living independently** who **frequently forget or double-dose their critical daily medications**, our **DoseGuard** is an **IoT-connected automated medication dispenser** that **guarantees exact medication adherence through timed audio-visual chimes and motorized lock-release compartments**. Unlike **traditional static pillboxes and generic smartphone alarms**, DoseGuard **automatically alerts remote family caregivers via SMS if a scheduled dosage is missed after 15 minutes**. In our hospital pilot testing with 40 senior patients, DoseGuard **reduced missed medication incidents from $38\%$ to zero across 60 days**. We are currently seeking **clinical hospital partnerships for our Phase 2 deployment**.''
    \end{quote}
\end{enumerate}
\end{solutionbox}
"""

with open("INT335/chapters/chapter-06-innovation-project-re-design-and-product-presentation.tex", "w", encoding="utf-8") as f:
    f.write(ch6)

print("Chapters 4, 5, and 6 generated successfully!")
