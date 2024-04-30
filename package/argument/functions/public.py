from argparse import Namespace
from typing import Pattern

def get_asset_name_pattern(parsed_args: Namespace) -> Pattern[str]:
    """
    Get the asset name pattern based on the parsed arguments

    ## Parameters
    - `parsed_args`:
        - The parsed arguments

    ## Returns
    - The asset file name pattern
    """

    from re2 import compile

    machine: str = parsed_args.machine
    mode: str = parsed_args.debug and "debug" or "release"
    system: str = parsed_args.system

    return compile(rf"{system}.{machine}.{mode}\.zip$")

def get_library_name_pattern(parsed_args: Namespace) -> Pattern[str]:
    """
    Get the library name pattern based on the parsed arguments

    ## Parameters
    - `parsed_args`:
        - The parsed arguments

    ## Returns
    - The library file name pattern
        - Header files are always included
    """

    from re2 import compile

    debug: bool = parsed_args.debug
    library = set(parsed_args.library)
    system = parsed_args.system

    suffixes: list[str] = []

    # Add suffixes of headers
    suffixes.append(r"h")
    suffixes.append(r"hpp")

    # Add suffixes of dynamic or static library
    if "dynamic" in library:
        if system == "linux":
            suffixes.append(r"so")
        elif system == "macos":
            suffixes.append(r"dylib")
        elif system == "windows":
            suffixes.append(r"dll")
            suffixes.append(r"dll\.lib")
    if "static" in library:
        if system == "linux":
            suffixes.append(r"a")
        elif system == "macos":
            suffixes.append(r"a")
        elif system == "windows":
            suffixes.append(r"lib")

    # Add suffixes of debug information
    if debug:
        if system == "windows":
            suffixes.append(r"pdb")

    # Combine all suffixes
    suffixes: str = "|".join(suffixes)

    return compile(rf"\.(?:{suffixes})$")
