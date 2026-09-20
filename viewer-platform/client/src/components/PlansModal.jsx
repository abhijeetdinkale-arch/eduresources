import React, { useState, useEffect } from 'react';
import { X, Check, Copy, CheckCheck, MessageCircle, Sparkles, ArrowRight, ShieldCheck } from 'lucide-react';

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
      'Formula Books & Cheatsheets',
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
    desc: 'Complete academic year vault with PYQs, sample papers & all 9+ course editions.',
    features: [
      'Everything in Starter Pass',
      'All 9+ Course Repositories (PHY, CSE, MTH, INT...)',
      'Official PYQ Sets & Sample Papers with Solutions',
      'CA1, CA2, Midterm & Endterm Companions',
      '300+ MCQ Banks & Clean Handwritten Notes',
      'Priority WhatsApp Support',
    ],
  },
  {
    id: 'vip',
    name: 'Lifetime Degree Pass',
    price: '₹999',
    duration: 'Lifetime All Years',
    badge: '👑 ULTIMATE VIP',
    highlight: false,
    desc: 'Ultimate 4-year degree pass with AI assistant, fast query resolution & on-demand books.',
    features: [
      'Everything in Pro All-Access Pass',
      'Full 4 Years Lifetime Access',
      'Future AI / LLM Study Assistant',
      'Academic Queries Solved Within 1 Day',
      'Direct 1-on-1 VIP WhatsApp Line',
    ],
  },
];

export default function PlansModal({ isOpen, onClose, user }) {
  const [selectedPlan, setSelectedPlan] = useState('pro');
  const [copiedUpi, setCopiedUpi] = useState(false);
  const upiId = 'abhijeetdinkale@oksbi';
  const whatsappNumber = '917666937049';

  // Close on Escape key
  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const handleCopyUpi = (e) => {
    e.stopPropagation();
    navigator.clipboard.writeText(upiId);
    setCopiedUpi(true);
    setTimeout(() => setCopiedUpi(false), 2000);
  };

  const activePlanObj = PLANS.find((p) => p.id === selectedPlan) || PLANS[1];

  const whatsappMessage = encodeURIComponent(
    `Hello Abhijeet, I want to subscribe to the Edu network ${activePlanObj.name} (${activePlanObj.price}).\nMy Email: ${user?.email || 'student@university.edu'}\nMy Name: ${user?.name || 'Student'}`
  );

  return (
    <div
      onClick={onClose}
      className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-ink-950/80 backdrop-blur-md overflow-y-auto cursor-pointer"
      title="Click outside to close"
    >
      {/* Modal Dialog Card */}
      <div
        onClick={(e) => e.stopPropagation()}
        className="relative w-full max-w-4xl max-h-[92vh] flex flex-col bg-paper-50 dark:bg-darkbg-850 border border-paper-300 dark:border-darkbg-border rounded-[32px] shadow-floating cursor-default animate-in fade-in zoom-in-95 duration-200 overflow-hidden my-auto"
      >
        {/* Sticky Modal Top Bar with Prominent Close Button */}
        <div className="sticky top-0 z-20 flex items-center justify-between px-6 pt-5 pb-3 bg-paper-50/95 dark:bg-darkbg-850/95 backdrop-blur-md border-b border-paper-200 dark:border-darkbg-border/60 shrink-0">
          <div className="flex items-center gap-2">
            <div className="w-5 h-5 rounded-full bg-ink-900 dark:bg-paper-50 flex items-center justify-center p-0.5">
              <img src="/logo.png" alt="Star" className="w-full h-full object-contain filter invert dark:invert-0" />
            </div>
            <span className="text-xs font-mono font-bold text-ink-900 dark:text-paper-100 tracking-wider">
              EDU NETWORK • CURRICULUM PASSES
            </span>
          </div>

          {/* Close Cross Button */}
          <button
            onClick={onClose}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-paper-200 dark:bg-darkbg-750 hover:bg-terracotta-500/20 hover:text-terracotta-600 dark:hover:text-terracotta-400 text-ink-700 dark:text-paper-200 text-xs font-mono font-bold transition border border-paper-300 dark:border-darkbg-border shadow-xs"
            title="Close (Esc or click outside)"
          >
            <X className="w-4 h-4" />
            <span className="hidden sm:inline">CLOSE (✕)</span>
          </button>
        </div>

        {/* Scrollable Content Body */}
        <div className="overflow-y-auto p-5 sm:p-7 space-y-6">
          {/* Header Title */}
          <div className="text-center pt-1">
            <div className="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-ochre-400/20 text-ochre-500 text-[10px] font-mono tracking-widest uppercase mb-2 border border-ochre-400/30 font-bold">
              <Sparkles className="w-3 h-3" />
              <span>SELECT YOUR ACADEMIC PASS</span>
            </div>
            <h2 className="text-2xl sm:text-3xl font-cinzel font-black text-ink-900 dark:text-paper-50 mb-1.5">
              Curriculum Access Passes
            </h2>
            <p className="text-xs sm:text-sm font-sans text-ink-600 dark:text-ink-400 max-w-lg mx-auto leading-relaxed">
              Unlock certified syllabus textbooks, high-yield question banks, and complete exam companion sets.
            </p>
          </div>

          {/* 3-Plan Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 sm:gap-5">
            {PLANS.map((plan) => (
              <div
                key={plan.id}
                onClick={() => setSelectedPlan(plan.id)}
                className={`relative rounded-[24px] p-5 transition-all duration-200 cursor-pointer flex flex-col justify-between ${
                  plan.highlight
                    ? 'bg-paper-100 dark:bg-darkbg-900 border-2 border-[#E5C05B] shadow-lg md:-translate-y-1 ring-2 ring-[#E5C05B]/20'
                    : 'bg-paper-50 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border hover:border-ink-900 dark:hover:border-paper-200'
                } ${selectedPlan === plan.id ? 'ring-2 ring-ink-900 dark:ring-paper-50' : ''}`}
              >
                {/* Badge for Pro Plan */}
                {plan.badge && (
                  <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-[#E5C05B] text-ink-950 text-[9px] font-mono font-black tracking-wider uppercase px-2.5 py-0.5 rounded-full shadow-md whitespace-nowrap">
                    {plan.badge}
                  </div>
                )}

                <div>
                  <div className="flex items-center justify-between mb-1.5 pt-1">
                    <h3 className="font-cinzel font-bold text-base text-ink-900 dark:text-paper-50">
                      {plan.name}
                    </h3>
                    {plan.discount && (
                      <span className="text-[9px] font-mono font-bold text-terracotta-600 bg-terracotta-500/10 px-1.5 py-0.5 rounded-full">
                        {plan.discount}
                      </span>
                    )}
                  </div>

                  <p className="text-[11px] font-sans text-ink-600 dark:text-ink-400 mb-3 min-h-[28px] leading-tight">
                    {plan.desc}
                  </p>

                  <div className="flex items-baseline gap-1.5 border-b border-paper-300 dark:border-darkbg-border pb-3 mb-3">
                    <span className="text-2xl sm:text-3xl font-cinzel font-black text-ink-900 dark:text-paper-50">
                      {plan.price}
                    </span>
                    <span className="text-[11px] font-mono text-ink-500 dark:text-ink-400">
                      / {plan.duration}
                    </span>
                  </div>

                  {/* Features list */}
                  <div className="space-y-1.5 text-xs text-ink-800 dark:text-paper-200 mb-5">
                    {plan.features.map((feat, i) => (
                      <div key={i} className="flex items-start gap-1.5">
                        <Check className={`w-3.5 h-3.5 shrink-0 mt-0.5 ${plan.highlight ? 'text-ochre-500 font-bold' : 'text-emerald-600'}`} />
                        <span className="leading-tight text-[11px]">{feat}</span>
                      </div>
                    ))}
                  </div>
                </div>

                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    setSelectedPlan(plan.id);
                  }}
                  className={`w-full py-2 rounded-full text-xs font-semibold uppercase tracking-wider transition ${
                    selectedPlan === plan.id
                      ? plan.highlight
                        ? 'bg-[#E5C05B] text-ink-950 shadow-sm font-bold'
                        : 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900'
                      : 'bg-paper-200 dark:bg-darkbg-700 text-ink-700 dark:text-paper-300 hover:bg-paper-300'
                  }`}
                >
                  {selectedPlan === plan.id ? 'Selected Pass ✓' : 'Select Pass'}
                </button>
              </div>
            ))}
          </div>

          {/* Selected Plan Action & Payment Box */}
          <div className="bg-paper-100 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-2xl p-4 sm:p-5">
            <div className="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3">
              <div>
                <span className="text-[10px] font-mono text-ink-500 dark:text-ink-400 uppercase tracking-widest block">
                  SELECTED PASS:
                </span>
                <div className="flex items-baseline gap-2">
                  <span className="text-lg font-cinzel font-bold text-ink-900 dark:text-paper-50">
                    {activePlanObj.name}
                  </span>
                  <span className="text-xl font-cinzel font-black text-ochre-500">
                    {activePlanObj.price}
                  </span>
                  <span className="text-xs font-mono text-ink-500">({activePlanObj.duration})</span>
                </div>
              </div>

              <div className="flex items-center gap-2 bg-paper-50 dark:bg-darkbg-800 px-3 py-1.5 rounded-xl border border-paper-300 dark:border-darkbg-border">
                <span className="text-[10px] font-mono text-ink-500 dark:text-ink-400">UPI:</span>
                <button
                  onClick={handleCopyUpi}
                  className="flex items-center gap-1.5 font-mono text-xs font-bold text-ink-900 dark:text-paper-100 hover:text-ochre-500 transition"
                  title="Click to copy UPI ID"
                >
                  <span>{upiId}</span>
                  {copiedUpi ? <CheckCheck className="w-3.5 h-3.5 text-emerald-600" /> : <Copy className="w-3.5 h-3.5 text-ink-400" />}
                </button>
              </div>
            </div>

            {/* Action to WhatsApp */}
            <a
              href={`https://wa.me/${whatsappNumber}?text=${whatsappMessage}`}
              target="_blank"
              rel="noopener noreferrer"
              className="w-full py-3 px-5 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold tracking-wider uppercase transition shadow-md shadow-emerald-600/20 flex items-center justify-center gap-2 text-center"
            >
              <MessageCircle className="w-4 h-4" />
              <span>Pay {activePlanObj.price} & Instant WhatsApp Activation (+91 7666937049)</span>
              <ArrowRight className="w-4 h-4" />
            </a>
          </div>

          {/* Direct Coordinator Footer */}
          <div className="pt-2 border-t border-dashed border-paper-300 dark:border-darkbg-border flex flex-wrap items-center justify-between text-[10px] font-mono text-ink-500 dark:text-ink-400 gap-2">
            <span>Coordinator: <strong>Abhijeet Dinkale</strong></span>
            <span>📞 +91 7666937049</span>
            <span>✉️ arcnyz@gmail.com</span>
          </div>
        </div>
      </div>
    </div>
  );
}
