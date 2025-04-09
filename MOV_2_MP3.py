import os
import sys
import subprocess
from tkinter import Tk, filedialog, messagebox

def get_ffmpeg_path():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
        return os.path.join(base_path, "ffmpeg")
    else:
        return os.path.abspath("ffmpeg")

def extract_audio(input_file, output_file):
    command = [
        get_ffmpeg_path(),
        '-i', input_file,
        '-q:a', '0',
        '-map', 'a',
        output_file
    ]
    try:
        subprocess.run(command, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error processing {input_file}: {e}")
        return False

def main():
    Tk().withdraw()
    messagebox.showinfo("MOV 2 MP3", "Select the folder containing .MOV files.")
    input_folder = filedialog.askdirectory(title="Select Folder with .MOV Files")

    if not input_folder:
        messagebox.showwarning("No Folder Selected", "Operation canceled.")
        return

    output_folder = os.path.join(input_folder, "mp3_output")
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".mov"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")
            if extract_audio(input_path, output_path):
                print(f"Converted: {filename} -> {output_path}")

    messagebox.showinfo("Conversion Complete", f"MP3 files saved in: {output_folder}")

if __name__ == "__main__":
    main()
