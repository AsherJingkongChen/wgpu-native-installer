from dataclasses import dataclass
from os import PathLike
from typing import TextIO

from ...common.objects import JSON


@dataclass
class GitHubReleaseAsset(JSON):
    """
    GitHub Release Asset

    ## Reference
    - [API Docs - Release Asset](https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#get-a-release-asset)
    """

    url_api: str
    "`application/vnd.github+json` `Release.url`"

    name: str
    "`application/vnd.github+json` `Release.name`"

    size: str
    "`application/vnd.github+json` `Release.size`"

    type: str
    "`application/vnd.github+json` `Release.type`"

    def __str__(self):
        pass

    def to_markdown(self) -> str:
        pass

    def write_markdown(self, target: TextIO | PathLike | str) -> None:
        pass
