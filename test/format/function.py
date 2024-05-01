def test_get_human_readable_byte_size_example():
    from package.format.functions import get_human_readable_byte_size

    assert get_human_readable_byte_size(1024) == "1 KiB"
    assert get_human_readable_byte_size(1000) == "1000 B"
