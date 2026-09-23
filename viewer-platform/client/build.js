import esbuild from 'esbuild';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const clientDir = __dirname;
const distDir = path.join(clientDir, 'dist');
const assetsDir = path.join(distDir, 'assets');
const publicDir = path.join(clientDir, 'public');

console.log('⚡ Building Edu network client bundle...');

// 1. Ensure output directories exist
fs.mkdirSync(assetsDir, { recursive: true });

// 2. Bundle React app with esbuild
const jsOutfile = path.join(assetsDir, 'app.js');
const cssOutfile = path.join(assetsDir, 'app.css');

await esbuild.build({
  entryPoints: [path.join(clientDir, 'src/main.jsx')],
  bundle: true,
  minify: true,
  sourcemap: false,
  outfile: jsOutfile,
  loader: {
    '.png': 'file',
    '.jpg': 'file',
    '.svg': 'file',
    '.woff': 'file',
    '.woff2': 'file',
  },
  define: {
    'process.env.NODE_ENV': '"production"',
  },
});

console.log('✅ JavaScript bundle built successfully!');

// 3. Build CSS with Tailwind styles and custom styles
let baseCss = '';
const cssFiles = fs.readdirSync(assetsDir).filter(f => f.startsWith('index-') && f.endsWith('.css'));
if (cssFiles.length > 0) {
  cssFiles.sort((a, b) => fs.statSync(path.join(assetsDir, b)).mtimeMs - fs.statSync(path.join(assetsDir, a)).mtimeMs);
  baseCss = fs.readFileSync(path.join(assetsDir, cssFiles[0]), 'utf8');
  console.log(`✅ Using latest compiled Tailwind CSS: ${cssFiles[0]} (${(baseCss.length / 1024).toFixed(1)} KB)`);
} else {
  const anyCss = fs.readdirSync(assetsDir).filter(f => f.endsWith('.css') && f !== 'app.css');
  if (anyCss.length > 0) {
    baseCss = fs.readFileSync(path.join(assetsDir, anyCss[0]), 'utf8');
  }
}

// Ensure correct texture image paths in CSS
baseCss = baseCss.replace(/url\(\/textures\/light-grain\.png\)/g, "url('./light-grain.png')");
baseCss = baseCss.replace(/url\(\/textures\/dark-grain\.png\)/g, "url('./dark-grain.png')");

fs.writeFileSync(cssOutfile, baseCss, 'utf8');
console.log('✅ CSS bundle built successfully!');

// 4. Copy public directory assets recursively (textures, logo, manifest, books)
function copyRecursiveSync(src, dest) {
  const exists = fs.existsSync(src);
  const stats = exists && fs.statSync(src);
  const isDirectory = exists && stats.isDirectory();
  if (isDirectory) {
    if (!fs.existsSync(dest)) fs.mkdirSync(dest, { recursive: true });
    fs.readdirSync(src).forEach((childItemName) => {
      copyRecursiveSync(path.join(src, childItemName), path.join(dest, childItemName));
    });
  } else if (exists) {
    fs.copyFileSync(src, dest);
  }
}

console.log('📂 Copying public static assets...');
copyRecursiveSync(publicDir, distDir);

// Also ensure textures are present directly in assets for relative CSS resolution
if (fs.existsSync(path.join(publicDir, 'textures'))) {
  copyRecursiveSync(path.join(publicDir, 'textures'), assetsDir);
}

// 5. Generate dist/index.html
const indexHtmlContent = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/png" href="./logo.png" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Edu network • Academic Material & Book Archives</title>
    <!-- Google Fonts: Editorial Serif + Modern Swiss Sans + Monospace -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800;900&family=Instrument+Serif:ital@0;1&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    <!-- Google Identity Services -->
    <script src="https://accounts.google.com/gsi/client" async defer></script>
    <script type="module" src="./assets/app.js"></script>
    <link rel="stylesheet" href="./assets/app.css">
  </head>
  <body class="bg-[#F5F2EB] text-[#18181B] min-h-screen antialiased selection:bg-[#18181B] selection:text-[#F5F2EB]">
    <div id="root"></div>
  </body>
</html>
`;

fs.writeFileSync(path.join(distDir, 'index.html'), indexHtmlContent, 'utf8');

console.log('🎉 Production build complete in dist/!');
