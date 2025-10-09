import "dotenv/config"; // carrega .env
import { app, BrowserWindow } from "electron";
import path from "node:path";
import { spawn } from "node:child_process";

let backendProcess;

// Se a variável existir, estamos em dev
const devServerURL = process.env.VITE_DEV_SERVER_URL;

const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
    },
  });

  if (devServerURL) {
    mainWindow.loadURL(devServerURL);
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(path.join(__dirname, "../renderer/index.html"));
  }
};

// Inicia backend só se não estivermos em dev
const startBackend = () => {
  const backendPath = path.join(__dirname, "../server/dist/server.exe");
  console.log(`Starting backend from: ${backendPath}`);

  backendProcess = spawn(backendPath, [], { stdio: "inherit" });

  backendProcess.on("exit", (code) => {
    console.log(`Backend exited with code ${code}`);
  });

  backendProcess.on("error", (err) => {
    console.error("Failed to start backend:", err);
  });
};

app.whenReady().then(() => {
  if (!devServerURL) startBackend();
  createWindow();
});

app.on("window-all-closed", () => {
  if (backendProcess) backendProcess.kill();
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
});
