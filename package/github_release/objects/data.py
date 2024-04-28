from __future__ import annotations

from dataclasses import dataclass
from os import PathLike
from typing import TextIO

from .asset import GitHubReleaseAsset
from .meta import GitHubReleaseMeta
from ...common.objects import JSON


@dataclass
class GitHubReleaseData(JSON):
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

    def __str__(self):
        pass

    def to_markdown(self) -> str:
        pass

    def write_markdown(self, target: TextIO | PathLike | str) -> None:
        pass
