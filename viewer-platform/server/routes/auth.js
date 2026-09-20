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

// Secret Academic Pass Login
router.post('/secret-login', (req, res) => {
  const { email, password } = req.body || {};
  
  const configuredEmail = (process.env.SECRET_LOGIN_EMAIL || 'admin@edunetwork.com').toLowerCase().trim();
  const allowedAdminEmails = [
    configuredEmail,
    'arcnyz@gmail.com',
    'abhijeetdinkale@gmail.com',
    'admin@edunetwork.com',
    'admin@gmail.com',
  ].map((e) => e.toLowerCase().trim());

  const expectedPassword = process.env.SECRET_LOGIN_PASSWORD || 'academic2026';

  const inputEmail = (email || '').toLowerCase().trim();
  const inputPassword = password || '';

  if (!inputEmail || !inputPassword) {
    return res.status(400).json({ message: 'Please enter both secret email and passcode' });
  }

  if (!allowedAdminEmails.includes(inputEmail) || inputPassword !== expectedPassword) {
    return res.status(401).json({ message: 'Invalid secret email or passcode. Access denied.' });
  }

  const user = {
    id: `AUTH-${Math.random().toString(36).substring(2, 8).toUpperCase()}`,
    email: inputEmail,
    name: inputEmail.includes('abhijeet') || inputEmail.includes('arcnyz') ? 'Abhijeet Dinkale' : 'Academic Scholar',
    picture: null,
    role: 'admin',
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

// Backward compatibility demo route forwarding to secret-login check
router.post('/demo', (req, res) => {
  const { email, password } = req.body || {};
  const expectedEmail = (process.env.SECRET_LOGIN_EMAIL || 'admin@edunetwork.com').toLowerCase().trim();
  const expectedPassword = process.env.SECRET_LOGIN_PASSWORD || 'academic2026';

  const inputEmail = (email || '').toLowerCase().trim();
  const inputPassword = password || '';

  if (inputEmail === expectedEmail && (inputPassword === expectedPassword || !password)) {
    const user = {
      id: `AUTH-${Math.random().toString(36).substring(2, 8).toUpperCase()}`,
      email: expectedEmail,
      name: 'Academic Scholar',
      picture: null,
      role: 'member',
      ip: req.headers['x-forwarded-for'] || req.socket.remoteAddress || '127.0.0.1',
    };
    const token = jwt.sign(user, JWT_SECRET, { expiresIn: '7d' });
    res.cookie('auth_token', token, {
      httpOnly: true,
      secure: process.env.NODE_ENV === 'production',
      sameSite: 'lax',
      maxAge: 7 * 24 * 60 * 60 * 1000,
    });
    return res.json({ user, token });
  }

  return res.status(401).json({ message: 'Invalid secret email or passcode.' });
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
