import { execSync } from 'child_process';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

console.log('⚡ Running modern Vite build with Cabinet Grotesk + Satoshi Swiss typography...');
execSync('npx vite build', { cwd: __dirname, stdio: 'inherit' });
console.log('🎉 Production build complete in dist/!');
