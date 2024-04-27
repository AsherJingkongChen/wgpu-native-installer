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

    payload = await get_release_latest(owner="gfx-rs", repo="wgpu-native")
    data = parse_release_latest(payload)
    
    pprint(data)
    
