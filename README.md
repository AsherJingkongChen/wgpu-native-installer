# wgpu-native-installer

> Install wgpu-native

[![PyPI](https://img.shields.io/pypi/v/wgpu-native-installer?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/wgpu-native-installer/)
[![PyPI](https://img.shields.io/pypi/pyversions/wgpu-native-installer?style=for-the-badge&logo=python&logoColor=white)](https://pypi.org/project/wgpu-native-installer/)

## Introduction

Install the GitHub assets from [gfx-rs/wgpu-native](https://github.com/gfx-rs/wgpu-native).

The installer has additional options to customize the installation.

## Installation

Choose one of the following methods:

1. Install the package from PyPI:

   Website [link](https://pypi.org/project/wgpu-native-installer/)

   ```shell
   pip install wgpu-native-installer
   ```

2. Install the package from GitHub:

   Website [link](https://github.com/AsherJingkongChen/wgpu-native-installer/releases/latest)

   ```shell
   curl -LO $ASSET_URL_ends_with_whl
   pip install *.whl
   ```

## Usage

Choose one of the following methods. It depends on your requirements.

1. Download the artifacts of wgpu-native on your machine:

   ```shell
   python -m wgpu_native_installer -v
   ls -l
   # c++ -L. -lwgpu_native ....
   ```

2. Import the CLI as a package:

    ```python
    from asyncio import run
    from wgpu_native_installer import main as install_wgpu_native

    if __name__ == "__main__":
        run(install_wgpu_native(["-vv", "--library", "dynamic", "static"]))
    ```

    ```python
    from asyncio import run
    from wgpu_native_installer.github_release import parse_release_latest

    async def amain():
        release = await parse_release_latest("pytorch", "pytorch")
        asset = release.search_assets(r".*\.tar\.gz")[0]
        async for _ in asset.download("pytorch-latest.tar.gz", show_progress=True):
            pass

    if __name__ == "__main__":
        run(amain())
    ```

3. Clone the repository and reuse the codes you like:

   ```shell
   git clone https://github.com/AsherJingkongChen/wgpu-native-installer.git
   ```

## Details

### Goals

As one of my Python package templates, it should be TSPC-compliant.

- Tested
- Simple
- Performant
- Customizable

## License

[MIT](./LICENSE)
