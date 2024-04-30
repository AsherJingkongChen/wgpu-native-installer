from argparse import ArgumentParser
from platform import machine, system

from .argtype import ArgType

argparser = ArgumentParser(
    prog="wgpu_native_installer",
)

argparser.add_argument(
    "-V",
    "--version",
    action="version",
    version=f"wgpu-native-installer 0.0.0",
)

argparser.add_argument(
    "-m",
    "--machine",
    help="""
        The type of machine.
        It is similar to `uname -m` but more generic.
        It defaults to the current machine type.
    """,
    choices=["aarch64", "i686", "x86_64"],
    default=machine(),
    type=ArgType.machine,
)

argparser.add_argument(
    "-s",
    "--system",
    help="""
        The name of system or kernel.
        It is similar to `uname -s` but more generic.
        It defaults to the current system name.
    """,
    choices=["linux", "macos", "windows"],
    default=system(),
    type=ArgType.system,
)

argparser.add_argument(
    "-l",
    "--library",
    help="""
        The library types to include in the artifacts.
        They default to `dynamic`.
    """,
    choices=["dynamic", "static"],
    default=["dynamic"],
    nargs="+",
)

argparser.add_argument(
    "-g",
    "--debug",
    action="store_true",
    help="""
        The flag to specify whether to include
        debug information in the artifacts.
        It defaults to `False`.
    """,
    default=False,
)
