# Quick-Rsync-Archive
A script to quickly generate an archive command for Rsync.
Gets source directory and target directory via drag-and-drop.
Archives source directory and its contents into target directory.
(Optionally) adds a file into the target directory with date and time of archive completion.  
"[File/Folder]-Archived_On-Date-Time"

Written for MacOS, but should also work on Linux.

## Note  

Requires Rsync to be installed first.

## PyInstaller build info

```bash
pyinstaller -F -n "Rsync Backup" rsync-backup/src/rsync_backup.py
```
