from __future__ import annotations

from typing import Sequence, TextIO

def main_wrapped() -> Exception | None:
    from asyncio import run

    try:
        return run(main())
    except Exception as error:
        if not str(error):
            error = RuntimeError(
                "An unknown error has occurred. It might be a network issue."
            )
        return error.__repr__()

async def main(
    args: Sequence[str] | None = None,
    *,
    owner: str | None = None,
    repo: str | None = None,
    file_out_data: TextIO | None = None,
) -> None:
    """
    ## Arguments
    - `args`: It defaults to `sys.argv[1:]`
    - `owner`: It defaults to `"gfx-rs"`
    - `repo`: It defaults to `"wgpu-native"`
    - `file_out_data`:
        - It defaults to `sys.stdout`
        - It is used to write the data to the file when `parsed_args.verbose >= 2`
    """

    from pathlib import Path
    from sys import argv, stdout

    from .argument import (
        argparser,
        get_asset_name_pattern,
        get_library_name_pattern,
    )
    from .github_release import parse_release_latest
    from .unzip import extract_filter

    args = args or argv[1:]
    owner = owner or "gfx-rs"
    repo = repo or "wgpu-native"
    file_out_data = file_out_data or stdout

    parsed_args = argparser.parse_args(args)
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
