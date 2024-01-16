"""

A small script to quickly generate an archive command for Rsync.
Gets source directory and target directory via drag-and-drop.
Archives source directory and its contents into target directory.

"""

import subprocess

from dropped_file_getter import get_dropped_file


print("\n Please drop the directory you would like to archive (source).")
print(" This folder and all of its contents will be archived.")
source = get_dropped_file()

print("\n Please drop the directory you would like to archive into (target).")
print(" The above folder and its contents will be archived into this folder.")
target = get_dropped_file()

# Shell command for rsync.
subprocess.run(f"rsync -av --progress {source} {target}/", shell=True, check=False)

print("\n Archive of:")
print(f" {source}")
print(" into:")
print(f" {target}")
input(" Complete.")
