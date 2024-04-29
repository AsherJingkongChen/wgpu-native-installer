from __future__ import annotations

from dataclasses import dataclass
from os import PathLike
from typing import BinaryIO


from ...common.functions import get_human_readable_byte_size
from ...common.objects import JSON
from ...common.objects import Markdown


@dataclass
class GitHubReleaseAsset(JSON, Markdown):
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
    "`application/vnd.github+json` `Release.content_type`"

    def to_markdown(self) -> str:
        size = get_human_readable_byte_size(self.size)
        return f"[{self.name}]({self.url_api}) | `{self.type}` | `{size}`"

    def download(
        self,
        target: BinaryIO | PathLike | str | None = None,
    ) -> None | bytes:
        """
        ## Arguments
        - `target`:
            - Defaults to `None`
            - It is either:
                - A writable binary IO stream (`BinaryIO`)
                - A writable file path (`PathLike | str`)
                - `None`

        ## Returns
        - Either:
            - `None` and the content is written to `target`
            - The content (`bytes`) if `target` is `None`
        """
