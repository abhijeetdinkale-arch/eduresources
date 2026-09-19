const express = require('express');
const router = express.Router();
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const WORKSPACE_ROOT = path.resolve(__dirname, '../../..');

function formatBytes(bytes) {
  if (!bytes || bytes === 0) return '0 B';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(1)) + ' ' + sizes[i];
}

function classifyPdf(relPath, fileName) {
  const parts = relPath.split(path.sep);
  const topFolder = parts[0] || '';
  const subFolder = parts.length > 2 ? parts[1] : '';

  let courseCode = 'GENERAL';
  if (topFolder.startsWith('CSE111')) courseCode = 'CSE111';
  else if (topFolder.startsWith('CSE326')) courseCode = 'CSE326';
  else if (topFolder.startsWith('INT335')) courseCode = 'INT335';
  else if (topFolder.startsWith('INT108')) courseCode = 'INT108';
  else if (topFolder.startsWith('MTH165')) courseCode = 'MTH165';
  else if (topFolder.startsWith('ECE249')) courseCode = 'ECE249';
  else if (topFolder.startsWith('ECE279')) courseCode = 'ECE279';
  else if (topFolder.startsWith('MEC136')) courseCode = 'MEC136';
  else if (topFolder.startsWith('Physics')) {
    if (topFolder.includes('Question_Bank') || topFolder.includes('Formula_Book') || fileName.includes('phy175')) {
      courseCode = 'PHY175';
    } else {
      courseCode = 'PHY110';
    }
  }

  let category = 'Study Material';
  if (topFolder.includes('Exam_Companion') || fileName.includes('Exam_Companion')) {
    category = 'Exam Companion';
  } else if (topFolder.includes('Question_Bank') || fileName.includes('Question_Bank') || fileName.includes('qb')) {
    category = 'Question Bank';
  } else if (topFolder.includes('Handwritten_Notes') || fileName.includes('Handwritten')) {
    category = 'Handwritten Notes';
  } else if (topFolder.includes('Sample_Question_Papers') || fileName.includes('Sample')) {
    category = 'Sample Question Papers';
  } else if (topFolder.includes('Formula_Book') || fileName.includes('Formula')) {
    category = 'Formula Book';
  } else if (topFolder.includes('Essential_Book') || topFolder.includes('Revision_Book') || fileName.includes('TEXTBOOK') || fileName.includes('main.pdf')) {
    category = 'Textbook';
  }

  let title = fileName.replace(/\.pdf$/i, '').replace(/_/g, ' ');
  if (title.toLowerCase() === 'main') {
    title = `${topFolder.replace(/_/g, ' ')}`;
  }
  if (subFolder && (subFolder === 'midterm' || subFolder === 'endterm' || subFolder === 'ca1' || subFolder === 'ca2')) {
    title = `${courseCode} ${category} (${subFolder.toUpperCase()})`;
  }

  return { courseCode, category, title };
}

function scanPdfFiles(dir, baseDir = dir) {
  let results = [];
  try {
    const list = fs.readdirSync(dir);
    for (const item of list) {
      if (item === 'node_modules' || item === '.git' || item === 'viewer-platform' || item === '.gemini' || item === 'pdf_verifier') {
        continue;
      }
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);

      if (stat.isDirectory()) {
        results = results.concat(scanPdfFiles(fullPath, baseDir));
      } else if (item.toLowerCase().endsWith('.pdf') && stat.size > 1000) {
        const relPath = path.relative(baseDir, fullPath);
        const { courseCode, category, title } = classifyPdf(relPath, item);
        const id = crypto.createHash('md5').update(relPath).digest('hex').substring(0, 16);

        results.push({
          id,
          title,
          courseCode,
          category,
          relativePath: relPath,
          size: stat.size,
          sizeFormatted: formatBytes(stat.size),
          lastModified: stat.mtime,
        });
      }
    }
  } catch (err) {
    console.error('Directory scan error:', err);
  }
  return results;
}

let cachedMaterials = null;
let lastScanTime = 0;

function getMaterialsList() {
  const now = Date.now();
  if (!cachedMaterials || now - lastScanTime > 30000) {
    cachedMaterials = scanPdfFiles(WORKSPACE_ROOT);
    cachedMaterials.sort((a, b) => {
      if (a.courseCode !== b.courseCode) return a.courseCode.localeCompare(b.courseCode);
      return a.title.localeCompare(b.title);
    });
    lastScanTime = now;
  }
  return cachedMaterials;
}

router.get('/', (req, res) => {
  const materials = getMaterialsList();
  const { course, category, search } = req.query;

  let filtered = materials;
  if (course && course !== 'All') {
    filtered = filtered.filter((m) => m.courseCode.toLowerCase() === course.toLowerCase());
  }
  if (category && category !== 'All') {
    filtered = filtered.filter((m) => m.category.toLowerCase() === category.toLowerCase());
  }
  if (search) {
    const q = search.toLowerCase();
    filtered = filtered.filter(
      (m) =>
        m.title.toLowerCase().includes(q) ||
        m.courseCode.toLowerCase().includes(q) ||
        m.category.toLowerCase().includes(q)
    );
  }

  res.json({
    total: filtered.length,
    materials: filtered,
  });
});

router.get('/:id', (req, res) => {
  const materials = getMaterialsList();
  const doc = materials.find((m) => m.id === req.params.id);
  if (!doc) {
    return res.status(404).json({ error: 'Document not found' });
  }
  res.json(doc);
});

module.exports = { router, getMaterialsList, WORKSPACE_ROOT };
