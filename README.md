# Py-Day98: Desktop File Organizer
Custom Automation - Automatically organize your messy folders!

## What It Does

This Python automation tool keeps your folders organized by automatically sorting files into categorized subfolders based on their type:

- **Images**: jpg, png, gif, svg, etc.
- **Documents**: pdf, docx, xlsx, txt, etc.
- **Videos**: mp4, avi, mkv, mov, etc.
- **Audio**: mp3, wav, flac, etc.
- **Archives**: zip, rar, 7z, etc.
- **Code**: py, js, html, css, etc.
- **Executables**: exe, msi, dmg, etc.
- **Others**: everything else

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### One-Time Organization

Run the organizer manually:

```bash
python file_organizer.py
```

The script will:
1. Ask for the folder path (defaults to Downloads)
2. Offer a dry run to preview changes
3. Organize files into categorized subfolders
4. Log all actions to `file_organizer.log`

### Scheduled Organization

Run the organizer automatically at set intervals:

```bash
python scheduler.py
```

Options:
- Every hour
- Daily at a specific time
- Weekly on a specific day

## Features

- **Safe**: Dry run mode to preview changes before moving files
- **Smart**: Handles duplicate filenames by adding timestamps
- **Logged**: All actions are logged for tracking
- **Flexible**: Works with any folder, not just Downloads
- **Customizable**: Easy to add new file categories

## Example

Before:
```
Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
├── video.mp4
└── script.py
```

After:
```
Downloads/
├── Images/
│   └── photo.jpg
├── Documents/
│   └── report.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── video.mp4
└── Code/
    └── script.py
```

## Customization

Edit `FILE_CATEGORIES` in `file_organizer.py` to add or modify file categories and extensions.
