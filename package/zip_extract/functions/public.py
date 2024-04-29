from __future__ import annotations

from typing import AsyncIterable, AsyncGenerator, Pattern

async def extract_filter(
    source: AsyncIterable[bytes],
    name: str | Pattern[str] | None = None,
) -> AsyncGenerator[tuple[str, bytes]]:
    """
    ## Arguments
    - `source`:
        - An async iterable of zip file chunks
    - `name`:
        - Defaults to `None`

        ## Returns
        - (`list[tuple[str, bytes]]`)
            - Assets with names matching the pattern
            - All assets if `name` is `None`
    """
    from re2 import search
    from stream_unzip import async_stream_unzip

    if name:
        async for filename, _, content in async_stream_unzip(source):
            filename = filename.decode()
            if search(name, filename):
                yield filename, b"".join([d async for d in content])
            else:
                async for _ in content:
                    pass
    else:
        async for filename, _, content in async_stream_unzip(source):
            filename = filename.decode()
            yield filename, b"".join([d async for d in content])
