from dataclasses import dataclass, is_dataclass

from package.format import JSON

@dataclass
class Inner(JSON):
    inner_value: str

@dataclass
class Outer(JSON):
    inner: Inner
    outer_value: float

    def __post_init__(self):
        if not is_dataclass(self.inner):
            self.inner = Inner(**self.inner)

@dataclass
class Simple(JSON):
    flag: bool
    none: None

def test_to_json_from_json_equal():
    source = Outer(inner=Inner("label"), outer_value=3.14)
    result_to = source.to_json()
    result_from = Outer.from_json(result_to)
    result_from_to = result_from.to_json()

    assert (
        result_to == '{"inner": {"inner_value": "label"}, "outer_value": 3.14}'
    )
    assert result_from == source
    assert result_from_to == result_to

def test_to_json_targets_equal():
    from io import StringIO
    from tempfile import NamedTemporaryFile

    source = Simple(flag=True, none=None)
    strfile = StringIO()
    tempfile = NamedTemporaryFile(mode="w+")

    result_none = source.to_json(target=None)

    result_path = source.to_json(target=tempfile.name)
    tempfile.seek(0)
    result_path_str = tempfile.read()
    tempfile.close()

    result_txio = source.to_json(target=strfile)
    result_txio_str = strfile.getvalue()
    strfile.close()

    assert type(result_none) is str
    assert result_path is None
    assert result_txio is None

    assert result_none == result_path_str
    assert result_none == result_txio_str

def test_indent_diff():
    source = Simple(flag=True, none=None)

    result_level_n = source.to_json(indent=None)
    result_level_0 = source.to_json(indent=0)
    result_level_2 = source.to_json(indent=2)

    assert result_level_n == '{"flag": true, "none": null}'
    assert result_level_0 == '{\n"flag": true,\n"none": null\n}'
    assert result_level_2 == '{\n  "flag": true,\n  "none": null\n}'
