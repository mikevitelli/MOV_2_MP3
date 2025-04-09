## 🎧 MOV_2_MP3 – Lightweight Audio Extractor

**MOV_2_MP3** is a simple, fast, and offline desktop application that converts `.MOV` video files into `.MP3` audio files with one click.

~98% reduction in file size when converting .mov → .mp3 🎯

It’s designed for:

- **Transcription workflows**
- **Audio extraction for editing or reference**
- **Podcast prep**
- **Note-taking from interviews or video calls**

Whether you're a journalist, editor, student, or content creator, MOV_2_MP3 helps you quickly isolate audio from video files — no need for complex software or internet access.

---

### ✅ Features

- Batch convert entire folders of `.mov` files
- Output high-quality `.mp3` files
- ffmpeg bundled — **no setup required**
- Works 100% offline
- Minimal interface, built for non-technical users

---

### 💻 Platform Support

- macOS (see install directions below)
- Windows version coming soon

## 🧪 INSTALL

### 🔧 System Requirements:

- macOS 11.0 or higher
- Intel or Apple Silicon (M1/M2/M3) compatible

### 📥 Download:

1. Head to the [Releases](https://github.com/mikevitelli/MOV_2_MP3/releases)
2. Download `MOV_2_MP3.zip`
3. Unzip the file
4. Move `MOV_2_MP3.app` to your Applications folder (optional)

### 🛡 First Time Running?

## IMPORTANT!!

macOS will block the app by default since it’s unsigned:

1. **Right-click** (or Control-click) on `MOV_2_MP3.app`
2. Select **“Open”**
3. Click **“Open”** again in the popup
4. You’re in! 🎉

---

## 🛠 BUILD (for Developers)

### 🔧 Prerequisites:

- macOS
- Python 3.10 or 3.11
- [PyInstaller](https://pyinstaller.org) installed:

  ```bash
  pip install pyinstaller
  ```

- [FFmpeg](https://ffmpeg.org/) (macOS binary placed next to the script):
  ```bash
  brew install ffmpeg
  ```

Or manually download a static macOS binary and place it as `ffmpeg` (not `.exe`).

---

### 📁 Project Folder Structure:

```
MOV_2_MP3/
├── MOV_2_MP3.py
├── ffmpeg                 # macOS binary, not .exe
├── icon.icns              # Optional app icon
├── README.md
├── .gitignore
```

---

### 🧱 Build the App:

```bash
pyinstaller --onefile --windowed --icon=icon.icns --add-binary=ffmpeg:. MOV_2_MP3.py
```

This will generate:

```
dist/
└── MOV_2_MP3.app
```

---

### 📦 Create a Shareable Zip:

Best to compress through finder vs. bash or shell command.

```bash
cd dist
zip -r MOV_2_MP3_macOS.zip MOV_2_MP3
```

You can now upload `MOV_2_MP3_macOS.zip` to GitHub Releases, Dropbox, etc.

---

MIT License

Copyright (c) 2024 Mike Vitelli

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:
...
