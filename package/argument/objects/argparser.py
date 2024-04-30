from argparse import ArgumentParser
from platform import machine, system

from .argtype import ArgType

argparser = ArgumentParser()

argparser.add_argument(
    "-m",
    "--machine",
    metavar="Machine_Type",
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
    metavar="System_Name",
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
    "-g",
    "--debug",
    action="store_true",
    help="Include debug information in the artifacts.",
    default=False,
)
