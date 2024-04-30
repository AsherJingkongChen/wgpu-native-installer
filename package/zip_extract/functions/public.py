from __future__ import annotations

from os import PathLike
from typing import AsyncIterable, AsyncGenerator, Pattern

async def extract_filter(
    source: AsyncIterable[bytes],
    target: PathLike | str | None = None,
    *,
    name: Pattern[str] | str | None = None,
) -> AsyncGenerator[None | tuple[str, bytes]]:
    """
    ## Arguments
    - `source`:
        - An async iterable of zip file chunks
    - `target`:
        - It defaults to `None`
        - It is either:
            - A directory path (`PathLike | str`)
            - `None`
    - `name`:
        - It defaults to `None`

    ## Returns
    - Extracted assets with names matching the pattern
    - All extracted assets if `name` is `None`
    - Either:
        - (`AsyncGenerator[None]`)
            and the extracted assets are written under `target`
        - (`AsyncGenerator[tuple[str, bytes]]`),
            the extracted assets with names if `target` is `None`
    """

    from pathlib import Path
    from re2 import search
    from stream_unzip import async_stream_unzip

    if target:
        target = Path(target)
        target.mkdir(parents=True, exist_ok=True)

    async for filename, _, content in async_stream_unzip(source):
        filename: str = filename.decode()
        if (not name) or search(name, filename):
            if target:
                with (target / filename).open("wb") as target_file:
                    async for chunk in content:
                        target_file.write(chunk)
            else:
                yield filename, b"".join([chunk async for chunk in content])
        else:
            async for _ in content:
                pass
