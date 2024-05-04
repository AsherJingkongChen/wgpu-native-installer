from argparse import ArgumentParser
from os import curdir
from pathlib import Path
from platform import machine, system

from ... import __version__
from .argtype import ArgType

argparser = ArgumentParser(
    prog="wgpu_native_installer",
    epilog="""
        example: %(prog)s -vv -d out -s linux -m x64 -g -l d s > out.md
    """,
)

argparser.add_argument(
    "-V",
    "--version",
    action="version",
    version=__version__,
)

argparser.add_argument(
    "-d",
    "--directory",
    help="""
        The directory to store the artifacts.
        
        It defaults to the current directory.
    """,
    metavar="Directory_Path",
    default=curdir,
    type=Path,
)

argparser.add_argument(
    "-m",
    "--machine",
    help="""
        The type of machine.
        It is similar to `uname -m` but more generic.
        It can be arm64, armv8l (for aarch64), x86 (for i686), x64 (for x86_64) or more.

        It defaults to the current machine type.
    """,
    metavar="Machine_Type",
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
        It can be Linux (for linux), Darwin, mac (for macos), MinGW, NT, win (for windows) or more.
        
        It defaults to the current system name.
    """,
    metavar="System_Name",
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
        
        They can be dynamic, d, shared (for dynamic) or static, s, archived (for static).
    """,
    metavar="Library_Type",
    choices=["dynamic", "static"],
    default=["dynamic"],
    nargs="+",
    type=ArgType.library,
)

argparser.add_argument(
    "-g",
    "--debug",
    action="store_true",
    help="""
        The flag to specify whether to include
        debug information in the artifacts.
        For example, it adds PDB files for windows system.

        It is disabled by default.
    """,
    default=False,
)

argparser.add_argument(
    "-v",
    "--verbose",
    action="count",
    help="""
        The flag to specify the verbosity level.
        
        It can be used multiple times to increase the verbosity level.
        For example, -v is verbose (1), -vv is more verbose (2).
        
        It is disabled (0) by default.
    """,
    default=0,
)
