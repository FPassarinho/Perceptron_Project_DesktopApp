const path = require("path");
const { FusesPlugin } = require("@electron-forge/plugin-fuses");
const { FuseV1Options, FuseVersion } = require("@electron/fuses");

module.exports = {
  packagerConfig: {
    icon: "./src/icons/icon",
    asar: true,
    extraResource: [
      path.resolve(__dirname, "../LICENSE"),
      path.resolve(__dirname, "resources/renderer"),
      path.resolve(__dirname, "../server/dist/server.exe"),
    ],
  },

  rebuildConfig: {},

  makers: [
    {
      name: "@electron-forge/maker-squirrel",
      config: {},
    },
    {
      name: "@electron-forge/maker-zip",
      platforms: ["win32", "darwin"], // ← adiciona win32
    },
    {
      name: "@electron-forge/maker-deb",
      config: {},
    },
    {
      name: "@electron-forge/maker-rpm",
      config: {},
    },
  ],

  plugins: [
    {
      name: "@electron-forge/plugin-vite",
      config: {
        build: [
          {
            entry: "src/main.js",
            config: "vite.main.config.mjs",
            target: "main",
          },
          {
            entry: "src/preload.js",
            config: "vite.preload.config.mjs",
            target: "preload",
          },
        ],
        renderer: [
          {
            name: "main_window",
            config: "vite.renderer.config.mjs",
          },
        ],
      },
    },

    new FusesPlugin({
      version: FuseVersion.V1,
      [FuseV1Options.RunAsNode]: false,
      [FuseV1Options.EnableCookieEncryption]: true,
      [FuseV1Options.EnableNodeOptionsEnvironmentVariable]: false,
      [FuseV1Options.EnableNodeCliInspectArguments]: false,
      [FuseV1Options.EnableEmbeddedAsarIntegrityValidation]: true,
      [FuseV1Options.OnlyLoadAppFromAsar]: true,
    }),
  ],
};
