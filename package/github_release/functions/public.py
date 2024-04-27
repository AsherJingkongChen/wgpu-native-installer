from ..objects import GitHubReleaseData


async def get_release_latest(owner: str, repo: str) -> dict[str]:
    from httpx import AsyncClient

    async with AsyncClient(http2=True) as client:
        return (
            await client.get(
                f"https://api.github.com/repos/{owner}/{repo}/releases/latest",
                headers={
                    "Accept": "application/vnd.github+json",
                    "X-GitHub-Api-Version": "2022-11-28",
                },
            )
        ).json()


def parse_release_latest(payload: dict[str]) -> GitHubReleaseData:
    from ..objects import GitHubReleaseAsset, GitHubReleaseMeta

    return GitHubReleaseData(
        meta=GitHubReleaseMeta(
            url_api=payload["url"],
            name=payload["tag_name"],
            time=payload["created_at"],
            url_html=payload["html_url"],
            note=payload["body"],
        ),
        assets=[
            GitHubReleaseAsset(
                url_api=data["url"],
                name=data["name"],
                size=data["size"],
                type=data["content_type"],
            )
            for data in payload["assets"]
        ],
    )
