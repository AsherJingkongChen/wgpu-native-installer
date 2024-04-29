def get_human_readable_byte_size(size_in_byte: int) -> str:
    n = int(size_in_byte)
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if n < 1024:
            return f"{n} {unit}B"
        n >>= 10
    return f"{n} YiB"
