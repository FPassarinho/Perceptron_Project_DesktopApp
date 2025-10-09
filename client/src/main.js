import "dotenv/config";
import { app, BrowserWindow } from "electron";
import path from "node:path";
import { spawn } from "node:child_process";

let backendProcess;

// Se a variável existir, estamos em dev
const devServerURL = process.env.VITE_DEV_SERVER_URL;
const isDev = !!devServerURL;

// Função para pegar o caminho correto do backend
const getBackendPath = () => {
  if (isDev) {
    return path.join(__dirname, "../server/dist/server/server.exe");
  }
  // Em produção, está dentro de resources do pacote
  return path.join(process.resourcesPath, "server.exe");
};

// Função para pegar o caminho correto do index.html
const getIndexHtml = () => {
  if (isDev) {
    return devServerURL;
  }
  // Em produção, build do Vite está copiado para resources/renderer
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

// Inicia backend
const startBackend = () => {
  const backendPath = getBackendPath();
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
  if (!isDev) startBackend();
  createWindow();
});

app.on("window-all-closed", () => {
  if (backendProcess) backendProcess.kill();
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (BrowserWindow.getAllWindows().length === 0) createWindow();
});
