"""

Writes the optional "archived" file to the target directory.
[File/Folder]-Date-Time
    
"""

from pathlib import Path
from datetime import datetime


def write_archived_file(source, target) -> None:
    """Writes the optional "archived" file to the target directory.
    [File/Folder]-Date-Time

    Args:
        source (Path): Path pointing to the source file/folder.
        target (Path): Path pointing to the target folder.
    """
    date_time = datetime.now()
    current_date_time = date_time.strftime("%Y.%m.%d-%H.%M")
    archived_file = f"[{source.name}]-Archived-{current_date_time}"
    output_path = Path(target).resolve() / archived_file
    Path(output_path).touch()
