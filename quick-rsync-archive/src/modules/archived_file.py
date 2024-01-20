"""

Writes the optional "Archived_On" file to the target directory.
[File/Folder]-Archived_On-Date-Time
    
"""

from pathlib import Path
from datetime import datetime


def write_archived_file(source, target) -> None:
    """Writes the optional "archived" file to the target directory.
    [File/Folder]-Archived_On-Date-Time

    Args:
        source (Path): Path pointing to the source file/folder.
        target (Path): Path pointing to the target folder.
    """
    # Gets the current date and time to build the output file name.
    date_time = datetime.now()
    current_date_time = date_time.strftime("%Y.%m.%d-%H.%M")
    archived_file = f"[{source.name}]-Archived_On-{current_date_time}"
    # Sets the path for the output file.
    output_path = Path(target).resolve() / archived_file
    # Removes the escape characters from the path so they aren't duplicated
    # when creating the new output file path when "touch" is called.
    output_path = str(output_path).replace("\\", "")
    try:
        # Creates the "Archived On" file in the target directory.
        Path(output_path).touch()
        print('\n "Archived On" file created in target directory.')
    except FileNotFoundError:
        print('\n Unable to create "Archived On" file in target directory.')
