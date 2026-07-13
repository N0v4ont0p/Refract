> Source: https://github.com/acmerobotics/ftc-dashboard/blob/master/README.md, https://acmerobotics.github.io/ftc-dashboard/gettingstarted.html, https://acmerobotics.github.io/ftc-dashboard/competition.html · Fetched: 2026-07-12

# FTC Dashboard

FTC Dashboard provides telemetry and monitoring tools for FTC robots during operation with the following features:

- Live telemetry with plots and field graphics
- Live configuration variables
- Camera streaming
- Limited op mode controls and gamepad support (note: gamepad support is volatile due to unstable browser APIs)
- Custom dashboard layouts
- Telemetry CSV export

## Installation

### Basic

1. Open `build.dependencies.gradle`.
2. In the `repositories` section, add:
   ```gradle
   maven { url = 'https://maven.brott.dev/' }
   ```
3. Add the dashboard implementation (see the [GitHub releases page](https://github.com/acmerobotics/ftc-dashboard/releases) for the latest version number):
   - If you're using a normal SDK setup, in the `dependencies` section, add:
     ```gradle
     implementation 'com.acmerobotics.dashboard:dashboard:0.6.0'
     ```
   - If you're using OpenRC or have non-standard SDK dependencies, in the `dependencies` section, add:
     ```gradle
     implementation('com.acmerobotics.dashboard:dashboard:0.6.0') {
       exclude group: 'org.firstinspires.ftc'
     }
     ```

### Advanced (building from source)

1. Clone the repo locally.
2. Append `-SNAPSHOT` to the end of `ext.dashboard_version` in `FtcDashboard/build.gradle`.
3. After making changes, publish them locally with `./gradlew publishToMavenLocal` (this has to be done on each computer).
4. Complete the basic instructions, adjusting the version and adding `mavenLocal()` to `repositories`.
5. Build and deploy like normal.

## Usage

1. Connect to the WiFi network broadcast by the RC (the passphrase is located in the `Program and Manage` menu).
2. Navigate to `192.168.49.1:8080/dash` with a phone RC or `192.168.43.1:8080/dash` with a Control Hub.

## Development

### Client setup

1. Install [Node.js](https://nodejs.org/en/download/) (Node.js 16+ is required for builds to work on M1 MacBooks; check [FtcDashboard/build.gradle](https://github.com/acmerobotics/ftc-dashboard/blob/master/FtcDashboard/build.gradle#L33) for the exact version used in gradle builds — `18.12.1` as of time of writing).
2. Install [Yarn](https://yarnpkg.com/en/docs/install) (not explicitly required, provides little advantage over modern `npm`, but instructions reference it for historical reasons).
3. The browser FTC Dashboard client is located in `client`.
4. Run `yarn` (or `npm install`) to install dependencies — only needs to be done once.
5. Optionally specify the server IP address through the environment variable `VITE_REACT_APP_HOST` (see [Vite's environment variable docs](https://vitejs.dev/guide/env-and-mode.html)). Default IPs:
   - Android Phone: `192.168.49.1`
   - Control Hub: `192.168.43.1`
6. Run `yarn dev` (or `npm run dev`) to start the development server on `http://localhost:3000` by default. It automatically reloads when source changes.

### Mock server

To test without an FTC app, run the mock server located at `DashboardCore/src/test/java/com/acmerobotics/dashboard/TestServer.java`.

- The mock server is a simple Java server hosting mock FTC op modes.
- A test sample op mode can be found at [`TestSineWaveOpMode.java`](https://github.com/acmerobotics/ftc-dashboard/blob/master/DashboardCore/src/test/java/com/acmerobotics/dashboard/TestSineWaveOpMode.java).
- Test op modes are registered in `TestOpModeManager.java`.

## Basic Architecture

### Java Server

Dashboard's server is split into two packages, `DashboardCore` and `FtcDashboard`:

- [Dashboard Core](https://github.com/acmerobotics/ftc-dashboard/tree/master/DashboardCore/src/main/java/com/acmerobotics/dashboard) — a standalone library that can be used to create a dashboard server for any Java application.
- [FtcDashboard](https://github.com/acmerobotics/ftc-dashboard/tree/master/FtcDashboard/src/main/java/com/acmerobotics/dashboard) — a wrapper around `DashboardCore` that provides relevant tooling and hooks for FTC teams. Contains the API FTC teams access and manipulate through their own code. Also contains the browser client source.

### Browser Client

The primary interface is a web client accessible to the end user through a web browser.

- Located in [`client`](https://github.com/acmerobotics/ftc-dashboard/tree/master/client).
- TypeScript + React application, built with Vite.
- Connects to the dashboard server via WebSocket.

Relevant files:

- [Dashboard.tsx](https://github.com/acmerobotics/ftc-dashboard/blob/master/client/src/components/Dashboard/Dashboard.tsx) — primary functional entrypoint.
- [LayoutPreset.tsx](https://github.com/acmerobotics/ftc-dashboard/blob/master/client/src/enums/LayoutPreset.tsx) — contains preset layouts.
- [`views/`](https://github.com/acmerobotics/ftc-dashboard/tree/master/client/src/components/views) — contains the various views displayed on the dashboard (graphs, telemetry, gamepad, etc).
- [`store/`](https://github.com/acmerobotics/ftc-dashboard/tree/master/client/src/store) — contains shared state management logic (WebSocket connection, gamepad state management, storage middleware, etc). Views subscribe to WebSocket updates via the Redux store.

## Competition Use

The **dashboard cannot be used during matches** pursuant to RS09 (2021-2022 Game Manual Part 1). To prevent accidental connections, use the "Disable Dashboard" menu item or the provided op mode during gameplay.

Dashboard use may be permitted in the pits. Keep other teams in mind and limit bandwidth usage, especially high-framerate camera streams.
