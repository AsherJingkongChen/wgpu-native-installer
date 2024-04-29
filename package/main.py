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
    from .github_release.functions import (
        get_release_latest,
        parse_release_latest,
    )

    payload = await get_release_latest(owner="gfx-rs", repo="wgpu-native")
    data = parse_release_latest(payload)

    Path("output.md").write_text(data.to_markdown())
    asset = data.search_assets(r"macos-a.*-release\.zip$")[0]

    from stream_unzip import async_stream_unzip

    async for t in async_stream_unzip(asset.download()):
        print(t[0].decode(), t[1])
        async for _ in t[-1]: pass
