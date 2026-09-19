import React, { useState, useEffect, useRef } from 'react';
import { X, Lock, User, Mail, AlertCircle, ArrowRight } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function LoginModal({ isOpen, onClose }) {
  const { googleClientId, loginWithGoogleCredential, loginWithDemo } = useAuth();
  const [demoName, setDemoName] = useState('Alex Student');
  const [demoEmail, setDemoEmail] = useState('alex.student@university.edu');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const googleBtnRef = useRef(null);

  useEffect(() => {
    if (!isOpen || !googleClientId) return;

    if (window.google?.accounts?.id && googleBtnRef.current) {
      window.google.accounts.id.initialize({
        client_id: googleClientId,
        callback: async (response) => {
          try {
            setLoading(true);
            setError(null);
            await loginWithGoogleCredential(response.credential);
            onClose();
          } catch (err) {
            setError(err.message || 'Google login failed');
          } finally {
            setLoading(false);
          }
        },
      });

      window.google.accounts.id.renderButton(googleBtnRef.current, {
        theme: 'filled_black',
        size: 'large',
        text: 'signin_with',
        shape: 'pill',
        width: '100%',
      });
    }
  }, [isOpen, googleClientId, loginWithGoogleCredential, onClose]);

  if (!isOpen) return null;

  const handleDemoSubmit = async (e) => {
    e.preventDefault();
    try {
      setLoading(true);
      setError(null);
      await loginWithDemo(demoName, demoEmail);
      onClose();
    } catch (err) {
      setError(err.message || 'Login failed');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-ink-950/70 backdrop-blur-md">
      <div className="relative w-full max-w-md bg-paper-50 dark:bg-darkbg-850 border border-paper-300 dark:border-darkbg-border rounded-[32px] p-6 sm:p-8 shadow-floating animate-in fade-in zoom-in duration-200 overflow-hidden">
        {/* Punch Hole Accents */}
        <div className="absolute top-4 left-4 punch-hole"></div>
        <div className="absolute top-4 right-4 punch-hole"></div>

        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-6 right-6 p-1.5 rounded-full text-ink-400 hover:text-ink-900 dark:hover:text-paper-100 hover:bg-paper-200 dark:hover:bg-darkbg-700 transition"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Header with Star Logo */}
        <div className="text-center mb-6 pt-2">
          <div className="w-12 h-12 rounded-full bg-ink-900 dark:bg-paper-50 flex items-center justify-center mx-auto mb-3 shadow-sm p-2">
            <img
              src="/logo.png"
              alt="Edu network star logo"
              className="w-full h-full object-contain filter invert dark:invert-0"
            />
          </div>
          <h2 className="text-xl font-cinzel font-bold text-ink-900 dark:text-paper-50 mb-0.5">
            Edu<span className="font-serif italic font-normal text-ink-600 dark:text-ink-400"> network</span>
          </h2>
          <p className="text-[11px] font-mono uppercase tracking-widest text-ink-400 dark:text-ink-500">
            MEMBER ACADEMIC KEYCARD
          </p>
        </div>

        {error && (
          <div className="mb-4 p-3 rounded-2xl bg-terracotta-500/10 border border-terracotta-500/30 text-terracotta-600 dark:text-terracotta-500 text-xs flex items-center gap-2">
            <AlertCircle className="w-4 h-4 shrink-0" />
            <span>{error}</span>
          </div>
        )}

        {/* Google Official Button */}
        <div className="space-y-4 mb-5">
          {googleClientId ? (
            <div ref={googleBtnRef} className="flex justify-center w-full min-h-[44px]"></div>
          ) : (
            <div className="p-3.5 rounded-2xl bg-paper-100 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border text-center">
              <div className="flex items-center justify-center gap-2 mb-1.5 text-xs font-semibold text-ink-900 dark:text-paper-100">
                <svg className="w-4 h-4" viewBox="0 0 24 24">
                  <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                  <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                  <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z"/>
                  <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z"/>
                </svg>
                <span>Real Google Account Sign-In Ready</span>
              </div>
              <p className="text-[11px] text-ink-500 dark:text-ink-400 leading-relaxed">
                Add your <code className="px-1 py-0.5 rounded bg-paper-200 dark:bg-darkbg-750 font-mono text-[10px]">GOOGLE_CLIENT_ID</code> in <code className="px-1 py-0.5 rounded bg-paper-200 dark:bg-darkbg-750 font-mono text-[10px]">.env</code> to activate live Google OAuth popup, or enter your Google email below.
              </p>
            </div>
          )}
          <div className="relative flex py-1 items-center">
            <div className="flex-grow border-t border-paper-300 dark:border-darkbg-border"></div>
            <span className="flex-shrink mx-3 text-[10px] font-mono uppercase tracking-wider text-ink-400">OR DIRECT EMAIL PASS</span>
            <div className="flex-grow border-t border-paper-300 dark:border-darkbg-border"></div>
          </div>
        </div>

        {/* Student Pass Form */}
        <form onSubmit={handleDemoSubmit} className="space-y-3.5">
          <div>
            <label className="block text-[11px] font-mono uppercase tracking-wider text-ink-600 dark:text-ink-400 mb-1">
              Student Full Name
            </label>
            <div className="relative">
              <User className="w-4 h-4 text-ink-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                required
                value={demoName}
                onChange={(e) => setDemoName(e.target.value)}
                placeholder="Student Name"
                className="w-full pl-10 pr-3.5 py-2.5 bg-paper-100 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-xl text-xs text-ink-900 dark:text-paper-100 placeholder-ink-400 focus:outline-none focus:ring-2 focus:ring-ink-900 dark:focus:ring-paper-200"
              />
            </div>
          </div>

          <div>
            <label className="block text-[11px] font-mono uppercase tracking-wider text-ink-600 dark:text-ink-400 mb-1">
              University Google Email
            </label>
            <div className="relative">
              <Mail className="w-4 h-4 text-ink-400 absolute left-3.5 top-1/2 -translate-y-1/2" />
              <input
                type="email"
                required
                value={demoEmail}
                onChange={(e) => setDemoEmail(e.target.value)}
                placeholder="student@university.edu"
                className="w-full pl-10 pr-3.5 py-2.5 bg-paper-100 dark:bg-darkbg-900 border border-paper-300 dark:border-darkbg-border rounded-xl text-xs text-ink-900 dark:text-paper-100 placeholder-ink-400 focus:outline-none focus:ring-2 focus:ring-ink-900 dark:focus:ring-paper-200"
              />
            </div>
          </div>

          <button
            type="submit"
            disabled={loading}
            className="w-full py-3 px-4 bg-ink-900 dark:bg-paper-100 hover:bg-black dark:hover:bg-white text-paper-50 dark:text-ink-900 rounded-xl text-xs font-semibold tracking-wider uppercase transition shadow-md flex items-center justify-center gap-2 mt-4"
          >
            <span>{loading ? 'Authenticating...' : 'Authorize Student Pass'}</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </form>

        {/* Perforated Barcode Footer */}
        <div className="mt-6 pt-4 border-t border-dashed border-paper-300 dark:border-darkbg-border flex items-center justify-between text-ink-600 dark:text-ink-400 text-xs">
          <div className="flex flex-col">
            <span className="text-[9px] font-mono text-ink-400 dark:text-ink-500 uppercase">SERIAL #EDU-PASS-2026</span>
            <div className="barcode text-[11px] font-bold text-ink-900 dark:text-paper-200 tracking-tight">
              ||| |||| | || |||||
            </div>
          </div>
          <div className="flex items-center gap-1 text-[10px] font-mono text-ink-500 dark:text-ink-400">
            <Lock className="w-3 h-3 text-emerald-600 dark:text-emerald-400" />
            <span>AUTHENTICATED PASS</span>
          </div>
        </div>
      </div>
    </div>
  );
}
