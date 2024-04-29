def get_human_readable_byte_size(size_in_byte: int) -> str:
    n = size_in_byte
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(n) < 1024.0:
            return f"{n:3.1f}{unit}B"
        n /= 1024.0
    return f"{n:.1f}YiB"
