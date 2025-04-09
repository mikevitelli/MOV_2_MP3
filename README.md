## 🧪 INSTALL

### 🔧 System Requirements:

- macOS 11.0 or higher
- Intel or Apple Silicon (M1/M2/M3) compatible

### 📥 Download:

1. Head to the [Releases](https://github.com/yourusername/MOV_2_MP3/releases)
2. Download `MOV_2_MP3_macOS.zip`
3. Unzip the file
4. Move `MOV_2_MP3.app` to your Applications folder (optional)

### 🛡 First Time Running?

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

```bash
cd dist
zip -r MOV_2_MP3_macOS.zip MOV_2_MP3.app
```

You can now upload `MOV_2_MP3_macOS.zip` to GitHub Releases, Dropbox, etc.
