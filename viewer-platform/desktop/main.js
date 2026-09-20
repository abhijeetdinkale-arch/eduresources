const { app, BrowserWindow, shell } = require('electron');
const path = require('path');

let mainWindow;

function createWindow() {
  const iconPath = path.join(__dirname, 'icon.png');

  mainWindow = new BrowserWindow({
    width: 1360,
    height: 900,
    minWidth: 960,
    minHeight: 650,
    title: 'Edu network • Academic Material & Book Archives',
    backgroundColor: '#F5F2EB',
    icon: iconPath,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      sandbox: true,
      devTools: process.env.NODE_ENV === 'development',
    },
    autoHideMenuBar: true,
    show: false,
  });

  if (process.platform === 'darwin' && app.dock) {
    try {
      app.dock.setIcon(iconPath);
    } catch (e) {}
  }

  // 🛡️ HARDWARE-LEVEL OS SCREEN-CAPTURE BLOCKING:
  // On Windows: calls SetWindowDisplayAffinity(WDA_MONITOR) -> Snipping Tool/OBS record black rectangle
  // On macOS: calls NSWindowSharingNone -> Screen captures & recording show empty black space
  mainWindow.setContentProtection(true);

  // Determine URL (Local internal server or online Vercel sync)
  const startUrl = process.env.ELECTRON_START_URL || `http://localhost:5001`;

  // Graceful show on ready
  mainWindow.once('ready-to-show', () => {
    mainWindow.show();
  });

  // Load URL with resilient retry
  const loadWithRetry = (url, retries = 5) => {
    mainWindow.loadURL(url).catch((err) => {
      if (retries > 0) {
        setTimeout(() => loadWithRetry(url, retries - 1), 1000);
      } else {
        // Fallback to cloud URL if local server port took too long
        mainWindow.loadURL('https://edu-network.vercel.app');
      }
    });
  };

  // Check if server is already running before spawning
  const http = require('http');
  const req = http.get('http://localhost:5001/api/health', (res) => {
    console.log('Connected to existing local server.');
    loadWithRetry(startUrl);
  });

  req.on('error', () => {
    try {
      require('../server/index.js');
    } catch (e) {
      console.log('Server init:', e.message);
    }
    setTimeout(() => loadWithRetry(startUrl), 800);
  });

  // Prevent external popup navigations
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    if (url.startsWith('https:') || url.startsWith('http:')) {
      shell.openExternal(url);
    }
    return { action: 'deny' };
  });

  // Block inspection shortcuts in production
  mainWindow.webContents.on('before-input-event', (event, input) => {
    if (
      (input.control || input.meta) &&
      (input.key.toLowerCase() === 'i' ||
        input.key.toLowerCase() === 'r' ||
        input.key.toLowerCase() === 's' ||
        input.key.toLowerCase() === 'p' ||
        input.key.toLowerCase() === 'u')
    ) {
      if (process.env.NODE_ENV !== 'development') {
        event.preventDefault();
      }
    }
  });

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (mainWindow === null) {
    createWindow();
  }
});
