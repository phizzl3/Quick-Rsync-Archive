"""

Generates and runs the terminal command for Rsync.
-a, -v, --progress
    
"""

import subprocess


def run_rsync_command(source, target) -> None:
    """Generates and runs the terminal command for Rsync.
    -a, -v, --progress

    Args:
        source (Path): Path pointing to the source file/folder.
        target (Path): Path pointing to the target folder.
    """
    source = str(source).replace(" ", "\\ ")
    target = str(target).replace(" ", "\\ ")

    subprocess.run(f"rsync -av --progress {source} {target}/", shell=True, check=False)
