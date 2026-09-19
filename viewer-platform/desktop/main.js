const { app, BrowserWindow, shell } = require('electron');
const path = require('path');
const http = require('http');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1280,
    height: 850,
    minWidth: 900,
    minHeight: 600,
    title: 'Secure Study Material Hub',
    backgroundColor: '#0f172a',
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true,
      sandbox: true,
      devTools: process.env.NODE_ENV === 'development',
    },
    autoHideMenuBar: true,
  });

  // 🛡️ NATIVE OS SCREEN-CAPTURE BLOCKING:
  // On Windows: calls SetWindowDisplayAffinity(WDA_MONITOR) -> Snipping Tool/OBS record black rectangle
  // On macOS: calls NSWindowSharingNone -> Screen captures record empty black space
  mainWindow.setContentProtection(true);

  const startUrl = process.env.ELECTRON_START_URL || `http://localhost:5001`;

  // Start internal server if running standalone
  try {
    require('../server/index.js');
  } catch (e) {
    console.log('Server already running or external.');
  }

  // Load backend/frontend
  setTimeout(() => {
    mainWindow.loadURL(startUrl).catch(() => {
      // Retry if server takes a moment to boot
      setTimeout(() => mainWindow.loadURL(startUrl), 1500);
    });
  }, 1000);

  // Prevent external navigation
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    if (url.startsWith('https:')) {
      shell.openExternal(url);
    }
    return { action: 'deny' };
  });

  // Block DevTools shortcuts
  mainWindow.webContents.on('before-input-event', (event, input) => {
    if (
      (input.control || input.meta) &&
      (input.key.toLowerCase() === 'i' ||
        input.key.toLowerCase() === 'r' ||
        input.key.toLowerCase() === 's' ||
        input.key.toLowerCase() === 'p')
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
