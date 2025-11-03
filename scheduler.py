"""
Scheduler for File Organizer
Runs the file organizer at specified intervals.
"""

import schedule
import time
from pathlib import Path
from file_organizer import FileOrganizer
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def organize_job(folder_path):
    """Job to organize files in the specified folder."""
    try:
        organizer = FileOrganizer(folder_path)
        organizer.organize_files(dry_run=False)
    except Exception as e:
        logging.error(f"Scheduled organization failed: {str(e)}")


def main():
    """Set up and run the scheduler."""
    print("File Organizer Scheduler")
    print("=" * 60)
    
    # Get folder to monitor
    default_folder = str(Path.home() / "Downloads")
    folder_input = input(f"Enter folder path to monitor (default: {default_folder}): ").strip()
    folder_path = folder_input if folder_input else default_folder
    
    # Get schedule interval
    print("\nSchedule options:")
    print("1. Every hour")
    print("2. Every day at specific time")
    print("3. Every week")
    
    choice = input("Choose option (1-3): ").strip()
    
    if choice == "1":
        schedule.every().hour.do(organize_job, folder_path)
        print(f"\n✓ Scheduled to run every hour")
    elif choice == "2":
        time_input = input("Enter time (HH:MM, 24-hour format): ").strip()
        schedule.every().day.at(time_input).do(organize_job, folder_path)
        print(f"\n✓ Scheduled to run daily at {time_input}")
    elif choice == "3":
        day = input("Enter day (monday/tuesday/etc.): ").strip().lower()
        time_input = input("Enter time (HH:MM, 24-hour format): ").strip()
        getattr(schedule.every(), day).at(time_input).do(organize_job, folder_path)
        print(f"\n✓ Scheduled to run every {day} at {time_input}")
    else:
        print("Invalid choice. Exiting.")
        return
    
    print(f"Monitoring: {folder_path}")
    print("Press Ctrl+C to stop\n")
    
    # Run the scheduler
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        print("\n\nScheduler stopped.")


if __name__ == "__main__":
    main()
