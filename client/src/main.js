// main.js
import { app, BrowserWindow } from "electron";
import path from "node:path";
import { exec } from "child_process";
import started from "electron-squirrel-startup";

// Quit if Electron Squirrel installer triggered
if (started) {
  app.quit();
}

let backendProcess;

const iconPath = path.resolve(process.cwd(), "src", "icons", "icon.png");

// Cria a janela principal
const createWindow = () => {
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    icon: iconPath,
    webPreferences: {
      nodeIntegration: true, // permite require dentro do renderer
      contextIsolation: false,
    },
  });

  // Carrega o frontend
  const devURL = process.env.MAIN_WINDOW_VITE_DEV_SERVER_URL;
  const prodPath = path.join(__dirname, "../renderer/index.html"); // ajustar se build estiver em outra pasta

  if (devURL) {
    mainWindow.loadURL(devURL);
    mainWindow.webContents.openDevTools();
  } else {
    mainWindow.loadFile(prodPath);
  }
};

// Inicializa o app
app.whenReady().then(() => {
  const backendPath = path.join(__dirname, "../server/dist/perceptron.exe"); 
  backendProcess = exec(`"${backendPath}"`, (err, stdout, stderr) => {
    if (err) console.error("Backend error:", err);
    if (stderr) console.error("Backend stderr:", stderr);
    console.log(stdout);
  });

  createWindow();

  // Para macOS
  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) createWindow();
  });
});

// Fecha app e backend
app.on("window-all-closed", () => {
  if (backendProcess) backendProcess.kill();
  if (process.platform !== "darwin") app.quit();
});

console.log("Icon path:", iconPath);
