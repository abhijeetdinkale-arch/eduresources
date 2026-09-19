const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');
const { OAuth2Client } = require('google-auth-library');
const { JWT_SECRET } = require('../middleware/authGuard');

// Return public auth config
router.get('/config', (req, res) => {
  const googleClientId = process.env.GOOGLE_CLIENT_ID || '';
  res.json({
    googleClientId: googleClientId,
    demoModeEnabled: true,
  });
});

// Google OAuth Login
router.post('/google', async (req, res) => {
  const { credential } = req.body;
  if (!credential) {
    return res.status(400).json({ message: 'Missing Google credential token' });
  }

  try {
    let payload;

    const googleClientId = process.env.GOOGLE_CLIENT_ID;
    if (googleClientId) {
      const client = new OAuth2Client(googleClientId);
      const ticket = await client.verifyIdToken({
        idToken: credential,
        audience: googleClientId,
      });
      payload = ticket.getPayload();
    } else {
      // Fallback decode for development/testing if no Client ID is configured yet
      payload = jwt.decode(credential);
    }

    if (!payload || !payload.email) {
      return res.status(400).json({ message: 'Invalid Google token payload' });
    }

    const user = {
      id: payload.sub || `USR-${Math.random().toString(36).substring(2, 9).toUpperCase()}`,
      email: payload.email,
      name: payload.name || payload.email.split('@')[0],
      picture: payload.picture || null,
      ip: req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1',
    };

    const token = jwt.sign(user, JWT_SECRET, { expiresIn: '7d' });

    res.cookie('auth_token', token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: 7 * 24 * 60 * 60 * 1000,
    });

    res.json({ user, token });
  } catch (err) {
    console.error('Google Auth Error:', err);
    res.status(401).json({ message: 'Google Authentication verification failed: ' + err.message });
  }
});

// Demo/Test Student Login
router.post('/demo', (req, res) => {
  const { name, email } = req.body;
  const studentEmail = email || 'student@university.edu';
  const studentName = name || 'Student User';

  const user = {
    id: `STU-${Math.random().toString(36).substring(2, 8).toUpperCase()}`,
    email: studentEmail,
    name: studentName,
    picture: null,
    ip: req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1',
  };

  const token = jwt.sign(user, JWT_SECRET, { expiresIn: '7d' });

  res.cookie('auth_token', token, {
    httpOnly: true,
    secure: process.env.NODE_ENV === 'production',
    sameSite: 'lax',
    maxAge: 7 * 24 * 60 * 60 * 1000,
  });

  res.json({ user, token });
});

// Current User Info
router.get('/me', (req, res) => {
  let token = req.cookies?.auth_token;
  if (!token && req.headers.authorization?.startsWith('Bearer ')) {
    token = req.headers.authorization.split(' ')[1];
  }

  if (!token) {
    return res.status(401).json({ user: null });
  }

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    // Refresh client IP
    decoded.ip = req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1';
    res.json(decoded);
  } catch (err) {
    res.status(401).json({ user: null });
  }
});

// Logout
router.post('/logout', (req, res) => {
  res.clearCookie('auth_token');
  res.json({ success: true });
});

module.exports = router;
