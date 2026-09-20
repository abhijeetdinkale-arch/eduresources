import React, { useState } from 'react';
import { ArrowRight, Sparkles, BookOpen, Shield, MessageCircle, Copy, CheckCheck, Phone, Mail, Check, Folder, ShieldCheck, CheckCircle2 } from 'lucide-react';

const PLANS = [
  {
    id: 'starter',
    name: 'Starter Pass',
    price: '₹299',
    duration: 'Single Semester',
    badge: null,
    highlight: false,
    desc: 'Essential basic textbooks & formula books for single semester prep.',
    features: [
      'Core Course Basic Textbooks',
      'Formula Books & Quick Cheatsheets',
      'In-App DRM Digital Reader',
      'Standard Email Support',
    ],
  },
  {
    id: 'pro',
    name: 'Pro All-Access Pass',
    price: '₹499',
    duration: 'Full Academic Year',
    badge: '🔥 MOST POPULAR • BEST VALUE',
    highlight: true,
    discount: 'SAVE 50%',
    desc: 'Complete full academic year vault with PYQs, sample papers & all 9+ course editions.',
    features: [
      'Everything in Starter Pass',
      'All 9+ Course Repositories (PHY, CSE, MTH, INT, ECE, MEC)',
      'Official PYQ Sets & Sample Papers with Solutions',
      'CA1, CA2, Midterm & Endterm Exam Companions',
      '300+ MCQ Question Banks & Clean Handwritten Notes',
      'Priority WhatsApp Support by Abhijeet Dinkale',
    ],
  },
  {
    id: 'vip',
    name: 'Lifetime Degree Pass',
    price: '₹999',
    duration: 'Lifetime All Years',
    badge: '👑 ULTIMATE VIP',
    highlight: false,
    desc: 'Ultimate 4-year degree pass with future AI/LLM assistant, 1-day query resolution & on-demand materials.',
    features: [
      'Everything in Pro All-Access Pass (All 4 Years Lifetime)',
      'Future AI / LLM Study Assistant & Smart Solver',
      'Academic Help Queries Solved Within 1 Day',
      'Request Any New Material or Topic On-Demand',
      'Direct 1-on-1 WhatsApp Support & VIP Priority Line',
    ],
  },
];

const QUICK_COURSES = [
  { code: 'PHY110', name: 'Engineering Physics & Derivations', count: '4 Editions' },
  { code: 'PHY175', name: 'Physics Question Bank & Formulas', count: '4 Editions' },
  { code: 'CSE111', name: 'Fundamentals of Computing & IT', count: '5 Editions' },
  { code: 'CSE326', name: 'Web Development & Technologies', count: '5 Editions' },
  { code: 'MTH165', name: 'Engineering Mathematics & Calculus', count: '5 Editions' },
  { code: 'INT335', name: 'Cloud Computing & Systems', count: '4 Editions' },
  { code: 'INT108', name: 'Python Programming Mastery', count: '3 Editions' },
  { code: 'ECE249', name: 'Digital Electronics Sample Papers', count: '3 Editions' },
  { code: 'ECE279', name: 'Electrical Handwritten Notes', count: '2 Editions' },
  { code: 'MEC136', name: 'Engineering Graphics & CAD PPTs', count: '2 Editions' },
];

export default function HomePage({ onBrowseBooks, onOpenPlans, onOpenLogin, user, isSubscribed, materialsCount = 37 }) {
  const [selectedPlan, setSelectedPlan] = useState('pro');
  const [copiedUpi, setCopiedUpi] = useState(false);
  const upiId = 'abhijeetdinkale@oksbi';
  const whatsappNumber = '917666937049';

  const handleCopyUpi = () => {
    navigator.clipboard.writeText(upiId);
    setCopiedUpi(true);
    setTimeout(() => setCopiedUpi(false), 2000);
  };

  const activePlanObj = PLANS.find((p) => p.id === selectedPlan) || PLANS[1];

  const whatsappMessage = encodeURIComponent(
    `Hello Abhijeet, I want to subscribe to the Edu network ${activePlanObj.name} (${activePlanObj.price}).\nMy Email: ${user?.email || 'student@university.edu'}\nMy Name: ${user?.name || 'Student'}`
  );

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-16">
      {/* 1. HERO SECTION */}
      <section className="bg-paper-100/90 dark:bg-darkbg-900/90 backdrop-blur-xs border border-paper-300/80 dark:border-darkbg-border rounded-[36px] p-6 sm:p-12 shadow-ticket dark:shadow-ticket-dark relative overflow-hidden transition-colors">
        <div className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-12 w-[380px] h-[380px] md:w-[480px] md:h-[480px] opacity-10 dark:opacity-5 pointer-events-none select-none">
          <img
            src="/logo.png"
            alt="Edu network star"
            className="w-full h-full object-contain filter invert dark:invert-0"
          />
        </div>

        <div className="max-w-3xl space-y-6 relative z-10">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border text-ink-800 dark:text-paper-200 text-xs font-mono tracking-wider">
            {isSubscribed ? (
              <>
                <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400" />
                <span>ACTIVE SCHOLAR PASS • UNLIMITED VAULT ACCESS</span>
              </>
            ) : (
              <>
                <span className="w-2 h-2 rounded-full bg-ochre-400 animate-pulse"></span>
                <span>OFFICIAL SYLLABUS TEXTS WITH IN-APP DIGITAL READER</span>
              </>
            )}
          </div>

          <h1 className="text-4xl sm:text-6xl font-cinzel font-black tracking-tight text-ink-900 dark:text-paper-50 leading-[1.08]">
            Interactive online <br />
            study education <br />
            <span className="font-serif italic font-normal text-ink-600 dark:text-ink-400">that inspires</span> ✦
          </h1>

          <p className="text-sm sm:text-base font-sans text-ink-600 dark:text-ink-400 leading-relaxed max-w-2xl">
            Discover the joy of studying through our vibrant academic repository, where passionate educators and students share certified curriculum textbooks, verified question banks, and intelligent AI study assistance.
          </p>

          <div className="flex flex-wrap items-center gap-3 pt-2">
            <button
              onClick={onBrowseBooks}
              className="px-6 py-3.5 rounded-full bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs font-semibold tracking-wider uppercase transition shadow-md flex items-center gap-2"
            >
              <span>{isSubscribed ? 'Open My Subject Dossiers' : 'Browse Subject Folders'}</span>
              <ArrowRight className="w-4 h-4" />
            </button>

            {/* If NOT subscribed, show Plans button */}
            {!isSubscribed && (
              <button
                onClick={onOpenPlans}
                className="px-6 py-3.5 rounded-full bg-[#E5C05B] hover:bg-[#d8b34c] text-ink-900 text-xs font-bold tracking-wider uppercase transition shadow-md flex items-center gap-2"
              >
                <Sparkles className="w-4 h-4" />
                <span>View Plans (from ₹299)</span>
              </button>
            )}

            {!user && (
              <button
                onClick={onOpenLogin}
                className="px-5 py-3.5 rounded-full bg-paper-200 dark:bg-darkbg-800 hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-900 dark:text-paper-100 text-xs font-mono font-bold transition border border-paper-300 dark:border-darkbg-border"
              >
                <span>Student Login</span>
              </button>
            )}
          </div>
        </div>

        {/* 4 Metric Badges */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 mt-12 pt-8 border-t border-paper-300/80 dark:border-darkbg-border relative z-10">
          <div className="bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-xs border border-paper-300 dark:border-darkbg-border rounded-2xl p-4">
            <span className="text-2xl font-cinzel font-bold text-ink-900 dark:text-paper-50">12k+</span>
            <p className="text-[11px] font-sans text-ink-600 dark:text-ink-400 mt-0.5">Students proudly served</p>
          </div>

          <div className="bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-xs border border-paper-300 dark:border-darkbg-border rounded-2xl p-4">
            <span className="text-2xl font-cinzel font-bold text-ink-900 dark:text-paper-50">34k</span>
            <p className="text-[11px] font-sans text-ink-600 dark:text-ink-400 mt-0.5">Hours of study instruction</p>
          </div>

          <div className="bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-xs border border-paper-300 dark:border-darkbg-border rounded-2xl p-4">
            <span className="text-2xl font-cinzel font-bold text-ink-900 dark:text-paper-50">10</span>
            <p className="text-[11px] font-sans text-ink-600 dark:text-ink-400 mt-0.5">Course Code Dossiers</p>
          </div>

          <div className="bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-xs border border-paper-300 dark:border-darkbg-border rounded-2xl p-4">
            <span className="text-2xl font-cinzel font-bold text-ink-900 dark:text-paper-50">4.9 ★</span>
            <p className="text-[11px] font-sans text-ink-600 dark:text-ink-400 mt-0.5">Academic Faculty Rating</p>
          </div>
        </div>
      </section>

      {/* 2. IF SUBSCRIBED: SHOW UNLOCKED ACTIVE STUDY SHELF (NO PRICING OR PAYWALLS) */}
      {isSubscribed ? (
        <section className="bg-paper-100/90 dark:bg-darkbg-900/90 backdrop-blur-xs border border-paper-300/80 dark:border-darkbg-border rounded-[36px] p-6 sm:p-12 shadow-ticket dark:shadow-ticket-dark">
          <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 border-b border-paper-300/80 dark:border-darkbg-border pb-6 mb-8">
            <div>
              <div className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 text-[10px] font-mono font-bold uppercase mb-2 border border-emerald-500/20">
                <ShieldCheck className="w-3.5 h-3.5" />
                <span>ALL DOSSIERS UNLOCKED</span>
              </div>
              <h2 className="text-2xl sm:text-3xl font-cinzel font-bold text-ink-900 dark:text-paper-50">
                Your Academic Library Shelf
              </h2>
              <p className="text-xs font-sans text-ink-600 dark:text-ink-400 mt-1">
                Select any course code below to open its textbooks, question banks, and notes.
              </p>
            </div>

            <button
              onClick={onBrowseBooks}
              className="px-5 py-2.5 rounded-full bg-ink-900 dark:bg-paper-50 hover:bg-black dark:hover:bg-paper-200 text-paper-50 dark:text-ink-900 text-xs font-mono font-bold tracking-wider uppercase transition shadow-xs flex items-center gap-1.5 shrink-0"
            >
              <span>Explore All Dossiers</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
            {QUICK_COURSES.map((c) => (
              <div
                key={c.code}
                onClick={onBrowseBooks}
                className="group bg-paper-50 dark:bg-darkbg-850 hover:bg-paper-200 dark:hover:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border rounded-2xl p-4 transition-all duration-200 cursor-pointer flex items-center justify-between shadow-xs"
              >
                <div className="flex items-center gap-3">
                  <div className="w-10 h-10 rounded-xl bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900 flex items-center justify-center font-cinzel font-bold text-xs">
                    {c.code.substring(0, 3)}
                  </div>
                  <div>
                    <h4 className="text-xs font-bold font-sans text-ink-900 dark:text-paper-50 group-hover:text-ochre-500 transition">
                      {c.code}
                    </h4>
                    <p className="text-[11px] text-ink-500 dark:text-ink-400 line-clamp-1">
                      {c.name}
                    </p>
                  </div>
                </div>
                <span className="text-[10px] font-mono text-ink-400 dark:text-ink-500 shrink-0">
                  {c.count} →
                </span>
              </div>
            ))}
          </div>
        </section>
      ) : (
        /* IF NOT SUBSCRIBED: SHOW 3-TIER PRICING (PROMOTING ₹500 PRO PASS) */
        <section className="bg-paper-100/90 dark:bg-darkbg-900/90 backdrop-blur-xs border border-paper-300/80 dark:border-darkbg-border rounded-[36px] p-6 sm:p-12 shadow-ticket dark:shadow-ticket-dark">
          <div className="text-center max-w-2xl mx-auto mb-10">
            <div className="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-ochre-400/20 text-ochre-500 text-[10px] font-mono tracking-widest uppercase mb-2 border border-ochre-400/30 font-bold">
              <Sparkles className="w-3.5 h-3.5" />
              <span>AFFORDABLE STUDENT PLANS</span>
            </div>
            <h2 className="text-3xl sm:text-4xl font-cinzel font-bold text-ink-900 dark:text-paper-50 mb-3">
              Academic Curriculum Passes
            </h2>
            <p className="text-xs sm:text-sm font-sans text-ink-600 dark:text-ink-400">
              Unlocking deep academic excellence across PHY110, PHY175, CSE111, CSE326, MTH165, INT335, INT108, ECE, and MEC.
            </p>
          </div>

          {/* 3 Pricing Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-5xl mx-auto mb-10">
            {PLANS.map((plan) => (
              <div
                key={plan.id}
                onClick={() => setSelectedPlan(plan.id)}
                className={`relative rounded-[32px] p-7 transition-all duration-300 cursor-pointer flex flex-col justify-between ${
                  plan.highlight
                    ? 'bg-paper-50 dark:bg-darkbg-850 border-2 border-[#E5C05B] shadow-2xl md:-translate-y-3 ring-8 ring-[#E5C05B]/15'
                    : 'bg-paper-50/80 dark:bg-darkbg-850/80 border border-paper-300 dark:border-darkbg-border hover:border-ink-900 dark:hover:border-paper-200'
                } ${selectedPlan === plan.id ? 'ring-2 ring-ink-900 dark:ring-paper-50' : ''}`}
              >
                {plan.badge && (
                  <div className="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#E5C05B] text-ink-950 text-[10px] font-mono font-black tracking-wider uppercase px-4 py-1.5 rounded-full shadow-md whitespace-nowrap">
                    {plan.badge}
                  </div>
                )}

                <div>
                  <div className="flex items-center justify-between mb-2">
                    <h3 className="font-cinzel font-bold text-xl text-ink-900 dark:text-paper-50">
                      {plan.name}
                    </h3>
                    {plan.discount && (
                      <span className="text-[10px] font-mono font-bold text-terracotta-600 bg-terracotta-500/10 px-2.5 py-0.5 rounded-full">
                        {plan.discount}
                      </span>
                    )}
                  </div>

                  <p className="text-xs font-sans text-ink-600 dark:text-ink-400 mb-5 min-h-[34px]">
                    {plan.desc}
                  </p>

                  <div className="flex items-baseline gap-1.5 border-b border-paper-300 dark:border-darkbg-border pb-5 mb-5">
                    <span className="text-4xl font-cinzel font-black text-ink-900 dark:text-paper-50">
                      {plan.price}
                    </span>
                    <span className="text-xs font-mono text-ink-500 dark:text-ink-400">
                      / {plan.duration}
                    </span>
                  </div>

                  <div className="space-y-3 text-xs text-ink-800 dark:text-paper-200 mb-8">
                    {plan.features.map((feat, i) => (
                      <div key={i} className="flex items-start gap-2.5">
                        <Check className={`w-4 h-4 shrink-0 mt-0.5 ${plan.highlight ? 'text-ochre-500 font-bold' : 'text-emerald-600'}`} />
                        <span className="leading-snug text-xs">{feat}</span>
                      </div>
                    ))}
                  </div>
                </div>

                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    setSelectedPlan(plan.id);
                  }}
                  className={`w-full py-3 rounded-full text-xs font-bold uppercase tracking-wider transition ${
                    selectedPlan === plan.id
                      ? plan.highlight
                        ? 'bg-[#E5C05B] text-ink-950 shadow-md'
                        : 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900'
                      : 'bg-paper-200 dark:bg-darkbg-700 text-ink-700 dark:text-paper-300 hover:bg-paper-300'
                  }`}
                >
                  {selectedPlan === plan.id ? 'Selected Pass ✓' : 'Select Pass'}
                </button>
              </div>
            ))}
          </div>

          {/* Selected Plan UPI Payment Box */}
          <div className="max-w-2xl mx-auto bg-paper-50 dark:bg-darkbg-850 border border-paper-300 dark:border-darkbg-border rounded-[32px] p-6 sm:p-8 shadow-floating">
            <div className="flex flex-col sm:flex-row items-center justify-between gap-4 border-b border-paper-300 dark:border-darkbg-border pb-5 mb-5">
              <div>
                <span className="text-[10px] font-mono text-ink-400 dark:text-ink-500 uppercase tracking-widest block">
                  ACTIVATING PASS:
                </span>
                <div className="flex items-baseline gap-2">
                  <span className="text-2xl font-cinzel font-bold text-ink-900 dark:text-paper-50">
                    {activePlanObj.name}
                  </span>
                  <span className="text-3xl font-cinzel font-black text-ochre-500">
                    {activePlanObj.price}
                  </span>
                </div>
              </div>

              <div className="flex items-center gap-2 bg-paper-100 dark:bg-darkbg-900 px-4 py-2.5 rounded-2xl border border-paper-300 dark:border-darkbg-border">
                <span className="text-xs font-mono text-ink-500 dark:text-ink-400">UPI:</span>
                <button
                  onClick={handleCopyUpi}
                  className="flex items-center gap-1.5 font-mono text-xs font-bold text-ink-900 dark:text-paper-100 hover:text-ochre-500 transition"
                >
                  <span>{upiId}</span>
                  {copiedUpi ? <CheckCheck className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5 text-ink-400" />}
                </button>
              </div>
            </div>

            <a
              href={`https://wa.me/${whatsappNumber}?text=${whatsappMessage}`}
              target="_blank"
              rel="noopener noreferrer"
              className="w-full py-4 px-6 bg-emerald-600 hover:bg-emerald-500 text-white rounded-2xl text-xs font-bold tracking-wider uppercase transition shadow-lg shadow-emerald-600/25 flex items-center justify-center gap-2 text-center"
            >
              <MessageCircle className="w-4 h-4" />
              <span>Pay {activePlanObj.price} & Instant WhatsApp Activation (+91 7666937049)</span>
              <ArrowRight className="w-4 h-4" />
            </a>
          </div>
        </section>
      )}

      {/* 3. COORDINATOR CONTACT BAR */}
      <section className="bg-paper-50/90 dark:bg-darkbg-850/90 backdrop-blur-xs border border-paper-300/80 dark:border-darkbg-border rounded-[28px] p-6 shadow-xs flex flex-col md:flex-row items-center justify-between gap-4 text-xs font-mono">
        <div className="flex items-center gap-2 text-ink-800 dark:text-paper-200">
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
          <span>Edu network Repository • Official Academic Pass</span>
        </div>

        <div className="flex flex-wrap items-center gap-3 text-ink-600 dark:text-ink-400">
          <a href="tel:+917666937049" className="hover:text-ink-900 dark:hover:text-paper-100 transition flex items-center gap-1">
            <Phone className="w-3.5 h-3.5" /> +91 7666937049
          </a>
          <span>•</span>
          <a href="mailto:arcnyz@gmail.com" className="hover:text-ink-900 dark:hover:text-paper-100 transition flex items-center gap-1">
            <Mail className="w-3.5 h-3.5" /> arcnyz@gmail.com
          </a>
          <span>•</span>
          <a
            href={`https://wa.me/${whatsappNumber}`}
            target="_blank"
            rel="noopener noreferrer"
            className="text-emerald-600 dark:text-emerald-400 font-bold hover:underline flex items-center gap-1"
          >
            <MessageCircle className="w-3.5 h-3.5" /> WhatsApp Chat
          </a>
        </div>
      </section>
    </div>
  );
}
