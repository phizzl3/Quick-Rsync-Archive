"""

A script to quickly generate an archive command for Rsync.
Gets source directory and target directory via drag-and-drop.
Archives source directory and its contents into target directory.
(Optionally) adds a file into the target directory with date and time 
of archive completion.

"""


from modules import (
    display_title,
    display_completed,
    get_target,
    get_source,
    run_rsync_command,
    write_archived_file,
    clear_screen,
)


VERSION = "0.2.1"
"""Package version."""

WRITE_ARCHIVED_FILE = True
"""Flag to write archived file with date and time to target directory."""

clear_screen()
display_title(VERSION)

SOURCE = get_source()
TARGET = get_target()

run_rsync_command(SOURCE, TARGET)

display_completed(SOURCE, TARGET)

if WRITE_ARCHIVED_FILE:
    write_archived_file(SOURCE, TARGET)
