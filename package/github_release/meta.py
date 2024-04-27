from __future__ import annotations

from dataclasses import dataclass
from os import PathLike
from typing import TextIO


@dataclass
class GitHubReleaseMeta:
    """
    GitHub Release Metadata
    """

    tag: str
    date: str
    url: str
    note: str

    def __str__(self):
        pass

    @staticmethod
    def from_response_json(response: dict[str]) -> "GitHubReleaseMeta":
        return GitHubReleaseMeta(
            tag=response["tag_name"],
            date=response["published_at"],
            url=response["html_url"],
            note=response["body"],
        )
    
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
                raise ValueError("Target is not a writable file")
        else:
            dump(self.__dict__, Path(target).open("w"), indent=4)

    # def to_markdown(self) -> str:
    #     pass

    # def write_markdown(self, target: TextIO | PathLike | str):
    #     from io import TextIOBase

    #     from datetime import datetime

    #     description = {
    #         "tag": response["tag_name"],
    #         "date": datetime.fromisoformat(response["published_at"]).isoformat(),
    #         "url": response["html_url"],
    #         "note": response["body"],
    #     }
    #     yaml_dump(
    #         description,
    #         open("latest.yml", "w"),
    #         default_style="|",
    #         indent=4,
    #         sort_keys=False,
    #     )
