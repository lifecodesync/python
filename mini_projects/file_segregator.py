# File Segregator: give a folder path, it sorts files into sub-folders
# by type (PDF, PPT, TXT, Images, ...) and prints a summary.
# Uses only built-in modules (os, shutil).

import os
import shutil

CATEGORIES = {
    "PDF": [".pdf"],
    "PPT": [".ppt", ".pptx"],
    "TXT": [".txt"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"],
    "Word": [".doc", ".docx"],
    "Excel": [".xls", ".xlsx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Code": [".py", ".java", ".c", ".cpp", ".js", ".html", ".css"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def unique_path(folder, filename):
    """Avoid overwriting: file.txt -> file (1).txt if it already exists."""
    base, ext = os.path.splitext(filename)
    path = os.path.join(folder, filename)
    n = 1
    while os.path.exists(path):
        path = os.path.join(folder, f"{base} ({n}){ext}")
        n += 1
    return path


def segregate(folder):
    summary = {}
    for name in os.listdir(folder):
        src = os.path.join(folder, name)
        if not os.path.isfile(src):
            continue  # skip sub-folders
        category = get_category(name)
        dest_dir = os.path.join(folder, category)
        os.makedirs(dest_dir, exist_ok=True)
        shutil.move(src, unique_path(dest_dir, name))
        summary.setdefault(category, []).append(name)
    return summary


if __name__ == "__main__":
    folder = input("Enter folder path: ").strip().strip('"')
    if not os.path.isdir(folder):
        print("Folder not found:", folder)
    else:
        result = segregate(folder)
        if not result:
            print("No files to segregate.")
        else:
            print("\nSegregation complete:\n")
            total = 0
            for category, files in sorted(result.items()):
                print(f"{category} ({len(files)} files)")
                for f in files:
                    print("   -", f)
                total += len(files)
            print(f"\nTotal files moved: {total}")
