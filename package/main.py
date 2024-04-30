from __future__ import annotations

def main_wrapped() -> Exception | None:
    try:
        return main()
    except Exception as error:
        return error

def main() -> None:
    from asyncio import run

    return run(main_async())

async def main_async() -> None:
    from pathlib import Path
    from .github_release import get_release_latest, parse_release_latest
    from .zip_extract import extract_filter

    payload = await get_release_latest(owner="gfx-rs", repo="wgpu-native")
    data = parse_release_latest(payload)

    Path("output.md").write_text(data.to_markdown())
    asset = data.search_assets(r"linux-a.*-debug\.zip$")[0]

    async for name, data in extract_filter(
        asset.download(),
        "zip-extract-output",
        # name=r".*\.(?:h|dylib)$",
    ):
        print(name, data[:20])
