import { app, BrowserWindow } from "electron";
import path from "node:path";
import { spawn } from "node:child_process";
import started from "electron-squirrel-startup";

if (started) app.quit();

const iconPath = path.resolve(process.cwd(), "src", "icons", "icon.png");
let pyProc = null;

const startPythonServer = () => {
  const isDev = process.env.NODE_ENV === "development";
  if (isDev) return; 

  const pythonPath = path.join(
    process.resourcesPath,
    "server",
    "venv",
    "Scripts",
    "python.exe"
  );
  const scriptPath = path.join(process.resourcesPath, "server", "app.py");

  pyProc = spawn(pythonPath, [scriptPath]);
  pyProc.stdout.on("data", (data) => console.log(`Flask: ${data}`));
  pyProc.stderr.on("data", (data) => console.error(`Flask error: ${data}`));

  console.log("Flask server initiated.");
};

const stopPythonServer = () => {
  if (pyProc) pyProc.kill();
  pyProc = null;
};

const createWindow = () => {
  const mainWindow = new BrowserWindow({
    icon: iconPath,
    width: 800,
    height: 600,
    webPreferences: { preload: path.join(__dirname, "preload.js") },
  });

  if (MAIN_WINDOW_VITE_DEV_SERVER_URL) {
    mainWindow.loadURL(MAIN_WINDOW_VITE_DEV_SERVER_URL);
  } else {
    mainWindow.loadFile(
      path.join(__dirname, `../renderer/${MAIN_WINDOW_VITE_NAME}/index.html`)
    );
  }

  mainWindow.webContents.openDevTools();
};

app.whenReady().then(() => {
  startPythonServer();
  createWindow();

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

app.on("window-all-closed", () => {
  stopPythonServer();
  if (process.platform !== "darwin") app.quit();
});
