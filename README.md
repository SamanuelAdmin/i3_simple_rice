
# i3 Simple Rice

A lightweight, minimalistic i3 window manager setup for a clean and efficient workspace.

<img width="1919" height="1079" alt="ksnip_222" src="https://github.com/user-attachments/assets/7bde0db2-04dc-496e-bd1b-00d11cd3d69f" />

<img width="1919" height="1079" alt="ksnip_20250711-170406" src="https://github.com/user-attachments/assets/9291bc84-b762-4989-92d8-2d5ab793d53a" />

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Dependencies](#dependencies)  
- [Installation](#installation)  
- [Directory Structure](#directory-structure)  
- [Usage](#usage)  
- [Customization](#customization)  
- [Troubleshooting](#troubleshooting)  

---

## Overview

This is a simple, clean i3 window manager rice designed for fast and distraction-free workflow. It uses a minimal setup with a few lightweight tools to enhance usability and visual appearance, while staying fast and resource-efficient.

---

## Features

- Tiling window manager with customized keybindings  
- Status bar configuration using i3blocks  
- Transparent effects with picom  
- Rofi application launcher  
- Media and brightness control with keyboard shortcuts  
- Minimal but functional design

---

## Dependencies

Make sure the following software is installed:

- `i3` or `i3-gaps`  
- `picom` – compositor for transparency/shadows  
- `i3blocks` – for custom status bar  
- `rofi` – application launcher  
- `pulsemixer` – audio control  
- `brightnessctl` – brightness control  
- `feh` – wallpaper setter (optional)  
- `xbacklight` or `light` – alternative brightness tools (optional)

You can install them on Debian/Ubuntu like this:

```bash
sudo apt update
sudo apt install i3 picom i3blocks rofi brightnessctl pulsemixer feh
```

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/SamanuelAdmin/i3_simple_rice.git ~/.config/i3_simple_rice
```

2. **Back up your existing i3 config:**

```bash
mv ~/.config/i3 ~/.config/i3.backup
```

3. **Link or copy the configs:**

```bash
ln -s ~/.config/i3_simple_rice/i3 ~/.config/i3
ln -s ~/.config/i3_simple_rice/picom ~/.config/picom
ln -s ~/.config/i3_simple_rice/i3blocks ~/.config/i3blocks
ln -s ~/.config/i3_simple_rice/rofi ~/.config/rofi
```

4. **Change "utils" path for your correct and check configs again:**
You can do it with vim, for ex.
```bash
vim ~/.config/i3/config
```

5. **Reload i3:**

Use `Mod+Shift+R` to reload the i3 config (Mod is usually the Super/Windows key).

---

## Directory Structure

```
i3_simple_rice/
├── i3/                # Main i3 configuration and keybindings
├── picom/             # Picom config for transparency and shadows
├── i3blocks/          # Status bar configuration and scripts
├── rofi/              # Rofi theme and launcher config
├── wallpapers/        # Background images
└── README.md          # This file
```

---

## Usage


This is a quick guide to the essential hotkeys used in the i3_simple_rice setup.

---

### 🔑 Basic Window Management

#### Open, Focus, Close Windows
- **Mod + Enter** → Open terminal  
- **Mod + J / K / L / ;** → Move focus (left / down / up / right)  
- **Mod + Shift + Q** → Close focused window

#### Window Splitting
- **Mod + V** → Vertical split  
- **Mod + H** → Horizontal split  
- **Mod + S** → Stacked layout  
- **Mod + W** → Tabbed layout

#### Fullscreen and Floating
- **Mod + F** → Toggle fullscreen mode  
- **Mod + Shift + Space** → Toggle floating mode

---

### 🖥 Workspaces

- **Mod + [1–9]** → Switch to workspace N  
- **Mod + Shift + [1–9]** → Move window to workspace N

---

### 🔄 Reload / Exit

- **Mod + Shift + R** → Reload i3 configuration  
- **Mod + Shift + E** → Exit i3 session

---

### 🚀 Application Launching

- **Mod + D** → Launch Rofi (application launcher)

---

### 🔊 Media & Brightness (custom bindings)

- Use **media keys** or custom **Mod + Arrow keys** for:
  - Volume control (`pulsemixer`)
  - Brightness control (`brightnessctl`)

---

### 💡 Tips

- Start a terminal with `Mod + Enter`  
- Move around with `Mod + J/K/L/;`  
- Change window layout dynamically (`Mod + V`, `Mod + H`, etc.)  
- Use `Mod + D` to quickly launch any installed app  
- Restart config with `Mod + Shift + R` after changes  
- Use `Mod + Shift + E` to cleanly exit your session

---

## Customization

You can customize your environment easily:

- **Keybindings:** Edit `~/.config/i3/config`  
- **Bar scripts:** Modify or add scripts in `i3blocks`  
- **Compositor:** Tweak effects in `picom.conf`  
- **Launcher:** Adjust Rofi theme and appearance in `rofi/config`  
- **Wallpaper:** Replace or set your own in the `wallpapers/` folder

---

## Troubleshooting

- **No i3 loads:** Run `i3 -C` to check for config errors  
- **No transparency:** Start picom manually or check config path  
- **Status bar not showing:** Run `i3blocks` in terminal to test  
- **App launcher not responding:** Try `rofi -show drun` and check errors  
- **No wallpaper:** Ensure `feh` is installed and paths are correct

---


