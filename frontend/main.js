const { spawn } = require('child_process');
let pythonProcess = null;

// frontend/main.js
const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 1000,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    backgroundColor: '#0f0f1a',
    title: 'Nexus',
    icon: path.join(__dirname, 'icon.png'), // optional: add an icon later
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,       // security: disabled
      contextIsolation: true,       // security: enabled
      enableRemoteModule: false     // extra security
    }
  });

  // Load the UI
  win.loadFile(path.join(__dirname, 'index.html'));

  // Open DevTools automatically during development (comment out when done)
  win.webContents.openDevTools();

  // Optional: Prevent garbage collection issues on macOS
  win.on('closed', () => {
    win = null;
  });
}

// When Electron is ready to launch
app.whenReady().then(() => {

  // Start Python backend
  pythonProcess = spawn('python', ['backend/app.py'], {
    cwd: path.join(__dirname, '..'),
    shell: true
  });

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python Error: ${data}`);
  });

  createWindow();
});

// Quit when all windows are closed (except on macOS)
app.on('window-all-closed', () => {
  if (pythonProcess) {
    pythonProcess.kill();
  }

  if (process.platform !== 'darwin') {
    app.quit();
  }
});