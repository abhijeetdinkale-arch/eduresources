/**
 * Universal Mock Examination Registry for EduNetwork
 * Aggregates verified university midterm papers across all engineering disciplines:
 * - MTH165: Engineering Mathematics I
 * - PHY110: Engineering Physics
 * - ECE249: Basic Electrical & Electronics Engineering
 * - CSE111: Fundamentals of Computing
 * - INT335: Design Thinking
 * - PHY175: Physics Practice & Formulae
 * - CSE326: Web Development & Technologies
 * - MEC136: Engineering Graphics & CAD (Subjective Drafting Studio)
 */

import { MTH165_MOCK_TESTS } from './mth165_mock_tests';
import { PHY110_MOCK_TESTS } from './phy110_mock_tests';
import { ECE249_MOCK_TESTS } from './ece249_mock_tests';
import { CSE111_MOCK_TESTS } from './cse111_mock_tests';
import { INT335_MOCK_TESTS } from './int335_mock_tests';
import { PHY175_MOCK_TESTS } from './phy175_mock_tests';
import { CSE326_MOCK_TESTS } from './cse326_mock_tests';
import { MEC136_DRAFTING_TESTS } from './mec136_drafting_tests';

export const COURSES_CONFIG = [
  {
    code: 'MTH165',
    name: 'Engineering Mathematics I',
    department: 'Mathematics',
    testsCount: MTH165_MOCK_TESTS.length,
    active: true,
    tag: `${MTH165_MOCK_TESTS.length} Full Papers Active`,
    description: 'Units 1-3: Matrices & Linear Algebra, Differential Calculus, Mean Value Theorems & Taylor Series.',
    accentColor: '#D97706', // Amber/Ochre
    isDrafting: false
  },
  {
    code: 'PHY110',
    name: 'Engineering Physics',
    department: 'Applied Sciences',
    testsCount: PHY110_MOCK_TESTS.length,
    active: true,
    tag: `${PHY110_MOCK_TESTS.length} Full Papers Active`,
    description: 'Units 1-3: Vector Calculus & Maxwell Equations, Lasers & Holography, Fiber Optics & Numerical Aperture.',
    accentColor: '#2563EB', // Blue
    isDrafting: false
  },
  {
    code: 'ECE249',
    name: 'Basic Electrical & Electronics Engineering',
    department: 'Electronics',
    testsCount: ECE249_MOCK_TESTS.length,
    active: true,
    tag: `${ECE249_MOCK_TESTS.length} Full Papers Active`,
    description: 'Units 1-3: DC Network Theorems (Thevenin/Norton), AC Fundamentals & RLC Resonance, Transformers & Diodes.',
    accentColor: '#EA580C', // Orange
    isDrafting: false
  },
  {
    code: 'CSE111',
    name: 'Fundamentals of Computing',
    department: 'Computer Science',
    testsCount: CSE111_MOCK_TESTS.length,
    active: true,
    tag: `${CSE111_MOCK_TESTS.length} Full Papers Active`,
    description: 'Units 1-3: Computer Systems & Cache Architecture, OS Process Lifecycle & Scheduling, Linux CLI & FHS.',
    accentColor: '#059669', // Emerald
    isDrafting: false
  },
  {
    code: 'INT335',
    name: 'Design Thinking',
    department: 'Information Tech',
    testsCount: INT335_MOCK_TESTS.length,
    active: true,
    tag: `${INT335_MOCK_TESTS.length} Full Papers Active`,
    description: 'Units 1-3: Foundations of Design Thinking, Empathy Mapping & Observation, POV & Ideation (SCAMPER).',
    accentColor: '#7C3AED', // Purple
    isDrafting: false
  },
  {
    code: 'PHY175',
    name: 'Physics Practice & Formulae',
    department: 'Applied Sciences',
    testsCount: PHY175_MOCK_TESTS.length,
    active: true,
    tag: `${PHY175_MOCK_TESTS.length} Full Papers Active`,
    description: 'Units 1-3: Solid State Physics & Fermi Energy, Rectifiers & BJT Transistors, Logic Gates & K-Maps.',
    accentColor: '#0284C7', // Sky Blue
    isDrafting: false
  },
  {
    code: 'CSE326',
    name: 'Web Development & Technologies',
    department: 'Computer Science',
    testsCount: CSE326_MOCK_TESTS.length,
    active: true,
    tag: `${CSE326_MOCK_TESTS.length} Full Papers Active`,
    description: 'Units 1-3: Semantic HTML5 Elements, CSS3 Specificity & Box Model, Flexbox & DOM Event Handling.',
    accentColor: '#E11D48', // Rose
    isDrafting: false
  },
  {
    code: 'MEC136',
    name: 'Engineering Graphics and CAD',
    department: 'Mechanical',
    testsCount: MEC136_DRAFTING_TESTS.length,
    active: true,
    tag: `${MEC136_DRAFTING_TESTS.length} Drafting Studios Active`,
    description: 'Units 1-3: Diagonal Scales (4.75 m), Line Projections with Traces (45°), 3D Isometric to Orthographic Views.',
    accentColor: '#475569', // Slate
    isDrafting: true
  }
];

export const ALL_MOCK_TESTS_MAP = {
  MTH165: MTH165_MOCK_TESTS,
  PHY110: PHY110_MOCK_TESTS,
  ECE249: ECE249_MOCK_TESTS,
  CSE111: CSE111_MOCK_TESTS,
  INT335: INT335_MOCK_TESTS,
  PHY175: PHY175_MOCK_TESTS,
  CSE326: CSE326_MOCK_TESTS,
  MEC136: MEC136_DRAFTING_TESTS
};

export const getTestsForCourse = (courseCode) => {
  return ALL_MOCK_TESTS_MAP[courseCode] || [];
};

export const findTestById = (testId) => {
  for (const list of Object.values(ALL_MOCK_TESTS_MAP)) {
    const found = list.find((t) => t.id === testId);
    if (found) return found;
  }
  return null;
};
