from __future__ import annotations

from os import PathLike
from typing import TextIO

from ...common.functions.private import get_dict_from_dataclass_recursively

class JSON:
    """
    Basic object with basic JSON (de)serialization
    """

    def to_json(self, indent: int | None = None) -> str:
        """
        ## Arguments
        - `indent`: (`int | None`)
            - Defaults to `None`
        """
        from json import dumps

        object = get_dict_from_dataclass_recursively(self)
        return dumps(object, indent=indent)

    def write_json(
        self,
        target: TextIO | PathLike | str,
        indent: int | None = None,
    ) -> None:
        """
        ## Arguments
        - `target`:
            - It is either:
                - A writable text IO stream (`TextIO`)
                - A writable file path (`PathLike | str`)
        - `indent`: (`int | None`)
            - Defaults to `None`
        """

        from json import dump
        from io import TextIOBase
        from pathlib import Path
        
        object = get_dict_from_dataclass_recursively(self)

        if isinstance(target, TextIOBase):
            dump(object, target, indent=indent)
        else:
            with Path(target).open("w") as target:
                dump(object, target, indent=indent)
