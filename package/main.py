from __future__ import annotations

from package.github_release.objects.meta import GitHubReleaseMeta

def main_wrapped() -> Exception | None:
    try:
        return main()
    except Exception as error:
        if not str(error):
            error = RuntimeError(
                "An unknown error has occurred. It might be an network issue."
            )
        return error.__repr__()

def main() -> None:
    from asyncio import run

    return run(main_async())

async def main_async() -> None:
    from pathlib import Path
    from .github_release import get_release_latest, parse_release_latest
    from .zip_extract import extract_filter
    from .argument import argparser, get_asset_name_pattern, get_library_name_pattern

    argparser.print_help()
    parsed_args = argparser.parse_args()
    asset_pat = get_asset_name_pattern(parsed_args)
    lib_pat = get_library_name_pattern(parsed_args)

    print(parsed_args)
    print(asset_pat.search("wgpu-macos-aarch64-debug.zip"))
    print(lib_pat.search("libwgpu_native.dylib"))
    print(lib_pat.search("libwgpu_native.so"))
    print(lib_pat.search("libwgpu_native.dll"))
    print(lib_pat.search("libwgpu_native.dll.lib"))
    print(lib_pat.search("libwgpu_native.a"))
    print(lib_pat.search("libwgpu_native.lib"))
    print(lib_pat.search("libwgpu_native.pdb"))
    print(lib_pat.search("wgpu.h"))
    return

    payload = await get_release_latest(owner="gfx-rs", repo="wgpu-native")
    data = parse_release_latest(payload)

    Path("output.md").write_text(data.to_markdown())
    asset = data.search_assets(r"linux-a.*-debug\.zip$")[0]

    async for name, data in extract_filter(
        asset.download(show_progress=True),
        "zip-extract-output",
        name=r".*\.(?:h|dylib)$",
    ):
        print(name, data[:20])
