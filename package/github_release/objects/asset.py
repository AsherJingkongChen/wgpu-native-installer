from __future__ import annotations

from dataclasses import dataclass

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
