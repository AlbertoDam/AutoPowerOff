# AutoPowerOff ![AutoPowerOff Logo](assets/icon.ico)

[![License: Source-available (Commercial requires paid license)](https://img.shields.io/badge/license-Source--available-orange.svg)]

Desktop application for Windows that allows you to schedule automatic shutdown with a cancelable countdown and interactive configuration. It features a modern interface, real-time validation, configurable limits, and a workflow designed to become an `.exe` that users can download directly after merging into `main`.

## Main Features

- ⏱️ **Cancelable shutdown timer** with real-time countdown.
- ⚠️ **User-friendly input validation:** does not allow 0, negative, or out-of-range values and provides immediate feedback.
- ⚙️ **Settings panel** with visual language selector and control to adjust the maximum minutes (currently visual only).
- 🎨 **Light/dark mode detection** and centralized color scheme.
- 🧩 **Modularized UI** for easy maintenance and extensions.
- 🖥️ **Executable `.exe` generation** for distribution without requiring Python installed on the target machine.
- 🇪🇸 / 🇬🇧 **Visual language menu** (currently visual only).

## Technology

The project is built with the following main technologies:

- **Python** – Logic, timer, and general orchestration.
- **CustomTkinter** – Modern, adaptable GUI on top of Tkinter.
- **Pillow** – Image loading and manipulation (flags, logo, icons).
- **darkdetect** – OS light/dark mode detection.
- **PyInstaller** – Packaging the project as a standalone `.exe` for Windows.
- **Packaging / pip** – Dependency and environment management.

## Requirements and Setup

1. Clone the repository and navigate to the project root.
2. Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:

```sh
pip install -r requirements.txt
```

> `requirements.txt` should include at least:
> `customtkinter`, `pillow`, `darkdetect`

## Running in Development

```sh
.\venv\Scripts\Activate.ps1
python src/main.py
```

- Enter a valid value in minutes.
- The **Start** button is enabled only if the input passes validation.
- You can cancel at any time.
- When it reaches zero, Windows shutdown is triggered (`shutdown /s /t 0`) — for testing, comment out that line in the code.

## Configuration

- **Maximum minutes:** adjustable from the settings panel (currently visual only) (`min_minutes` / `max_minutes` parameters in `TimeInput`).
- **Live validation:** the time field is automatically validated and controls the start button state.
- **Theme:** colors are managed from `src/utils/theme_config.py` and adapt to system mode.
- **Settings icons:** loaded as `PhotoImage` and retained so they don't disappear in the native menu.

## CI/CD and Automatic Deployment (future)

A CI/CD pipeline with **GitHub Actions** will be integrated later to automate build and deployment:

- On merge to `main`, `.exe` build with PyInstaller will be triggered.
- Code will be validated and tested, the artifact will be generated automatically and published (as a GitHub release).
- Users will be able to download the generated `.exe` directly from the releases interface or a distribution site without needing to compile anything locally.

## How to Contribute

1. Create a branch from `develop`:

```sh
git checkout develop
git checkout -b feature/your-improvement
```

2. Make commits using Conventional Commits.
3. Open a pull request to `develop`.

## License

This project is **source-available**: you can view, clone, fork, modify, and contribute freely. **Non-commercial** use is allowed at no cost. For any **commercial** use (including distributing the `.exe` as part of a paid product, integrating it into commercial offerings, reselling, or providing as a service) **a paid commercial license is required**.

Contact to negotiate a commercial license or clarify usage:
**Alberto Pérez Pérez** · [aperper.4@gmail.com](mailto:aperper.4@gmail.com)

## Contact

AlbertoDam · [aperper.4@gmail.com](mailto:aperper.4@gmail.com)
Repository: AutoPowerOff
