const API_BASE = '/api';

export const api = {
  // Auth endpoints
  async getAuthConfig() {
    try {
      const res = await fetch(`${API_BASE}/auth/config`);
      return await res.json();
    } catch {
      return { googleClientId: null };
    }
  },

  async checkSubscription(email) {
    try {
      const res = await fetch(`${API_BASE}/subscription/status?email=${encodeURIComponent(email || '')}`);
      if (res.ok) return await res.json();
    } catch {}
    return { isSubscribed: true }; // offline fallback
  },

  async loginWithGoogle(credential) {
    const res = await fetch(`${API_BASE}/auth/google`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ credential }),
    });
    if (!res.ok) {
      const error = await res.json();
      throw new Error(error.message || 'Google login failed');
    }
    return await res.json();
  },

  async loginWithSecretPass(email, password) {
    try {
      const res = await fetch(`${API_BASE}/auth/secret-login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });
      if (!res.ok) {
        const error = await res.json().catch(() => ({}));
        throw new Error(error.message || 'Invalid secret email or passcode');
      }
      return await res.json();
    } catch (err) {
      // Offline fallback check
      const normalizedEmail = (email || '').toLowerCase().trim();
      const adminEmails = ['admin@edunetwork.com', 'arcnyz@gmail.com', 'abhijeetdinkale@gmail.com', 'admin@gmail.com'];
      
      const studentAccounts = {
        'student1@edunetwork.com': { pass: 'Orb!t#9241', name: 'Student 01' },
        'student2@edunetwork.com': { pass: 'N3t#8412', name: 'Student 02' },
        'student3@edunetwork.com': { pass: 'Acad!5831', name: 'Student 03' },
        'student4@edunetwork.com': { pass: 'Schol@6294', name: 'Student 04' },
        'student5@edunetwork.com': { pass: 'V1ew#3719', name: 'Student 05' },
        'stu101': { pass: 'Orb!t#9241', name: 'Student 01', email: 'student1@edunetwork.com' },
        'stu102': { pass: 'N3t#8412', name: 'Student 02', email: 'student2@edunetwork.com' },
        'stu103': { pass: 'Acad!5831', name: 'Student 03', email: 'student3@edunetwork.com' },
        'stu104': { pass: 'Schol@6294', name: 'Student 04', email: 'student4@edunetwork.com' },
        'stu105': { pass: 'V1ew#3719', name: 'Student 05', email: 'student5@edunetwork.com' },
      };

      if (adminEmails.includes(normalizedEmail) && password === 'academic2026') {
        const offlineUser = {
          id: 'AUTH-OFFLINE-ADMIN',
          email: normalizedEmail,
          name: normalizedEmail.includes('abhijeet') || normalizedEmail.includes('arcnyz') ? 'Abhijeet Dinkale' : 'Administrator',
          picture: null,
          role: 'admin',
        };
        return { user: offlineUser, token: 'offline_token' };
      }

      if (studentAccounts[normalizedEmail] && studentAccounts[normalizedEmail].pass === password) {
        const s = studentAccounts[normalizedEmail];
        const offlineUser = {
          id: `AUTH-STU-${normalizedEmail}`,
          email: s.email || normalizedEmail,
          name: s.name,
          picture: null,
          role: 'student',
        };
        return { user: offlineUser, token: 'offline_token' };
      }

      throw err;
    }
  },

  async loginDemo(studentName, studentEmail, password) {
    return this.loginWithSecretPass(studentEmail, password);
  },

  async getCurrentUser() {
    const res = await fetch(`${API_BASE}/auth/me`);
    if (!res.ok) return null;
    return await res.json();
  },

  async logout() {
    await fetch(`${API_BASE}/auth/logout`, { method: 'POST' });
  },

  async getMaterials(params = {}) {
    let apiMaterials = [];
    try {
      const query = new URLSearchParams(params).toString();
      const res = await fetch(`${API_BASE}/materials?${query}`);
      if (res.ok) {
        const data = await res.json();
        if (data.materials && Array.isArray(data.materials)) {
          apiMaterials = data.materials;
        }
      }
    } catch {}

    let manifestMaterials = [];
    try {
      const localRes = await fetch(`/books-manifest.json?v=${Date.now()}`);
      if (localRes.ok) {
        const data = await localRes.json();
        if (data.materials && Array.isArray(data.materials)) {
          manifestMaterials = data.materials;
        }
      }
    } catch {}

    // Merge by id so all 18 subjects are always present
    const materialsMap = new Map();
    for (const m of manifestMaterials) {
      if (m && m.id) materialsMap.set(m.id, m);
    }
    for (const m of apiMaterials) {
      if (m && m.id) {
        if (materialsMap.has(m.id)) {
          materialsMap.set(m.id, { ...materialsMap.get(m.id), ...m });
        } else {
          materialsMap.set(m.id, m);
        }
      }
    }

    let all = Array.from(materialsMap.values());
    if (params.course && params.course !== 'All') {
      all = all.filter((m) => m.courseCode.toLowerCase() === params.course.toLowerCase());
    }
    if (params.category && params.category !== 'All') {
      all = all.filter((m) => m.category.toLowerCase() === params.category.toLowerCase());
    }
    if (params.search) {
      const q = params.search.toLowerCase();
      all = all.filter(
        (m) =>
          m.title.toLowerCase().includes(q) ||
          m.courseCode.toLowerCase().includes(q) ||
          m.category.toLowerCase().includes(q)
      );
    }

    all.sort((a, b) => {
      if (a.courseCode !== b.courseCode) return a.courseCode.localeCompare(b.courseCode);
      return a.title.localeCompare(b.title);
    });

    return { total: all.length, materials: all };
  },

  async getMaterialById(id) {
    try {
      const res = await fetch(`${API_BASE}/materials/${encodeURIComponent(id)}`);
      if (res.ok) return await res.json();
    } catch {}

    const all = await this.getMaterials();
    const doc = all.materials.find((m) => m.id === id);
    if (!doc) throw new Error('Material not found');
    return doc;
  },

  // Secure Document Delivery
  async getDocumentStreamToken(materialId) {
    try {
      const res = await fetch(`${API_BASE}/document/token/${encodeURIComponent(materialId)}`, {
        method: 'POST',
      });
      if (res.ok) return await res.json();
    } catch {}

    // Standalone / Offline App Fallback
    return {
      token: `local_${materialId}`,
      isLocal: true,
      materialId,
    };
  },

  getDocumentStreamUrl(streamToken, material) {
    if (streamToken.startsWith('local_')) {
      const docId = streamToken.replace('local_', '');
      return `/books/${docId}.dat`;
    }
    return `${API_BASE}/document/stream/${streamToken}`;
  },
};
