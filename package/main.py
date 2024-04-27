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
    from httpx import AsyncClient
    from .github_release.meta import GitHubReleaseMeta
    from pprint import pprint

    async with AsyncClient(http2=True) as client:
        response = (
            await client.get(
                "https://api.github.com/repos/gfx-rs/wgpu-native/releases/latest",
                headers={
                    "Accept": "application/vnd.github+json",
                    "X-GitHub-Api-Version": "2022-11-28",
                },
            )
        ).json()

        meta = GitHubReleaseMeta.from_response_json(response)

        pprint(meta, sort_dicts=False)
        pprint(
            [
                (e["name"], e["content_type"], e["created_at"], e["url"])
                for e in response["assets"]
            ]
        )
