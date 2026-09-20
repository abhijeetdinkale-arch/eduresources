import React, { useState } from 'react';
import { X, Check, Copy, CheckCheck, MessageCircle, Sparkles, ArrowRight, Star, Flame, Crown } from 'lucide-react';

const PLANS = [
  {
    id: 'starter',
    name: 'Starter Pass',
    price: '₹299',
    duration: 'Single Semester',
    badge: null,
    highlight: false,
    desc: 'Essential textbook & notes access for single semester exam prep.',
    features: [
      'Core Course Textbooks',
      'Basic Question Bank Sets',
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
    desc: 'Complete unlimited access to all 9+ course dossiers, exam companions & handwritten notes.',
    features: [
      'All 9+ Course Repositories (PHY110, PHY175, CSE111, CSE326, MTH165, INT335, INT108, ECE, MEC)',
      'CA1, CA2, Midterm & Endterm Exam Companion Blueprints',
      'Full 300+ MCQ Question Banks & Step-by-Step Solutions',
      'Clean Handwritten Revision Notes & Lecture PPT Slides',
      'Offline Desktop & Mobile App Access',
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
    desc: 'Lifetime access to all current and future engineering & computing semester archives.',
    features: [
      'Everything in Pro All-Access Pass',
      'Lifetime Access to All 4 Years & Future Updates',
      'Direct 1-on-1 Exam Doubt Clearing on WhatsApp',
      'Early Access to New Question Banks & Sample Papers',
      'VIP Priority Access Line',
    ],
  },
];

export default function PlansModal({ isOpen, onClose, user }) {
  const [selectedPlan, setSelectedPlan] = useState('pro');
  const [copiedUpi, setCopiedUpi] = useState(false);
  const upiId = 'abhijeetdinkale@oksbi';
  const whatsappNumber = '917666937049';

  if (!isOpen) return null;

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
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-ink-950/75 backdrop-blur-md overflow-y-auto">
      <div className="relative w-full max-w-4xl bg-paper-50 dark:bg-darkbg-850 border border-paper-300 dark:border-darkbg-border rounded-[36px] p-6 sm:p-10 shadow-floating my-8 animate-in fade-in zoom-in duration-200 overflow-hidden">
        {/* Punch Holes */}
        <div className="absolute top-4 left-4 punch-hole"></div>
        <div className="absolute top-4 right-4 punch-hole"></div>

        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-6 right-6 p-2 rounded-full text-ink-400 hover:text-ink-900 dark:hover:text-paper-100 hover:bg-paper-200 dark:hover:bg-darkbg-700 transition"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header */}
        <div className="text-center mb-8 pt-2">
          <div className="inline-flex items-center gap-1.5 px-3.5 py-1 rounded-full bg-ochre-400/20 text-ochre-500 text-[10px] font-mono tracking-widest uppercase mb-3 border border-ochre-400/30 font-bold">
            <Sparkles className="w-3 h-3" />
            <span>SELECT YOUR ACADEMIC PASS</span>
          </div>
          <h2 className="text-3xl font-cinzel font-black text-ink-900 dark:text-paper-50 mb-2">
            Curriculum Access Passes
          </h2>
          <p className="text-xs sm:text-sm font-sans text-ink-600 dark:text-ink-400 max-w-lg mx-auto leading-relaxed">
            Unlock certified syllabus textbooks, high-yield question banks, and complete exam companion sets.
          </p>
        </div>

        {/* 3-Plan Cards Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-5 mb-8">
          {PLANS.map((plan) => (
            <div
              key={plan.id}
              onClick={() => setSelectedPlan(plan.id)}
              className={`relative rounded-[28px] p-6 transition-all duration-300 cursor-pointer flex flex-col justify-between ${
                plan.highlight
                  ? 'bg-paper-100 dark:bg-darkbg-900 border-2 border-[#E5C05B] shadow-xl md:-translate-y-2 ring-4 ring-[#E5C05B]/10'
                  : 'bg-paper-50 dark:bg-darkbg-800 border border-paper-300 dark:border-darkbg-border hover:border-ink-900 dark:hover:border-paper-200'
              } ${selectedPlan === plan.id ? 'ring-2 ring-ink-900 dark:ring-paper-50' : ''}`}
            >
              {/* Badge for Pro Plan */}
              {plan.badge && (
                <div className="absolute -top-3.5 left-1/2 -translate-x-1/2 bg-[#E5C05B] text-ink-950 text-[10px] font-mono font-black tracking-wider uppercase px-3 py-1 rounded-full shadow-md whitespace-nowrap">
                  {plan.badge}
                </div>
              )}

              <div>
                <div className="flex items-center justify-between mb-2">
                  <h3 className="font-cinzel font-bold text-lg text-ink-900 dark:text-paper-50">
                    {plan.name}
                  </h3>
                  {plan.discount && (
                    <span className="text-[10px] font-mono font-bold text-terracotta-600 bg-terracotta-500/10 px-2 py-0.5 rounded-full">
                      {plan.discount}
                    </span>
                  )}
                </div>

                <p className="text-[11px] font-sans text-ink-600 dark:text-ink-400 mb-4 min-h-[32px]">
                  {plan.desc}
                </p>

                <div className="flex items-baseline gap-1.5 border-b border-paper-300 dark:border-darkbg-border pb-4 mb-4">
                  <span className="text-3xl font-cinzel font-black text-ink-900 dark:text-paper-50">
                    {plan.price}
                  </span>
                  <span className="text-xs font-mono text-ink-500 dark:text-ink-400">
                    / {plan.duration}
                  </span>
                </div>

                {/* Features list */}
                <div className="space-y-2 text-xs text-ink-800 dark:text-paper-200 mb-6">
                  {plan.features.map((feat, i) => (
                    <div key={i} className="flex items-start gap-2">
                      <Check className={`w-4 h-4 shrink-0 mt-0.5 ${plan.highlight ? 'text-ochre-500 font-bold' : 'text-emerald-600'}`} />
                      <span className="leading-snug text-[11px]">{feat}</span>
                    </div>
                  ))}
                </div>
              </div>

              <button
                onClick={(e) => {
                  e.stopPropagation();
                  setSelectedPlan(plan.id);
                }}
                className={`w-full py-2.5 rounded-full text-xs font-semibold uppercase tracking-wider transition ${
                  selectedPlan === plan.id
                    ? plan.highlight
                      ? 'bg-[#E5C05B] text-ink-950 shadow-md font-bold'
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
        <div className="bg-paper-100 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-3xl p-5 sm:p-6 mb-6">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 mb-4">
            <div>
              <span className="text-xs font-mono text-ink-500 dark:text-ink-400 uppercase tracking-widest block">
                SELECTED PASS:
              </span>
              <div className="flex items-baseline gap-2">
                <span className="text-xl font-cinzel font-bold text-ink-900 dark:text-paper-50">
                  {activePlanObj.name}
                </span>
                <span className="text-2xl font-cinzel font-black text-ochre-500">
                  {activePlanObj.price}
                </span>
                <span className="text-xs font-mono text-ink-500">({activePlanObj.duration})</span>
              </div>
            </div>

            <div className="flex items-center gap-2 bg-paper-50 dark:bg-darkbg-800 px-3.5 py-2 rounded-2xl border border-paper-300 dark:border-darkbg-border">
              <span className="text-[11px] font-mono text-ink-500 dark:text-ink-400">UPI ID:</span>
              <button
                onClick={handleCopyUpi}
                className="flex items-center gap-1.5 font-mono text-xs font-bold text-ink-900 dark:text-paper-100 hover:text-ochre-500 transition"
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
            className="w-full py-4 px-6 bg-emerald-600 hover:bg-emerald-500 text-white rounded-2xl text-xs font-bold tracking-wider uppercase transition shadow-lg shadow-emerald-600/25 flex items-center justify-center gap-2 text-center"
          >
            <MessageCircle className="w-4 h-4" />
            <span>Pay {activePlanObj.price} & Instant WhatsApp Activation (+91 7666937049)</span>
            <ArrowRight className="w-4 h-4" />
          </a>
        </div>

        {/* Contact info bar */}
        <div className="pt-3 border-t border-dashed border-paper-300 dark:border-darkbg-border flex flex-wrap items-center justify-between text-[11px] font-mono text-ink-500 dark:text-ink-400 gap-2">
          <span>Direct Coordinator: <strong>Abhijeet Dinkale</strong></span>
          <span>📞 +91 7666937049</span>
          <span>✉️ arcnyz@gmail.com</span>
        </div>
      </div>
    </div>
  );
}
