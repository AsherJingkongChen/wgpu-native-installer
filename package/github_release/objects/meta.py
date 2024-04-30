from __future__ import annotations

from dataclasses import dataclass

from ...format import JSON

@dataclass
class GitHubReleaseMeta(JSON):
    """
    GitHub Release Metadata

    ## Reference
    - [API Docs - Release](https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#get-a-release)
    """

    url_api: str
    "`application/vnd.github+json` `Release.url`"

    url_html: str
    "`application/vnd.github+json` `Release.html_url`"

    owner: str
    "The path parameter `owner` of `Get a release`"

    repo: str
    "The path parameter `repo` of `Get a release`"

    name: str
    "`application/vnd.github+json` `Release.tag_name`"

    time: str
    "`application/vnd.github+json` `Release.published_at` or `Release.created_at`"

    note: str
    '`application/vnd.github+json` `Release.body` or `""`'

    def to_markdown(self) -> str:
        return f"""\
# {self.owner} / {self.repo} / release / [{self.name}]({self.url_html})

> *`{self.time}`*

{self.note}"""
