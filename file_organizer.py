"""
Desktop File Organizer
Automatically organizes files into categorized folders based on file extensions.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('file_organizer.log'),
        logging.StreamHandler()
    ]
)

# File categories and their extensions
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.ico', '.webp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.xls', '.ppt', '.pptx', '.odt', '.csv'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.rs'],
    'Executables': ['.exe', '.msi', '.dmg', '.pkg', '.deb', '.rpm'],
    'Others': []
}


class FileOrganizer:
    def __init__(self, source_folder):
        self.source_folder = Path(source_folder)
        if not self.source_folder.exists():
            raise ValueError(f"Source folder '{source_folder}' does not exist")
        
    def get_category(self, file_extension):
        """Determine the category of a file based on its extension."""
        file_extension = file_extension.lower()
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                return category
        return 'Others'
    
    def organize_files(self, dry_run=False):
        """
        Organize files in the source folder into categorized subfolders.
        
        Args:
            dry_run (bool): If True, only show what would be done without moving files
        """
        files_moved = 0
        files_skipped = 0
        
        logging.info(f"Starting file organization in: {self.source_folder}")
        logging.info(f"Dry run mode: {dry_run}")
        
        # Get all files in the source folder (not subdirectories)
        files = [f for f in self.source_folder.iterdir() if f.is_file()]
        
        if not files:
            logging.info("No files to organize")
            return
        
        for file_path in files:
            try:
                # Skip log files
                if file_path.name == 'file_organizer.log':
                    continue
                
                # Get file extension and category
                file_extension = file_path.suffix
                category = self.get_category(file_extension)
                
                # Create category folder if it doesn't exist
                category_folder = self.source_folder / category
                
                if not dry_run and not category_folder.exists():
                    category_folder.mkdir(parents=True)
                    logging.info(f"Created folder: {category}")
                
                # Destination path
                destination = category_folder / file_path.name
                
                # Handle duplicate filenames
                if destination.exists():
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    name_without_ext = file_path.stem
                    destination = category_folder / f"{name_without_ext}_{timestamp}{file_extension}"
                
                # Move the file
                if dry_run:
                    logging.info(f"[DRY RUN] Would move: {file_path.name} -> {category}/")
                else:
                    shutil.move(str(file_path), str(destination))
                    logging.info(f"Moved: {file_path.name} -> {category}/")
                
                files_moved += 1
                
            except Exception as e:
                logging.error(f"Error processing {file_path.name}: {str(e)}")
                files_skipped += 1
        
        logging.info(f"Organization complete! Files moved: {files_moved}, Files skipped: {files_skipped}")
        return files_moved, files_skipped


def main():
    """Main function to run the file organizer."""
    print("=" * 60)
    print("Desktop File Organizer")
    print("=" * 60)
    
    # Get the folder to organize
    default_folder = str(Path.home() / "Downloads")
    print(f"\nDefault folder: {default_folder}")
    folder_input = input("Enter folder path to organize (or press Enter for default): ").strip()
    
    source_folder = folder_input if folder_input else default_folder
    
    try:
        organizer = FileOrganizer(source_folder)
        
        # Ask for dry run
        dry_run_input = input("\nDo you want to do a dry run first? (y/n): ").strip().lower()
        dry_run = dry_run_input == 'y'
        
        # Organize files
        organizer.organize_files(dry_run=dry_run)
        
        if dry_run:
            proceed = input("\nDo you want to proceed with actual organization? (y/n): ").strip().lower()
            if proceed == 'y':
                organizer.organize_files(dry_run=False)
        
        print("\n✓ Done! Check file_organizer.log for details.")
        
    except Exception as e:
        logging.error(f"Failed to organize files: {str(e)}")
        print(f"\n✗ Error: {str(e)}")


if __name__ == "__main__":
    main()
