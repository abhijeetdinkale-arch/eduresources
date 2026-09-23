const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const WORKSPACE_ROOT = path.resolve(__dirname, '..');
const TARGET_BOOKS_DIR = path.resolve(__dirname, 'client/public/books');
const MANIFEST_PATH = path.resolve(__dirname, 'client/public/books-manifest.json');

if (!fs.existsSync(TARGET_BOOKS_DIR)) {
  fs.mkdirSync(TARGET_BOOKS_DIR, { recursive: true });
}

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
    // Distinguish between PHY110 (Textbook & Exam Companion) and PHY175 (Question Bank & Formula Book)
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

function scanAndBundlePdfs(dir, baseDir = dir) {
  let results = [];
  try {
    const list = fs.readdirSync(dir);
    for (const item of list) {
      if (
        item === 'node_modules' ||
        item === '.git' ||
        item === 'viewer-platform' ||
        item === '.gemini' ||
        item === '.agents' ||
        item === 'android-app' ||
        item === 'release' ||
        item === 'dist' ||
        item === 'build' ||
        item === '.gradle' ||
        item === 'ios' ||
        item === 'android' ||
        item === 'pdf_verifier' ||
        item.startsWith('.')
      ) {
        continue;
      }
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);

      if (stat.isDirectory()) {
        results = results.concat(scanAndBundlePdfs(fullPath, baseDir));
      } else if (item.toLowerCase().endsWith('.pdf') && stat.size > 1000) {
        const relPath = path.relative(baseDir, fullPath);
        const { courseCode, category, title } = classifyPdf(relPath, item);
        const id = crypto.createHash('md5').update(relPath).digest('hex').substring(0, 16);

        const bundledFilename = `${id}.dat`;
        const targetPath = path.join(TARGET_BOOKS_DIR, bundledFilename);
        fs.copyFileSync(fullPath, targetPath);

        results.push({
          id,
          title,
          courseCode,
          category,
          relativePath: relPath,
          bundledFile: `books/${bundledFilename}`,
          size: stat.size,
          sizeFormatted: formatBytes(stat.size),
          lastModified: stat.mtime,
        });
      }
    }
  } catch (err) {
    console.error('Bundle error:', err);
  }
  return results;
}

console.log('📦 Bundling all local study materials into app assets...');
const materials = scanAndBundlePdfs(WORKSPACE_ROOT);
materials.sort((a, b) => {
  if (a.courseCode !== b.courseCode) return a.courseCode.localeCompare(b.courseCode);
  return a.title.localeCompare(b.title);
});

fs.writeFileSync(MANIFEST_PATH, JSON.stringify({ total: materials.length, materials }, null, 2));
console.log(`✅ Successfully bundled ${materials.length} books locally!`);
