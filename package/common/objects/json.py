from __future__ import annotations

from os import PathLike
from typing import TextIO


class JSON:
    """
    Basic object with basic JSON (de)serialization
    """

    @classmethod
    def from_json(
        cls,
        literal: str | None = None,
        *,
        source: PathLike | str | TextIO | None = None,
    ) -> JSON:
        """
        ## Arguments
        - `literal`: (`str | None`)
            - Defaults to `None`
        - `source`:
            - Defaults to `None`
            - It is either:
                - A readable text IO stream (`TextIO`)
                - A readable file path (`PathLike | str`)
                - `None`

        ## Returns
        - A new instance built from either `literal` or `source`
        """

        from io import TextIOBase
        from json import load, loads
        from pathlib import Path

        if (literal is None) is (source is None):
            raise ValueError("Either `literal` or `source` must be provided (eXclusive OR)")
        if literal is not None:
            return cls(**loads(literal))
        if source is not None:
            if isinstance(target, TextIOBase):
                return cls(**load(source))
            else:
                with Path(source).open("r") as target:
                    return cls(**load(source))

    def to_json(
        self,
        target: PathLike | str | TextIO | None = None,
        indent: int | None = None,
    ) -> None | str:
        """
        ## Arguments
        - `target`:
            - Defaults to `None`
            - It is either:
                - A writable text IO stream (`TextIO`)
                - A writable file path (`PathLike | str`)
                - `None`
        - `indent`: (`int | None`)
            - Defaults to `None`

        ## Returns
        - It is either:
            - `None` and the JSON text is written to `target`
            - A JSON text (`str`) if `target` is `None`
        """

        from dataclasses import asdict, is_dataclass
        from json import dump, dumps
        from io import TextIOBase
        from pathlib import Path

        if is_dataclass(self):
            data = asdict(self)
        else:
            data = self

        if target is None:
            return dumps(data, indent=indent)
        elif isinstance(target, TextIOBase):
            return dump(data, target, indent=indent)
        else:
            with Path(target).open("w") as target:
                return dump(data, target, indent=indent)
