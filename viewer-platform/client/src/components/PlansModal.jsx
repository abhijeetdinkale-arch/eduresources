import React, { useState, useEffect } from 'react';
import { X, Check, Copy, CheckCheck, MessageCircle, Sparkles, ArrowRight } from 'lucide-react';

const PLANS = [
  {
    id: 'starter',
    name: 'Starter Pass',
    price: '₹299',
    duration: 'Single Semester',
    badge: null,
    highlight: false,
    desc: 'Essential syllabus textbooks & quick cheatsheets for 1 semester.',
    features: [
      'Core Course Basic Textbooks',
      'Formula Books & Cheatsheets',
      'In-App DRM Digital Reader',
      'Email Support',
    ],
  },
  {
    id: 'pro',
    name: 'Pro All-Access',
    price: '₹499',
    duration: 'Full Year',
    badge: '🔥 POPULAR',
    highlight: true,
    discount: 'SAVE 50%',
    desc: 'Complete academic year vault with PYQs, sample papers & all 9+ subjects.',
    features: [
      'Everything in Starter Pass',
      'All 9+ Course Codes (PHY, CSE, MTH...)',
      'Official PYQ Sets & Sample Papers',
      'CA1, CA2 & Endterm Companions',
      'Direct WhatsApp Activation',
    ],
  },
  {
    id: 'vip',
    name: 'Lifetime Degree',
    price: '₹999',
    duration: '4-Year Lifetime',
    badge: '👑 VIP',
    highlight: false,
    desc: 'All 4 years degree access with instant priority support and updates.',
    features: [
      'Everything in Pro (4-Year Lifetime)',
      'Future AI / LLM Study Assistant',
      'Academic Queries Solved in 1 Day',
      'Request Any Topic On-Demand',
      'Direct 1-on-1 VIP Support',
    ],
  },
];

export default function PlansModal({ isOpen, onClose, user }) {
  const [selectedPlan, setSelectedPlan] = useState('pro');
  const [copiedUpi, setCopiedUpi] = useState(false);
  const upiId = 'abhijeetdinkale@oksbi';
  const whatsappNumber = '917666937049';

  // Listen to Escape key
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
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* 1. Backdrop Overlay (Click anywhere outside to close) */}
      <div
        onClick={onClose}
        className="fixed inset-0 bg-black/80 dark:bg-black/85 backdrop-blur-md transition-opacity cursor-pointer animate-in fade-in duration-200"
        title="Click anywhere outside to close"
      />

      {/* 2. Independent Top-Right Floating Close Button (ALWAYS 100% visible on screen) */}
      <button
        onClick={onClose}
        className="fixed top-4 right-4 sm:top-6 sm:right-8 z-[70] flex items-center gap-1.5 px-4 py-2 rounded-full bg-paper-50 dark:bg-darkbg-800 text-ink-900 dark:text-paper-50 hover:bg-terracotta-500 hover:text-white dark:hover:bg-terracotta-500 transition-all font-mono text-xs font-bold shadow-2xl border border-paper-300 dark:border-darkbg-border cursor-pointer group animate-in fade-in duration-200"
        title="Close (Escape key or click outside)"
      >
        <X className="w-4 h-4 group-hover:rotate-90 transition-transform" />
        <span>CLOSE (✕)</span>
      </button>

      {/* 3. Compact Modal Dialog Box */}
      <div
        onClick={(e) => e.stopPropagation()}
        className="relative z-[60] w-full max-w-3xl max-h-[88vh] mx-3 sm:mx-6 flex flex-col bg-paper-50 dark:bg-darkbg-850 border border-paper-300 dark:border-darkbg-border rounded-[28px] shadow-floating cursor-default animate-in fade-in zoom-in-95 duration-200 overflow-hidden"
      >
        {/* Modal Top Header with Title & Cross Button */}
        <div className="flex items-center justify-between px-5 py-3.5 bg-paper-100/90 dark:bg-darkbg-900/90 border-b border-paper-300/80 dark:border-darkbg-border shrink-0">
          <div className="flex items-center gap-2">
            <div className="w-5 h-5 rounded-full bg-ink-900 dark:bg-paper-50 flex items-center justify-center p-0.5">
              <img src="/logo.png" alt="Star" className="w-full h-full object-contain filter invert dark:invert-0" />
            </div>
            <span className="text-xs font-mono font-bold text-ink-900 dark:text-paper-100 tracking-wider uppercase">
              Curriculum Access Passes
            </span>
          </div>

          <button
            onClick={onClose}
            className="p-1.5 rounded-full hover:bg-paper-300 dark:hover:bg-darkbg-700 text-ink-700 dark:text-paper-300 transition"
            title="Close modal"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Scrollable Content Pane */}
        <div className="overflow-y-auto p-4 sm:p-6 space-y-4">
          {/* Header Subtitle */}
          <div className="text-center">
            <div className="inline-flex items-center gap-1.5 px-3 py-0.5 rounded-full bg-ochre-400/15 text-ochre-500 text-[10px] font-mono tracking-widest uppercase mb-1 border border-ochre-400/30 font-bold">
              <Sparkles className="w-3 h-3" />
              <span>OFFICIAL STUDENT PLANS</span>
            </div>
            <h2 className="text-xl sm:text-2xl font-cinzel font-black text-ink-900 dark:text-paper-50 mb-1">
              Select Your Academic Pass
            </h2>
            <p className="text-xs font-sans text-ink-600 dark:text-ink-400 max-w-md mx-auto">
              Unlock certified curriculum books, verified question banks, and complete exam companion sets.
            </p>
          </div>

          {/* 3 Compact Pricing Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3.5 pt-1">
            {PLANS.map((plan) => (
              <div
                key={plan.id}
                onClick={() => setSelectedPlan(plan.id)}
                className={`relative rounded-2xl p-4 transition-all duration-200 cursor-pointer flex flex-col justify-between ${
                  plan.highlight
                    ? 'bg-paper-100 dark:bg-darkbg-900 border-2 border-[#E5C05B] shadow-md ring-2 ring-[#E5C05B]/20'
                    : 'bg-paper-50 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border hover:border-ink-900 dark:hover:border-paper-200'
                } ${selectedPlan === plan.id ? 'ring-2 ring-ink-900 dark:ring-paper-50' : ''}`}
              >
                {plan.badge && (
                  <div className="absolute -top-2.5 left-1/2 -translate-x-1/2 bg-[#E5C05B] text-ink-950 text-[9px] font-mono font-black tracking-wider uppercase px-2 py-0.5 rounded-full shadow-xs whitespace-nowrap">
                    {plan.badge}
                  </div>
                )}

                <div>
                  <div className="flex items-center justify-between mb-1">
                    <h3 className="font-cinzel font-bold text-sm text-ink-900 dark:text-paper-50">
                      {plan.name}
                    </h3>
                    {plan.discount && (
                      <span className="text-[9px] font-mono font-bold text-terracotta-600 bg-terracotta-500/10 px-1.5 py-0.5 rounded-full">
                        {plan.discount}
                      </span>
                    )}
                  </div>

                  <p className="text-[10px] font-sans text-ink-600 dark:text-ink-400 mb-2.5 min-h-[24px] leading-tight">
                    {plan.desc}
                  </p>

                  <div className="flex items-baseline gap-1 border-b border-paper-300/80 dark:border-darkbg-border pb-2.5 mb-2.5">
                    <span className="text-xl sm:text-2xl font-cinzel font-black text-ink-900 dark:text-paper-50">
                      {plan.price}
                    </span>
                    <span className="text-[10px] font-mono text-ink-500 dark:text-ink-400">
                      / {plan.duration}
                    </span>
                  </div>

                  {/* Feature Bullets */}
                  <div className="space-y-1 text-xs text-ink-800 dark:text-paper-200 mb-4">
                    {plan.features.map((feat, i) => (
                      <div key={i} className="flex items-start gap-1.5">
                        <Check className={`w-3.5 h-3.5 shrink-0 mt-0.5 ${plan.highlight ? 'text-ochre-500 font-bold' : 'text-emerald-600'}`} />
                        <span className="leading-tight text-[10px]">{feat}</span>
                      </div>
                    ))}
                  </div>
                </div>

                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    setSelectedPlan(plan.id);
                  }}
                  className={`w-full py-1.5 rounded-full text-[11px] font-semibold uppercase tracking-wider transition ${
                    selectedPlan === plan.id
                      ? plan.highlight
                        ? 'bg-[#E5C05B] text-ink-950 shadow-xs font-bold'
                        : 'bg-ink-900 dark:bg-paper-50 text-paper-50 dark:text-ink-900'
                      : 'bg-paper-200 dark:bg-darkbg-700 text-ink-700 dark:text-paper-300 hover:bg-paper-300'
                  }`}
                >
                  {selectedPlan === plan.id ? 'Selected ✓' : 'Select'}
                </button>
              </div>
            ))}
          </div>

          {/* Compact Payment Action Box */}
          <div className="bg-paper-100 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-xl p-3.5 sm:p-4">
            <div className="flex flex-col sm:flex-row items-center justify-between gap-2.5 mb-2.5">
              <div className="flex items-baseline gap-2">
                <span className="text-[10px] font-mono text-ink-500 dark:text-ink-400 uppercase">Selected:</span>
                <span className="text-sm font-cinzel font-bold text-ink-900 dark:text-paper-50">
                  {activePlanObj.name}
                </span>
                <span className="text-base font-cinzel font-black text-ochre-500">
                  {activePlanObj.price}
                </span>
              </div>

              <div className="flex items-center gap-1.5 bg-paper-50 dark:bg-darkbg-800 px-3 py-1 rounded-lg border border-paper-300 dark:border-darkbg-border">
                <span className="text-[10px] font-mono text-ink-500 dark:text-ink-400">UPI:</span>
                <button
                  onClick={handleCopyUpi}
                  className="flex items-center gap-1 font-mono text-xs font-bold text-ink-900 dark:text-paper-100 hover:text-ochre-500 transition"
                  title="Copy UPI ID"
                >
                  <span>{upiId}</span>
                  {copiedUpi ? <CheckCheck className="w-3 h-3 text-emerald-600" /> : <Copy className="w-3 h-3 text-ink-400" />}
                </button>
              </div>
            </div>

            {/* Instant WhatsApp activation button */}
            <a
              href={`https://wa.me/${whatsappNumber}?text=${whatsappMessage}`}
              target="_blank"
              rel="noopener noreferrer"
              className="w-full py-2.5 px-4 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl text-xs font-bold tracking-wider uppercase transition shadow-sm flex items-center justify-center gap-2 text-center"
            >
              <MessageCircle className="w-4 h-4" />
              <span>Pay {activePlanObj.price} & Instant WhatsApp Activation (+91 7666937049)</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </a>
          </div>

          {/* Coordinator Footer */}
          <div className="pt-1 text-center text-[10px] font-mono text-ink-500 dark:text-ink-400">
            <span>Direct Coordinator: Abhijeet Dinkale • 📞 +91 7666937049 • ✉️ arcnyz@gmail.com</span>
          </div>
        </div>
      </div>
    </div>
  );
}
