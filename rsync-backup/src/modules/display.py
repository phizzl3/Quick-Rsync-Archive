"""

Messages for display in the terminal. 

"""


def display_title(version) -> None:
    """Displays the title ASCII text to the terminal.

    Args:
        version (str): Package version.
    """
    title = f"""
    V{version}
    ██████╗ ███████╗██╗   ██╗███╗   ██╗ ██████╗      
    ██╔══██╗██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝      
    ██████╔╝███████╗ ╚████╔╝ ██╔██╗ ██║██║           
    ██╔══██╗╚════██║  ╚██╔╝  ██║╚██╗██║██║           
    ██║  ██║███████║   ██║   ██║ ╚████║╚██████╗      
    ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═══╝ ╚═════╝      
    ██████╗  █████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ 
    ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗
    ██████╔╝███████║██║     █████╔╝ ██║   ██║██████╔╝
    ██╔══██╗██╔══██║██║     ██╔═██╗ ██║   ██║██╔═══╝ 
    ██████╔╝██║  ██║╚██████╗██║  ██╗╚██████╔╝██║     
    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                        :phiZzL3        
"""

    print(title)


def display_completed(source, target) -> None:
    """Displays a message to the terminal showing the folders transferred.

    Args:
        source (Path): Path pointing to the source file/folder.
        target (Path): Path pointing to the target folder.
    """
    print("=" * 65)
    print("\n Archive of:")
    print(f" {source}")
    print("\n Into:")
    print(f" {target}")
    print("\n Complete.")
