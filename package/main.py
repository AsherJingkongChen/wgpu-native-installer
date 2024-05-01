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
    from .github_release import parse_release_latest
    from .zip_extract import extract_filter
    from .argument import (
        argparser,
        get_asset_name_pattern,
        get_library_name_pattern,
    )

    parsed_args = argparser.parse_args()

    data = await parse_release_latest(owner="gfx-rs", repo="wgpu-native")
    asset = data.search_assets(get_asset_name_pattern(parsed_args))[0]

    Path("output.md").write_text(data.to_markdown())
    async for filename, filedata in extract_filter(
        asset.download(show_progress=True),
        "zip-extract-output",
        name=get_library_name_pattern(parsed_args),
    ):
        print(filename, filedata[:16] + b" ...")
