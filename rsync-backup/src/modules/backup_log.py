"""

Writes an optional Backup_Log.txt file to the target directory.
Entries: [File/Folder] - Complete - Date - Time
    
"""

from pathlib import Path
from datetime import datetime


def write_backup_log(source, target) -> None:
    """Writes an optional Backup_Log.txt file to the target directory.
    Entries: [File/Folder] - Complete - Date - Time

    Args:
        source (Path): Path pointing to the source file/folder.
        target (Path): Path pointing to the target folder.
    """
    # Gets the current date and time to build the log entry.
    date_time = datetime.now()
    current_date_time = date_time.strftime("%m/%d/%Y - %H:%M")
    log_entry = f"[{source.name}] - Complete - {current_date_time}\n"
    # Sets the path for the log file.
    log_file = Path(target).resolve() / "Backup_Log.txt"
    # Writes the log entry.
    with open(log_file, "a", encoding="utf-8") as text:
        text.write(log_entry)
