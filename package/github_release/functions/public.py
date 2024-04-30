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

async def parse_release_latest(
    owner: str,
    repo: str,
    payload: dict[str] | None = None,
) -> GitHubReleaseData:
    """
    ## Arguments
    - `owner`:
        - The owner of the GitHub repository
    - `repo`:
        - The GitHub repository name
    - `payload`:
        - It defaults to `None`
        - The JSON payload of the latest release from the GitHub API
            - It will be fetched from the GitHub API if it is `None`

    ## Returns
    - The parsed GitHub release data
    """
    from ..objects import GitHubReleaseAsset, GitHubReleaseMeta

    if not payload:
        payload = await get_release_latest(owner, repo)

    return GitHubReleaseData(
        meta=GitHubReleaseMeta(
            url_api=payload["url"],
            url_html=payload["html_url"],
            owner=owner,
            repo=repo,
            name=payload["tag_name"],
            time=payload.get("published_at", payload["created_at"]),
            note=payload.get("body", ""),
        ),
        assets=[
            GitHubReleaseAsset(
                url_api=data["url"],
                url_download=data["browser_download_url"],
                name=data["name"],
                size=data["size"],
                type=data["content_type"],
            )
            for data in payload["assets"]
        ],
    )
