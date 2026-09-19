const express = require('express');
const router = express.Router();
const jwt = require('jsonwebtoken');
const fs = require('fs');
const path = require('path');
const { authGuard, JWT_SECRET } = require('../middleware/authGuard');
const { getMaterialsList, WORKSPACE_ROOT } = require('./materials');

// POST /api/document/token/:materialId - Issue single-use short-lived stream token
router.post('/token/:materialId', authGuard, (req, res) => {
  const { materialId } = req.params;
  const materials = getMaterialsList();
  const doc = materials.find((m) => m.id === materialId);

  if (!doc) {
    return res.status(404).json({ error: 'Document not found' });
  }

  // Create 5-minute expiring signed stream token
  const streamToken = jwt.sign(
    {
      materialId: doc.id,
      relativePath: doc.relativePath,
      userId: req.user.id,
      email: req.user.email,
      ip: req.user.ip,
    },
    JWT_SECRET,
    { expiresIn: '5m' }
  );

  res.json({
    token: streamToken,
    expiresInSeconds: 300,
  });
});

// GET /api/document/stream/:token - Stream secure document
router.get('/stream/:token', (req, res) => {
  const { token } = req.params;

  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    const filePath = path.resolve(WORKSPACE_ROOT, decoded.relativePath);

    // Path traversal check
    if (!filePath.startsWith(WORKSPACE_ROOT)) {
      return res.status(403).json({ error: 'Forbidden document path' });
    }

    if (!fs.existsSync(filePath)) {
      return res.status(404).json({ error: 'Document file not found on disk' });
    }

    const stat = fs.statSync(filePath);

    // Set anti-caching & secure headers
    res.writeHead(200, {
      'Content-Type': 'application/pdf',
      'Content-Length': stat.size,
      'Content-Disposition': 'inline; filename="protected-document.pdf"',
      'Cache-Control': 'no-store, no-cache, must-revalidate, private, proxy-revalidate',
      'Pragma': 'no-cache',
      'Expires': '0',
      'X-Content-Type-Options': 'nosniff',
      'X-Frame-Options': 'DENY',
    });

    const readStream = fs.createReadStream(filePath);
    readStream.pipe(res);
  } catch (err) {
    console.error('Stream token verification error:', err);
    return res.status(403).json({ error: 'Stream token expired or invalid. Please re-open the document.' });
  }
});

module.exports = router;
