from __future__ import annotations

from package.github_release.objects.meta import GitHubReleaseMeta

def main_wrapped() -> Exception | None:
    try:
        return main()
    except Exception as error:
        if not str(error):
            error = RuntimeError(
                "An unknown error has occurred. It might be an network issue."
            )
        return error.__repr__()

def main() -> None:
    from asyncio import run

    return run(main_async())

async def main_async() -> None:
    from pathlib import Path
    from .github_release import get_release_latest, parse_release_latest
    from .zip_extract import extract_filter
    from .argument import argparser
    
    argparser.print_help()
    print(argparser.parse_args())
    return

    payload = await get_release_latest(owner="gfx-rs", repo="wgpu-native")
    data = parse_release_latest(payload)

    Path("output.md").write_text(data.to_markdown())
    asset = data.search_assets(r"linux-a.*-debug\.zip$")[0]

    async for name, data in extract_filter(
        asset.download(show_progress=True),
        "zip-extract-output",
        name=r".*\.(?:h|dylib)$",
    ):
        print(name, data[:20])
