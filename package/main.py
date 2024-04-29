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

    pprint(payload, sort_dicts=False)
    pprint(data, sort_dicts=False)

    from io import StringIO

    fp = StringIO()
    print(data.assets[0].to_json(fp, indent=2))
    print(fp.closed, fp.getvalue())
    pprint(data)
    r_data = GitHubReleaseData.from_json(data.to_json(indent=2))
    pprint(r_data)
    print(r_data.to_json(indent=2))
