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
    from .github_release.functions import get_release_latest, parse_release_latest
    from .github_release.objects import GitHubReleaseData

    payload = await get_release_latest(owner="gfx-rs", repo="wgpu-native")
    data = parse_release_latest(payload)

    r_data = GitHubReleaseData.from_json(data.to_json(indent=2))
    pprint(r_data)
    print(4, r_data, file=open("output.md", "w"))
    print(5, r_data.to_json(indent=2))
    pprint(r_data.find_assets(r"release\.zip$"))
