from __future__ import annotations

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

async def main_async() -> None:
    from pathlib import Path
    from sys import stdout
    from .argument import (
        argparser,
        get_asset_name_pattern,
        get_library_name_pattern,
    )
    from .github_release import parse_release_latest
    from .unzip import extract_filter

    parsed_args = argparser.parse_args()
    outdir: Path = parsed_args.directory
    verbose: int = parsed_args.verbose

    data = await parse_release_latest(owner="gfx-rs", repo="wgpu-native")
    asset = data.search_assets(get_asset_name_pattern(parsed_args))[0]

    if verbose >= 2:
        print(data, file=stdout)

    async for _ in extract_filter(
        source=asset.download(show_progress=verbose >= 1),
        target=outdir,
        name=get_library_name_pattern(parsed_args),
    ):
        pass