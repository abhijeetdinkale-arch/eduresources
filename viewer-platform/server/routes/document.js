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

    // Check possible local and bundled paths
    const candidatePaths = [];
    if (decoded.relativePath) {
      candidatePaths.push(path.resolve(WORKSPACE_ROOT, decoded.relativePath));
      candidatePaths.push(path.resolve(__dirname, '../../../', decoded.relativePath));
      candidatePaths.push(path.resolve(__dirname, '../../', decoded.relativePath));
    }
    if (decoded.materialId) {
      candidatePaths.push(
        path.resolve(__dirname, '../../client/public/books', `${decoded.materialId}.dat`),
        path.resolve(__dirname, '../../client/dist/books', `${decoded.materialId}.dat`),
        path.resolve(__dirname, '../data/books', `${decoded.materialId}.dat`)
      );
    }

    const finalFilePath = candidatePaths.find((p) => p && fs.existsSync(p));

    if (finalFilePath) {
      const stat = fs.statSync(finalFilePath);
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
      return fs.createReadStream(finalFilePath).pipe(res);
    }

    // On Serverless / Edge Cloud (e.g. Vercel), redirect to the CDN-cached dat file
    if (decoded.materialId) {
      return res.redirect(302, `/books/${decoded.materialId}.dat`);
    }

    return res.status(404).json({ error: 'Document file not found' });
  } catch (err) {
    console.error('Stream verification error:', err);
    return res.status(403).json({ error: 'Stream token expired or invalid. Please re-open the document.' });
  }
});

module.exports = router;
