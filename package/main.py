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
    from pprint import pprint
    from pathlib import Path
    from .github_release.functions import get_release_latest, parse_release_latest
    from .github_release.objects import GitHubReleaseData

    payload = await get_release_latest(owner="gfx-rs", repo="wgpu-native")
    data = parse_release_latest(payload)

    Path("output.md").write_text(data.to_markdown())
    asset = data.search_assets(r"linux-aarch64-release\.zip$")[0]

    async for _ in asset.download("output.zip"):
        pass
