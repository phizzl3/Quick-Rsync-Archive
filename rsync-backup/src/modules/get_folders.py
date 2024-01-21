"""

Gets the source file/folder path and target folder path via drag-and-drop.

"""


from pathlib import Path

from modules import get_dropped_file


def get_source() -> Path:
    """Gets the source file/folder path via drag-and-drop.

    Returns:
        Path: Path pointing to the source file/folder.
    """
    print("\n Please drop the file or directory you would like to archive (source).")
    print(" This file or folder and all of its contents will be archived.")
    return get_dropped_file()


def get_target() -> Path:
    """Gets the target folder path via drag-and-drop.

    Returns:
        Path: Path pointing to the target directory.
    """
    print("\n Please drop the directory you would like to archive into (target).")
    print(
        " The above file or folder and its contents will be archived into this folder."
    )
    return get_dropped_file()
