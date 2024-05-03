from __future__ import annotations

from argparse import Namespace
from typing import TextIO

def main_wrapped() -> Exception | None:
    try:
        return main()
    except Exception as error:
        if not str(error):
            error = RuntimeError(
                "An unknown error has occurred. It might be a network issue."
            )
        return error.__repr__()

def main() -> None:
    from asyncio import run

    return run(main_async())

async def main_async(
    *,
    parsed_args: Namespace | None = None,
    owner: str | None = None,
    repo: str | None = None,
    file_out_data: TextIO | None = None,
) -> None:
    """
    ## Arguments
    - `parsed_args`: It defaults to `.argument.argparser.parse_args()`
    - `owner`: It defaults to `"gfx-rs"`
    - `repo`: It defaults to `"wgpu-native"`
    - `file_out_data`:
        - It defaults to `sys.stdout`
        - It is used to write the data to the file when `parsed_args.verbose >= 2`
    """

    from pathlib import Path
    from sys import stdout
    from .argument import (
        argparser,
        get_asset_name_pattern,
        get_library_name_pattern,
    )
    from .github_release import parse_release_latest
    from .unzip import extract_filter

    parsed_args = parsed_args or argparser.parse_args()
    owner = owner or "gfx-rs"
    repo = repo or "wgpu-native"
    file_out_data = file_out_data or stdout

    outdir: Path = parsed_args.directory
    verbose: int = parsed_args.verbose

    data = await parse_release_latest(owner=owner, repo=repo)
    asset = data.search_assets(get_asset_name_pattern(parsed_args))[0]

    if verbose >= 2:
        file_out_data.write(str(data))

    async for _ in extract_filter(
        source=asset.download(show_progress=verbose >= 1),
        target=outdir,
        name=get_library_name_pattern(parsed_args),
    ):
        pass
