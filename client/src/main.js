import "dotenv/config";
import { app, BrowserWindow } from "electron";
import path from "node:path";
import { spawn } from "node:child_process";
import fetch from "node-fetch";

let backendProcess;

// Detecta se estamos em dev
const devServerURL = process.env.VITE_DEV_SERVER_URL;
const isDev = !!devServerURL;

// Paths
const getBackendPath = () => {
  if (isDev) return path.join(__dirname, "../server/dist/server/server.exe");
  return path.join(process.resourcesPath, "server.exe");
};

const getIndexHtml = () => {
  if (isDev) return devServerURL;
  return path.join(process.resourcesPath, "renderer/index.html");
};

// Cria janela principal
const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js"),
    },
  });

  if (isDev) {
    mainWindow.loadURL(devServerURL);
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(getIndexHtml());
  }
};

// Inicia backend e captura logs
const startBackend = () => {
  if (isDev) {
    // Em dev, roda o Python direto
    const backendPath = path.join(__dirname, "../server/server.py");
    console.log(`Starting backend in dev mode: ${backendPath}`);

    backendProcess = spawn("python", [backendPath], {
      cwd: path.dirname(backendPath),
      shell: true,
      stdio: "pipe",
    });
  } else {
    // Em produção, roda o exe
    const backendPath = path.join(process.resourcesPath, "server.exe");
    console.log(`Starting backend from exe: ${backendPath}`);

    backendProcess = spawn(backendPath, {
      cwd: path.dirname(backendPath),
      shell: true,
      stdio: "pipe",
    });
  }

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

// Espera o backend responder
const waitForBackend = async (url, retries = 20, delay = 500) => {
  for (let i = 0; i < retries; i++) {
    try {
      await fetch(url);
      console.log("Backend is ready");
      return true;
    } catch (e) {
      await new Promise((r) => setTimeout(r, delay));
    }
  }
  console.error("Backend never responded");
  return false;
};

app.whenReady().then(async () => {
  if (!isDev) startBackend();

  // Espera o backend antes de abrir a janela
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

// Captura erros globais
process.on("uncaughtException", console.error);
process.on("unhandledRejection", console.error);
