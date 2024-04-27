#! /usr/bin/env python3

from setuptools import setup

setup(
    name="wgpu-native-installer",
    version="0.0.0",
    author="Asher Jingkong Chen",
    description="Install wgpu-native",
    license="MIT",
    packages=["wgpu_native_installer"],
    package_dir={"wgpu_native_installer": "package"},
)
