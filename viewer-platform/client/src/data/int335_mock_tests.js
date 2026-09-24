/**
 * Official INT335: Design Thinking Midterm Mock Examination Suite
 * Contains Full-Length 30-Question Tests
 * Modelled on actual University Midterm Examination Question Bank
 * Focuses strictly on Units 1-3:
 *   Unit 1: Foundations of Learning, Creativity and Design Thinking
 *   Unit 2: Empathy, Observation and Problem Identification
 *   Unit 3: Ideation and Creative Problem Solving
 * Authentic +1 / -0.25 marking scheme and detailed step-by-step solutions.
 */

export const INT335_MOCK_TESTS = [
  {
    id: 'int335-midterm-paper-1',
    code: 'INT335-MIDTERM-1',
    title: 'Midterm Examination • Paper 1 (Official University Blueprint)',
    courseCode: 'INT335',
    courseName: 'Design Thinking',
    examType: 'Midterm Examination',
    durationMinutes: 90,
    totalQuestions: 30,
    marksPerQuestion: 1,
    negativeMarks: 0.25,
    maxMarks: 30,
    difficulty: 'Standard Exam',
    topics: ['Empathy & Observation', 'Problem Definition', 'Ideation Techniques', 'Wicked Problems'],
    description: 'Authentic university midterm examination paper testing human-centered design principles, empathy mapping, wicked problems, divergent vs convergent thinking, and SCAMPER ideation.',
    questions: [
      {
        id: 1,
        question: 'What is the fundamental starting point and core philosophy of Design Thinking?',
        options: ['Cutting-edge technology exploration', 'Market profit maximization', 'Human needs and user empathy', 'Government regulations compliance'],
        correctIndex: 2,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'Design Thinking is an intrinsically human-centered methodology.',
            'It begins with deeply understanding real human needs, feelings, and pain points before considering technical constraints or business models.'
          ],
          keyConcept: 'Human-centered empathy is the bedrock of Design Thinking.'
        }
      },
      {
        id: 2,
        question: 'Who coined the term "Wicked Problems" in 1973 to describe complex, ambiguous social and organizational challenges?',
        options: ['Herbert Simon and Peter Rowe', 'Horst Rittel and Melvin Webber', 'David Kelley and Tim Brown', 'Karl Duncker and David Kolb'],
        correctIndex: 1,
        topic: 'Wicked Problems',
        explanation: {
          steps: [
            'In 1973, social planners Horst Rittel and Melvin Webber introduced the concept of "Wicked Problems" to characterize challenges with incomplete, contradictory, and changing requirements.'
          ],
          keyConcept: 'Rittel and Webber formulated the theory of Wicked Problems.'
        }
      },
      {
        id: 3,
        question: 'Which of the following is NOT one of IDEO\'s three overlapping lenses of innovation in Design Thinking?',
        options: ['Desirability (Human)', 'Feasibility (Technical)', 'Viability (Business)', 'Predictability (Bureaucracy)'],
        correctIndex: 3,
        topic: 'Problem Definition',
        explanation: {
          steps: [
            'IDEO defines successful innovation at the intersection of three criteria:',
            '1. Desirability: What makes sense to and for people?',
            '2. Feasibility: What is technologically possible?',
            '3. Viability: What is economically sustainable and viable?',
            'Predictability is not an innovation lens.'
          ],
          keyConcept: 'Innovation Venn: Desirability, Feasibility, Viability.'
        }
      },
      {
        id: 4,
        question: 'What cognitive thinking mode focuses on generating a wide variety of novel, unconstrained ideas without immediate judgment?',
        options: ['Convergent thinking', 'Divergent thinking', 'Critical thinking', 'Deductive reasoning'],
        correctIndex: 1,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'Divergent thinking expands choices and explores broad possibilities.',
            'Convergent thinking subsequently narrows down and selects the best options.'
          ],
          keyConcept: 'Divergent thinking broadens options; Convergent thinking refines and selects.'
        }
      },
      {
        id: 5,
        question: 'Which brain state is characterized by relaxed, diffused attention, enabling subconscious incubation and unexpected creative breakthroughs?',
        options: ['Focused mode', 'Diffused mode', 'Analytical mode', 'Reflexive mode'],
        correctIndex: 1,
        topic: 'Problem Definition',
        explanation: {
          steps: [
            'As popularized by neuroscience, the diffuse mode allows disparate neural areas to connect when attention wanders (e.g. taking a walk, in the shower), fostering creative leaps.'
          ],
          keyConcept: 'Diffused mode facilitates subconscious creative connections.'
        }
      },
      {
        id: 6,
        question: 'In Bloom\'s Revised Taxonomy of Educational Objectives, which cognitive level represents the pinnacle of learning mastery?',
        options: ['Analyzing', 'Evaluating', 'Creating', 'Applying'],
        correctIndex: 2,
        topic: 'Problem Definition',
        explanation: {
          steps: [
            'The revised Bloom\'s taxonomy ranks cognitive skills from lowest to highest:',
            'Remembering → Understanding → Applying → Analyzing → Evaluating → Creating.'
          ],
          keyConcept: '"Creating" is the highest level of Bloom\'s cognitive taxonomy.'
        }
      },
      {
        id: 7,
        question: 'The cognitive bias where an individual views an object or tool as only functioning in its customary, traditional manner is called:',
        options: ['Functional Fixedness', 'Confirmation Bias', 'Anchoring Bias', 'Framing Effect'],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'Karl Duncker demonstrated functional fixedness with the candle problem: subjects failed to see the matchbox as a potential platform because they only viewed it as a container.'
          ],
          keyConcept: 'Functional fixedness prevents seeing alternative uses for familiar objects.'
        }
      },
      {
        id: 8,
        question: 'What is the primary objective of the "Empathize" phase in the Stanford d.school Design Thinking framework?',
        options: [
          'Design digital wireframes immediately',
          'Understand users through observation, engagement, and immersing oneself in their lived experiences',
          'Conduct pricing negotiations',
          'Pitch to venture capitalists'
        ],
        correctIndex: 1,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'Empathizing is about understanding user experiences, motivations, emotional barriers, and physical context without personal bias.'
          ],
          keyConcept: 'Empathy discovers explicit and latent user needs.'
        }
      },
      {
        id: 9,
        question: 'Which design research artifact synthesizes qualitative user observations into four quadrants: "Says", "Thinks", "Does", and "Feels"?',
        options: ['User Persona', 'Customer Journey Map', 'Empathy Map', 'Stakeholder Matrix'],
        correctIndex: 2,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'An Empathy Map splits insights into: What the user Says (quotes), Thinks (beliefs), Does (actions), and Feels (emotions), revealing hidden tensions.'
          ],
          keyConcept: 'Empathy Map quadrants: Says, Thinks, Does, Feels.'
        }
      },
      {
        id: 10,
        question: 'A well-crafted Point-of-View (POV) problem statement in Design Thinking combines three core elements:',
        options: [
          'User + Need + Insight',
          'Budget + Timeline + Deliverable',
          'Market + Competitor + Profit',
          'Problem + Solution + Price'
        ],
        correctIndex: 0,
        topic: 'Problem Definition',
        explanation: {
          steps: [
            'Formula: [User] needs [User\'s Need] because [Surprising Insight].',
            'This provides a human-centered framing that sparks productive ideation.'
          ],
          keyConcept: 'POV = User + Need + Insight.'
        }
      },
      {
        id: 11,
        question: 'How do designers transition from a defined POV problem statement into actionable brainstorming prompts?',
        options: [
          'By drafting "How Might We" (HMW) questions',
          'By writing immediate business contracts',
          'By applying standard operating procedures',
          'By executing code compilations'
        ],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            '"How Might We" (HMW) questions open up solution space: "How" suggests solutions exist, "Might" encourages open possibilities, "We" promotes collaboration.'
          ],
          keyConcept: '"How Might We" (HMW) questions launch generative ideation.'
        }
      },
      {
        id: 12,
        question: 'What does the acronym SCAMPER in creative problem solving stand for?',
        options: [
          'Substitute, Combine, Adapt, Modify/Magnify, Put to another use, Eliminate, Reverse/Rearrange',
          'Solve, Create, Analyze, Model, Program, Evaluate, Repeat',
          'Scan, Capture, Archive, Manage, Process, Export, Retain',
          'Select, Collect, Align, Merge, Position, Enable, Review'
        ],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'SCAMPER is an idea-generation checklist developed by Bob Eberle based on Alex Osborn\'s brainstorming principles.'
          ],
          keyConcept: 'SCAMPER: Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse.'
        }
      },
      {
        id: 13,
        question: 'Which of the following is a fundamental rule during a productive Design Thinking Brainstorming session?',
        options: [
          'Immediately criticize unfeasible ideas',
          'Defer judgment and encourage wild ideas',
          'Focus exclusively on one safe idea',
          'Limit participants to senior management'
        ],
        correctIndex: 1,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'IDEO Brainstorming rules: Defer judgment, Encourage wild ideas, Build on the ideas of others, Stay focused on topic, One conversation at a time, Go for quantity.'
          ],
          keyConcept: 'Deferring judgment unlocks creative divergent thinking.'
        }
      },
      {
        id: 14,
        question: 'In customer journey mapping, "Touchpoints" refer to:',
        options: [
          'Points of interaction between the user and the product, service, or brand across their experience timeline',
          'Physical touch screen hardware',
          'Employee biometric checkpoints',
          'Server ping responses'
        ],
        correctIndex: 0,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'Touchpoints are moments of engagement (e.g. visiting a website, unboxing a product, speaking to customer support).'
          ],
          keyConcept: 'Touchpoints are moments of user-brand interaction.'
        }
      },
      {
        id: 15,
        question: 'What is the primary purpose of creating Extreme User Personas (e.g., both power users and complete novices)?',
        options: [
          'To design products exclusively for fringe demographics',
          'Extreme users amplify unarticulated needs and workarounds that benefit mainstream users',
          'To satisfy legal compliance quotas',
          'To reduce prototyping costs'
        ],
        correctIndex: 1,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'Mainstream users often tolerate difficulties, whereas extreme users invent clever workarounds or experience extreme frustration, illuminating latent opportunities.'
          ],
          keyConcept: 'Extreme users reveal amplified needs that inspire breakthrough solutions.'
        }
      },
      {
        id: 16,
        question: 'The "Fly on the Wall" qualitative observation method involves:',
        options: [
          'Discreetly observing users in their natural environment without interfering or interacting with them',
          'Administering multiple-choice surveys over email',
          'Conducting formal laboratory focus groups',
          'Interviewing corporate executives'
        ],
        correctIndex: 0,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'Shadowing or fly-on-the-wall observation captures genuine user behaviors, habits, and body language without observer Hawthorne bias.'
          ],
          keyConcept: 'Fly on the wall is unobtrusive naturalistic observation.'
        }
      },
      {
        id: 17,
        question: 'Which method uses rapid, silent idea generation on sticky notes passed around in silence before discussion?',
        options: ['Brainwriting (Method 6-3-5)', 'Traditional vocal brainstorming', 'Debate panel', 'Solo contemplation'],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'Brainwriting (such as 6-3-5: 6 people, 3 ideas, 5 minutes) ensures equal voice for introverted team members and eliminates vocal dominance.'
          ],
          keyConcept: 'Brainwriting generates high volume of ideas quietly and democratically.'
        }
      },
      {
        id: 18,
        question: 'In Edward de Bono\'s "Six Thinking Hats" framework, what does wearing the "Green Hat" signify?',
        options: [
          'Creativity, new ideas, possibilities, and alternatives',
          'Facts, figures, and objective data (White Hat)',
          'Caution, critical judgment, and risk assessment (Black Hat)',
          'Emotions, gut feelings, and intuition (Red Hat)'
        ],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'White: Facts; Red: Feelings; Black: Risks; Yellow: Optimism; Green: Creativity; Blue: Process control.'
          ],
          keyConcept: 'Green Hat represents creative thinking and alternatives.'
        }
      },
      {
        id: 19,
        question: 'In the Double Diamond design framework developed by the British Design Council, the four phases in sequence are:',
        options: [
          'Discover → Define → Develop → Deliver',
          'Design → Draft → Deploy → Debug',
          'Decide → Document → Distribute → Discard',
          'Deduce → Direct → Delegate → Deliver'
        ],
        correctIndex: 0,
        topic: 'Problem Definition',
        explanation: {
          steps: [
            'Diamond 1 (Problem Space): Discover (divergent) → Define (convergent).',
            'Diamond 2 (Solution Space): Develop (divergent) → Deliver (convergent).'
          ],
          keyConcept: 'Double Diamond: Discover, Define, Develop, Deliver.'
        }
      },
      {
        id: 20,
        question: 'What is the distinction between "Latent Needs" and "Explicit Needs" in user research?',
        options: [
          'Explicit needs are openly articulated by users; latent needs are unarticulated, subconscious needs that users cannot easily describe',
          'Latent needs are illegal requirements',
          'Explicit needs only relate to software bugs',
          'There is no distinction'
        ],
        correctIndex: 0,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'Users can state explicit needs ("I want a faster horse").',
            'Latent needs must be uncovered through observation ("I need to travel between cities comfortably and reliably" → automobile).'
          ],
          keyConcept: 'Latent needs are hidden opportunities discovered through deep empathy.'
        }
      },
      {
        id: 21,
        question: 'The "Five Whys" interrogation technique originally developed by Sakichi Toyoda is used primarily to:',
        options: [
          'Drill down past superficial symptoms to uncover the root cause of an issue',
          'Test code performance five times',
          'Conduct employee background checks',
          'Assign blame to team members'
        ],
        correctIndex: 0,
        topic: 'Problem Definition',
        explanation: {
          steps: [
            'By repeatedly asking "Why?", each answer forms the basis of the next question, peeling back layers of symptoms to reveal foundational root causes.'
          ],
          keyConcept: 'Five Whys identifies root causes beneath surface symptoms.'
        }
      },
      {
        id: 22,
        question: 'In customer journey mapping, emotional peaks and valleys are identified to locate:',
        options: [
          'Pain points (moments of frustration) and Moments of Delight',
          'Server response latency metrics',
          'Employee salary grades',
          'Legal liability contracts'
        ],
        correctIndex: 0,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'Mapping the emotional curve highlights where users feel confused, delayed, or anxious (pain points), guiding where innovation creates the greatest relief.'
          ],
          keyConcept: 'Pain points and moments of truth guide targeted redesign.'
        }
      },
      {
        id: 23,
        question: 'What does "Bodystorming" entail during the ideation phase?',
        options: [
          'Physically acting out, roleplaying, and simulating user scenarios in a physical space with rough props',
          'Typing ideas into spreadsheets',
          'Performing aerobic exercises',
          'Sitting in dark rooms contemplating problems'
        ],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'Bodystorming combines roleplay with physical embodiment, quickly exposing ergonomic, interpersonal, and situational dynamics.'
          ],
          keyConcept: 'Bodystorming is physical roleplay of user interactions.'
        }
      },
      {
        id: 24,
        question: 'Why is "Failing Fast and Early" considered a virtue in Design Thinking?',
        options: [
          'Because low-fidelity experimentation uncovers flaws when iteration costs are near zero, avoiding costly failures post-launch',
          'Because failure is the explicit goal of companies',
          'To prematurely terminate engineering projects',
          'To discourage junior designers'
        ],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'Finding flaws early in sketches and paper prototypes costs minutes; finding flaws after full tooling and software rollout costs millions.'
          ],
          keyConcept: 'Failing fast minimizes iteration costs and validates assumptions.'
        }
      },
      {
        id: 25,
        question: 'Which method uses an 8-minute blitz where each team member sketches 8 distinct ideas in 8 minutes on a folded sheet of paper?',
        options: ['Crazy Eights', 'Mind Mapping', 'Delphi Method', 'Morphological Matrix'],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'Crazy Eights is a core Design Sprint sprint exercise. The fast pace forces designers past their initial obvious ideas into novel territory.'
          ],
          keyConcept: 'Crazy Eights: 8 ideas in 8 minutes for rapid idea generation.'
        }
      },
      {
        id: 26,
        question: 'What is a "Composite User Persona"?',
        options: [
          'A fictional archetype synthesized from patterns and traits observed across multiple real research participants',
          'A real living individual whose exact identity is revealed',
          'A random computer-generated avatar',
          'A resume of the designer'
        ],
        correctIndex: 0,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'A persona consolidates qualitative interview trends, goals, frustrations, and behaviors into a relatable character representing a core user segment.'
          ],
          keyConcept: 'Personas are archetypes based on real qualitative research patterns.'
        }
      },
      {
        id: 27,
        question: 'When conducting an ethnographic user interview, why should open-ended questions like "Tell me about the last time you..." be prioritized over closed yes/no questions?',
        options: [
          'They evoke rich narrative storytelling and uncover emotional motivations and unexpected nuances',
          'They take less time to transcribe',
          'They make the interviewee feel interrogated',
          'They can be answered by automated robots'
        ],
        correctIndex: 0,
        topic: 'Empathy & Observation',
        explanation: {
          steps: [
            'Stories contain emotion, context, and workarounds that yes/no answers obscure.'
          ],
          keyConcept: 'Open-ended storytelling questions uncover authentic motivations.'
        }
      },
      {
        id: 28,
        question: 'In idea clustering and selection, the "Dot Voting" technique enables team members to:',
        options: [
          'Democratically prioritize and converge upon the most promising ideas using a limited number of voting stickers',
          'Assign mathematical grades to every concept',
          'Discard all wild ideas immediately',
          'Select the idea favored by the highest-paid person'
        ],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'Dot voting gives each team member 3-5 sticky dots to place on their favorite concepts, quickly highlighting shared consensus.'
          ],
          keyConcept: 'Dot voting provides fast, democratic prioritization of ideas.'
        }
      },
      {
        id: 29,
        question: 'What is an "Analogy and Metaphor" ideation technique (e.g. "How would Disney or Apple solve hospital waiting lines?")?',
        options: [
          'Borrowing proven paradigms and customer service principles from unrelated industries to spark novel solutions',
          'Plagiarizing competitor marketing materials',
          'Renaming existing hospital procedures with movie titles',
          'Ignoring the medical domain entirely'
        ],
        correctIndex: 0,
        topic: 'Ideation Techniques',
        explanation: {
          steps: [
            'Cross-industry analogies (e.g. Formula 1 pit stops inspiring emergency room pediatric surgery handoffs) transfer established best practices to new contexts.'
          ],
          keyConcept: 'Cross-industry analogies translate successful patterns into new domains.'
        }
      },
      {
        id: 30,
        question: 'Which of the following best summarizes the relationship between Problem Definition and Ideation in Design Thinking?',
        options: [
          'A deeply empathetic, accurately defined problem makes effective ideation straightforward and impactful',
          'Ideation should always precede problem definition',
          'Problem definition is optional if brainstorming is energetic',
          'Solutions determine what the problem was'
        ],
        correctIndex: 0,
        topic: 'Problem Definition',
        explanation: {
          steps: [
            'As Albert Einstein famously observed: "If I had an hour to solve a problem, I\'d spend 55 minutes thinking about the problem and 5 minutes thinking about solutions."'
          ],
          keyConcept: 'Careful problem definition is the key to meaningful ideation.'
        }
      }
    ]
  }
];
