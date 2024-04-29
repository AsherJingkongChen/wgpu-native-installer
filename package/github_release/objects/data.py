from __future__ import annotations

from dataclasses import dataclass

from .asset import GitHubReleaseAsset
from .meta import GitHubReleaseMeta
from ...common.objects import JSON
from ...common.objects import Markdown


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
        assets = "".join([f"| {asset.to_markdown()} |\n" for asset in self.assets])
        return f"""\
{self.meta.to_markdown()}

## Assets

| Name | Type | Size |
| ---- | ---- | ---- |
{assets}"""
