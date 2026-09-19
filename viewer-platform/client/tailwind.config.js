/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      fontFamily: {
        serif: ['"Instrument Serif"', 'Georgia', 'serif'],
        cinzel: ['"Cinzel"', 'serif'],
        sans: ['"Plus Jakarta Sans"', 'system-ui', 'sans-serif'],
        mono: ['"Space Mono"', 'monospace'],
      },
      colors: {
        paper: {
          50: '#FDFBF7',
          100: '#F5F2EB',
          200: '#EAE5D9',
          300: '#DDD6C5',
          400: '#C5BCAC',
        },
        ink: {
          50: '#F4F4F5',
          100: '#E4E4E7',
          400: '#A1A1AA',
          600: '#52525B',
          800: '#27272A',
          900: '#18181B',
          950: '#0E0E10',
        },
        darkbg: {
          950: '#08080A',
          900: '#0C0C0E',
          850: '#121215',
          800: '#18181D',
          700: '#24242B',
          border: '#2A2A33',
        },
        terracotta: {
          500: '#C86452',
          600: '#B85342',
        },
        ochre: {
          400: '#E5C05B',
          500: '#D4AF37',
        }
      },
      boxShadow: {
        'ticket': '0 10px 25px -5px rgba(24, 24, 27, 0.07), 0 8px 10px -6px rgba(24, 24, 27, 0.05)',
        'ticket-dark': '0 10px 30px -5px rgba(0, 0, 0, 0.5), 0 0 0 1px rgba(255, 255, 255, 0.05)',
        'pill': '0 4px 20px -2px rgba(24, 24, 27, 0.08)',
        'pill-dark': '0 4px 25px -2px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.08)',
        'floating': '0 20px 40px -15px rgba(24, 24, 27, 0.15)',
      }
    },
  },
  plugins: [],
}
