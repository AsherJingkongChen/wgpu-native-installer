from package.github_release.objects import GitHubReleaseAsset
from pytest import mark


def test_download_client_not_closed():
    pass


@mark.asyncio
async def test_download_equal():
    from tempfile import NamedTemporaryFile
    from io import BytesIO

    source = GitHubReleaseAsset(
        url_api="",
        url_download="https://raw.githubusercontent.com/AsherJingkongChen/wgpu-native-installer/main/README.md",
        name="",
        size=0,
        type="",
    )
    bytefile = BytesIO()
    tempfile = NamedTemporaryFile(mode="w+b")

    result_none = b"".join([d async for d in source.download(target=None)])

    result_path = b"".join([d async for d in source.download(target=tempfile.name)])
    tempfile.seek(0)
    result_path_str = tempfile.read()
    tempfile.close()

    result_byio = b"".join([d async for d in source.download(target=bytefile)])
    result_byio_str = bytefile.getvalue()
    bytefile.close()

    assert type(result_none) is bytes
    assert result_path == b""
    assert result_byio == b""

    assert result_none == result_path_str
    assert result_none == result_byio_str
