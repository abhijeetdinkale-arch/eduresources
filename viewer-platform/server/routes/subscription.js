const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');
const { authGuard } = require('../middleware/authGuard');

const SUBSCRIBERS_FILE = path.resolve(__dirname, '../data/subscribers.json');

function getSubscribers() {
  try {
    if (fs.existsSync(SUBSCRIBERS_FILE)) {
      const data = JSON.parse(fs.readFileSync(SUBSCRIBERS_FILE, 'utf-8'));
      return data.subscribers || [];
    }
  } catch (e) {
    console.error('Error reading subscribers:', e);
  }
  return [];
}

function saveSubscribers(list) {
  try {
    fs.writeFileSync(SUBSCRIBERS_FILE, JSON.stringify({ subscribers: list }, null, 2));
  } catch (e) {
    console.error('Error saving subscribers:', e);
  }
}

// Check subscription status
router.get('/status', (req, res) => {
  let email = req.query.email;
  if (!email && req.user) email = req.user.email;

  const subscribers = getSubscribers();
  const isSubscribed = email ? subscribers.includes(email.toLowerCase().trim()) : false;

  res.json({
    isSubscribed,
    email,
    plan: isSubscribed ? 'Semester Curriculum Pass' : 'Free Preview',
    price: '₹300',
    upiId: 'abhijeetdinkale@oksbi',
    phone: '+91 7666937049',
    coordinator: 'Abhijeet Dinkale',
  });
});

// Admin add subscriber
router.post('/admin/add', (req, res) => {
  const { email } = req.body;
  if (!email) return res.status(400).json({ error: 'Email required' });

  const subscribers = getSubscribers();
  const normalized = email.toLowerCase().trim();
  if (!subscribers.includes(normalized)) {
    subscribers.push(normalized);
    saveSubscribers(subscribers);
  }

  res.json({ success: true, subscribers });
});

module.exports = { router, getSubscribers };
