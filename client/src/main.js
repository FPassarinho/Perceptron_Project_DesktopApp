import path from "node:path";
import { app, BrowserWindow } from "electron";
import { spawn } from "node:child_process";

let backendProcess;

const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
    },
  });

  if (process.env.VITE_DEV_SERVER_URL) {
    mainWindow.loadURL(process.env.VITE_DEV_SERVER_URL);
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(path.join(__dirname, "../renderer/index.html"));
  }
};

const isDev = !!process.env.VITE_DEV_SERVER_URL;

const startBackend = () => {
  const backendPath = isDev
    ? path.join(__dirname, "../server/dist/server.exe")
    : path.join(process.resourcesPath, "server.exe");

  console.log("Starting backend:", backendPath);

  backendProcess = spawn(backendPath, [], { stdio: "inherit" });

  backendProcess.on("exit", (code) => {
    console.log(`Backend exited with code ${code}`);
  });
};

app.whenReady().then(() => {
  if (!isDev) startBackend();
  createWindow();
});

app.on("window-all-closed", () => {
  if (backendProcess) backendProcess.kill();
  if (process.platform !== "darwin") app.quit();
});
