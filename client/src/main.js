import "dotenv/config";
import { app, BrowserWindow } from "electron";
import path from "node:path";
import { spawn } from "node:child_process";
import fetch from "node-fetch";

let backendProcess;
const devServerURL = process.env.VITE_DEV_SERVER_URL;
const isDev = !!devServerURL;

// Paths
const getBackendPath = () =>
  isDev
    ? path.join(__dirname, "../server/dist/server/server.exe")
    : path.join(process.resourcesPath, "server.exe");

const getIndexHtml = () =>
  isDev
    ? devServerURL
    : path.join(process.resourcesPath, "renderer/index.html");

// Cria janela com loading
const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: { preload: path.join(__dirname, "preload.js") },
  });

  if (isDev) {
    mainWindow.loadURL(devServerURL);
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(getIndexHtml());
  }

  return mainWindow;
};

// Start backend e captura logs
const startBackend = () => {
  const backendPath = getBackendPath();
  console.log(`Starting backend from: ${backendPath}`);

  backendProcess = spawn(backendPath, {
    cwd: path.dirname(backendPath),
    shell: true,
    stdio: "pipe",
  });

  backendProcess.stdout.on("data", (data) =>
    console.log(`Backend: ${data.toString()}`)
  );
  backendProcess.stderr.on("data", (data) =>
    console.error(`Backend ERROR: ${data.toString()}`)
  );

  backendProcess.on("exit", (code) =>
    console.log(`Backend exited with code ${code}`)
  );
  backendProcess.on("error", (err) =>
    console.error("Failed to start backend:", err)
  );
};

// Espera backend
const waitForBackend = async (url, retries = 40, delay = 500) => {
  for (let i = 0; i < retries; i++) {
    try {
      const res = await fetch(url);
      if (res.ok) {
        console.log("Backend is ready");
        return true;
      }
    } catch {}
    await new Promise((r) => setTimeout(r, delay));
  }
  console.error("Backend never responded");
  return false;
};

app.whenReady().then(async () => {
  if (!isDev) startBackend();

  // Aguarda backend antes de abrir a janela
  if (!isDev) await waitForBackend("http://127.0.0.1:5000/datasets");

  createWindow();
});

app.on("window-all-closed", () => {
  if (backendProcess) backendProcess.kill();
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
});

process.on("uncaughtException", console.error);
process.on("unhandledRejection", console.error);
