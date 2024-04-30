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

    system = parsed_args.system
    machine = parsed_args.machine
    mode = parsed_args.debug and "debug" or "release"

    return compile(fr"{system}.{machine}.{mode}\.zip$")

def get_library_name_pattern(parsed_args: Namespace) -> Pattern[str]: ...
