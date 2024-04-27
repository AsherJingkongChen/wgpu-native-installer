from __future__ import annotations

from dataclasses import dataclass
from os import PathLike
from typing import TextIO

from .asset import GitHubReleaseAsset
from .meta import GitHubReleaseMeta

@dataclass
class GitHubReleaseData:
    """
    GitHub Release Data

    ## Reference
    - [API Docs - Release](https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#get-a-release)
    - [API Docs - Release Asset](https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#get-a-release-asset)
    """

    meta: GitHubReleaseMeta
    assets: list[GitHubReleaseAsset]

    def __str__(self):
        pass

    def to_json(self) -> str:
        from json import dumps

        return dumps(self.__dict__, indent=4)

    def write_json(self, target: TextIO | PathLike | str) -> None:
        from json import dump
        from io import TextIOBase
        from pathlib import Path

        if isinstance(target, TextIOBase):
            if target.writable():
                target.write(self.to_json())
            else:
                raise ValueError("target is not a writable file")
        else:
            dump(self.__dict__, Path(target).open("w"), indent=4)

    def to_markdown(self) -> str:
        pass

    def write_markdown(self, target: TextIO | PathLike | str) -> None:
        pass
