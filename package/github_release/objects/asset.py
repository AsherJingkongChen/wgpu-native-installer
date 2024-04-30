from __future__ import annotations

from dataclasses import dataclass
from httpx import AsyncClient
from os import PathLike
from typing import BinaryIO, AsyncGenerator

from ...common import get_human_readable_byte_size
from ...format import JSON, Markdown

@dataclass
class GitHubReleaseAsset(JSON, Markdown):
    """
    GitHub Release Asset

    ## Reference
    - [API Docs - Release Asset](https://docs.github.com/en/rest/releases/assets?apiVersion=2022-11-28#get-a-release-asset)
    """

    url_api: str
    "`application/vnd.github+json` `ReleaseAsset.url`"

    url_download: str
    "`application/vnd.github+json` `ReleaseAsset.browser_download_url`"

    name: str
    "`application/vnd.github+json` `ReleaseAsset.name`"

    size: int
    "`application/vnd.github+json` `ReleaseAsset.size`"

    type: str
    "`application/vnd.github+json` `ReleaseAsset.content_type`"

    def to_markdown(self) -> str:
        size = get_human_readable_byte_size(self.size)
        return f"[{self.name}]({self.url_download}) | `{self.type}` | `{size}`"

    async def download(
        self,
        target: BinaryIO | PathLike | str | None = None,
        client: AsyncClient | None = None,
        *,
        show_progress: bool | None = None,
    ) -> AsyncGenerator[None | bytes]:
        """
        ## Arguments
        - `target`:
            - Defaults to `None`
            - It is either:
                - A writable binary IO stream (`BinaryIO`)
                - A writable file path (`PathLike | str`)
                - `None`
        - `client`:
            - Defaults to `None`
            - It will be used to download the asset if provided
        - `show_progress`:
            - Defaults to `None`
            - A progress bar will be shown if `True`

        ## Returns
        - Either:
            - (`AsyncGenerator[None]`) and the stream content is written to `target`
            - (`AsyncGenerator[bytes]`), the stream content if `target` is `None`
        """

        from io import BufferedIOBase, RawIOBase
        from pathlib import Path
        from tqdm.auto import tqdm

        if client:
            will_close_client = False
        else:
            will_close_client = True
            client = AsyncClient(http2=True)

        async with client.stream(
            "GET",
            self.url_download,
            follow_redirects=True,
            headers={"Accept": "application/octet-stream"},
        ) as response:

            progress_bar = tqdm(
                disable=not show_progress,
                desc=f"Downloading {self.name}",
                ascii="         |",
                colour="blue",
                dynamic_ncols=True,
                unit="B",
                unit_scale=True,
                unit_divisor=1 << 10,
                mininterval=0.2,
                miniters=0,
                smoothing=0,
                total=self.size,
            )

            if target:
                if isinstance(target, (BufferedIOBase, RawIOBase)):
                    will_close_target = False
                else:
                    will_close_target = True
                    target = Path(target).open("wb")

                async for chunk in response.aiter_bytes():
                    target.write(chunk)
                    progress_bar.update(len(chunk))

                if will_close_target:
                    target.close()
            else:
                async for chunk in response.aiter_bytes():
                    yield chunk
                    progress_bar.update(len(chunk))

            progress_bar.close()

        if will_close_client:
            await client.aclose()
