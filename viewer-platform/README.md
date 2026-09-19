# 📚 Secure Study Material & Book Viewer Platform

A full-stack, enterprise-grade study platform where students log in with their Google account to read books, exam companions, question banks, and notes with **hardened Anti-Screenshot, Anti-Download, and Dynamic Forensic Watermark protection**.

---

## 🌟 Key Features

1. **🔐 Google Account Authentication**:
   - Google Sign-In (OAuth 2.0 / Google Identity Services).
   - Secure HTTP-only JWT sessions.
   - Built-in instant test/demo student sign-in for zero-config evaluation.

2. **🛡️ Multi-Layer Anti-Screenshot & Anti-Download DRM**:
   - **Forensic Dynamic Watermarking**: Every page is continuously stamped with a repeating 45° watermark containing the student's **Email**, **User ID**, **IP Address**, and **Live Clock Timestamp**.
   - **Canvas-Level Stamping**: The watermark is drawn directly into the HTML5 canvas pixel buffer (cannot be inspected or hidden in dev tools).
   - **Anti-Snipping & Focus-Loss Shield**: The moment a student opens a screen capture tool (Windows Snipping Tool, Mac `Cmd+Shift+4`, Lightshot, OBS) or unfocuses the browser, the viewer immediately blurs/blacks out with a security lock screen.
   - **Shortcut & Print Interception**: Blocks `Ctrl+S`, `Cmd+S`, `Ctrl+P`, `Cmd+P`, `PrintScreen`, `F12`, `Ctrl+Shift+I`, and `Cmd+Option+I`.
   - **Print Blanking CSS**: `@media print` rules ensure any print attempt results in a completely blank page.
   - **No Raw PDF Downloads**: PDFs are streamed via short-lived (5-minute) signed tokens directly to the canvas worker; raw static file URLs are never exposed.

3. **📖 Rich Document & Course Explorer**:
   - Auto-indexes all materials in your courses: **CSE111**, **CSE326**, **INT335**, **MTH165**, **Physics**, **ECE249**, **ECE279**, **INT108**, **MEC136**.
   - Categorized by Textbooks, Exam Companions, Question Banks, Handwritten Notes, and Sample Papers.
   - Fast instant search and course code filters.

---

## 🚀 Quick Start (Local Run)

### 1. Install Dependencies
```bash
cd viewer-platform
npm install
cd client && npm install
cd ..
```

### 2. Start the Backend & Frontend
In terminal 1 (Backend Server):
```bash
npm run server
```
*Backend runs on `http://localhost:5001`*

In terminal 2 (Frontend Client):
```bash
npm run client
```
*Frontend runs on `http://localhost:5173`*

---

## 🌐 100% Free Hosting & Free Cloud Storage Guide

### Step 1: Free Google OAuth Credentials (5 mins)
1. Go to [Google Cloud Console Credentials](https://console.cloud.google.com/apis/credentials).
2. Create a Project > Click **Create Credentials** > **OAuth client ID**.
3. Select **Web application**.
4. Add your domain (e.g. `http://localhost:5173` for local, or `https://your-app.vercel.app` for production) to **Authorized JavaScript origins**.
5. Copy your **Client ID** and add it to `viewer-platform/.env`:
   ```env
   GOOGLE_CLIENT_ID=your-client-id-here.apps.googleusercontent.com
   ```

---

### Step 2: Free Cloud Hosting (Choose either Vercel or Render)

#### Option A: Vercel (Recommended - Fastest & 100% Free)
1. Push this repository to **GitHub**.
2. Go to [Vercel](https://vercel.com) and click **Add New Project**.
3. Import your GitHub repository.
4. Set Root Directory to `viewer-platform`.
5. Set Build Command: `npm run build` and Output Directory: `client/dist`.
6. Add your Environment Variables (`GOOGLE_CLIENT_ID`, `JWT_SECRET`).
7. Click **Deploy** — your site is live with a free SSL domain!

#### Option B: Render.com (100% Free Web Service)
1. Push to GitHub.
2. Go to [Render](https://render.com) > **New Web Service**.
3. Set Build Command: `npm run install:all && npm run build`
4. Set Start Command: `npm start`
5. Click **Create Web Service**.

---

### Step 3: Free PDF Cloud Storage (If your files exceed 1 GB)

| Provider | Free Tier Storage | Egress Fees | Best For |
| :--- | :--- | :--- | :--- |
| **Supabase Storage** | **5 GB Free** | 0 fees | Easiest setup + built-in PostgreSQL & Auth |
| **Cloudflare R2** | **10 GB Free** | **0 fees (Unlimited)** | Best performance & completely free egress |
| **Direct Git Repo** | **1 - 2 GB Free** | 0 fees | Zero external setup (bundled directly in repo) |

---

## 🔒 Security Best Practices Implemented
- `X-Frame-Options: SAMEORIGIN` (prevents iframe clickjacking)
- `X-Content-Type-Options: nosniff` (prevents MIME sniffing)
- Ephemeral stream tokens (valid for only 300 seconds)
- Rate-limiting and path traversal sanitization
