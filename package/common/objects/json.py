from __future__ import annotations

from os import PathLike
from typing import TextIO, Type, TypeVar

_T = TypeVar("_T")

class JSON:
    """
    Basic JSON (de)serialization
    """

    @classmethod
    def from_json(
        cls: Type[_T],
        literal: str | None = None,
        *,
        source: PathLike | str | TextIO | None = None,
    ) -> _T:
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

        if (not literal) == (not source):
            raise ValueError(
                "Either `literal` or `source` must be provided (exclusive or)"
            )

        if literal:
            result = cls(**loads(literal))
        if source:
            if not isinstance(source, TextIOBase):
                will_close_source = False
            else:
                will_close_source = True
                source = Path(source).open("r")

            result = cls(**load(source))

            if will_close_source:
                source.close()

        return result

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
        - Either:
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

        if target:
            if not isinstance(target, TextIOBase):
                target = Path(target).open("w")
                will_close_target = True
            else:
                will_close_target = False

            result = dump(data, target, indent=indent)
            if will_close_target:
                target.close()
        else:
            result = dumps(data, indent=indent)

        return result
