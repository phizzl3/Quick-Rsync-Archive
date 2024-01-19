# Quick-Rsync-Archive

A script to quickly generate an archive command for Rsync.
Gets source directory and target directory via drag-and-drop.
Archives source directory and its contents into target directory.
(Optionally) adds a file into the target directory with date and time 
of archive completion.

Written for MacOS, but should also work on Linux.

## PyInstaller build info

```bash
pyinstaller --onefile quick-rsync-archive/src/quick_rsync_archive.py
```
