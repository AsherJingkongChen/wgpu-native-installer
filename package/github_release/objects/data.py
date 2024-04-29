from __future__ import annotations

from dataclasses import dataclass
from typing import Pattern

from .asset import GitHubReleaseAsset
from .meta import GitHubReleaseMeta
from ...format import JSON, Markdown

@dataclass
class GitHubReleaseData(JSON, Markdown):
    """
    GitHub Release Data

    ## Reference
    - [API Docs - Release](https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#get-a-release)
    - [API Docs - Release Asset](https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#get-a-release-asset)
    """

    meta: GitHubReleaseMeta
    "Metadata"

    assets: list[GitHubReleaseAsset]
    "Assets"

    def __post_init__(self) -> None:
        from dataclasses import is_dataclass

        if not is_dataclass(self.meta):
            self.meta = GitHubReleaseMeta(**self.meta)
        self.assets = [
            GitHubReleaseAsset(**asset) if not is_dataclass(asset) else asset
            for asset in self.assets
        ]

    def to_markdown(self) -> str:
        assets = "".join(
            [f"| {asset.to_markdown()} |\n" for asset in self.assets]
        )
        return f"""\
{self.meta.to_markdown()}

## Assets

| Name | Type | Size |
| ---- | ---- | ---- |
{assets}"""

    def search_assets(
        self,
        name: str | Pattern[str] | None = None,
    ) -> list[GitHubReleaseAsset]:
        """
        ## Arguments
        - `name`:
            - Defaults to `None`

        ## Returns
        - (`list[GitHubReleaseAsset]`)
            - Assets with names matching the pattern
            - All assets if `name` is `None`
        """
        from re2 import search

        if name:
            return [asset for asset in self.assets if search(name, asset.name)]
        else:
            return self.assets
