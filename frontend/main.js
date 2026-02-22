// main.js
const { spawn } = require('child_process');
const { app, BrowserWindow } = require('electron');
const path = require('path');

let pythonProcess = null;

function createWindow() {
  const win = new BrowserWindow({
    width: 1000,
    height: 800,
    minWidth: 800,
    minHeight: 600,
    backgroundColor: '#0f0f1a',
    title: 'Nexus',
    icon: path.join(__dirname, 'icon.png'),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      nodeIntegration: false,
      contextIsolation: true,
      enableRemoteModule: false
    }
  });

  win.loadFile(path.join(__dirname, 'index.html'));
}

app.whenReady().then(() => {

  // Start Python backend silently
  pythonProcess = spawn('python', ['backend/app.py'], {
    cwd: path.join(__dirname, '..'),
    shell: true,
    windowsHide: true   // <-- Hides the Python console
  });

  pythonProcess.stdout.on('data', (data) => {
    console.log(`Python: ${data}`);
  });

  pythonProcess.stderr.on('data', (data) => {
    console.error(`Python Error: ${data}`);
  });

  createWindow();
});

app.on('window-all-closed', () => {
  if (pythonProcess) pythonProcess.kill();
  if (process.platform !== 'darwin') app.quit();
});