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
    from .github_release.objects import GitHubReleaseAsset, GitHubReleaseData

    payload = await get_release_latest(owner="gfx-rs", repo="wgpu-native")
    data = parse_release_latest(payload)

    Path("output.md").write_text(data.to_markdown())
    asset = data.search_assets(r"linux-aarch64-release\.zip$")[0]
    print(asset.to_json(indent=2))
    asset = GitHubReleaseAsset(
        url_api="",
        url_download="https://raw.githubusercontent.com/AsherJingkongChen/wgpu-native-installer/main/README.md",
        name="",
        size=0,
        type="",
    )
    async for _ in asset.download("test.md"):
        pass
