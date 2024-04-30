from __future__ import annotations

from package.argument import ArgType

def test_machine_matching():
    def machine_wrapped(value: str) -> str | None:
        try:
            return ArgType.machine(value)
        except ValueError:
            return None
    # References:
    # 1. https://stackoverflow.com/a/45125525
    # 2. https://en.wikipedia.org/wiki/Uname

    # It's not aarch64 compatible
    assert machine_wrapped("arm") == None
    assert machine_wrapped("armv7") == None
    assert machine_wrapped("aarch") == None
    assert machine_wrapped("aarchv7") == None
    assert machine_wrapped("aarchv8") == None
    assert machine_wrapped("aarchv9") == None

    # It's aarch64 compatible
    assert machine_wrapped("arm64") == "aarch64"
    assert machine_wrapped("armv8b") == "aarch64"
    assert machine_wrapped("armv8l") == "aarch64"
    assert machine_wrapped("aarch64") == "aarch64"
    assert machine_wrapped("aarch64_be") == "aarch64"

    # It's not i686 compatible
    assert machine_wrapped("i86") == None
    assert machine_wrapped("ix86") == None
    assert machine_wrapped("i086") == None
    assert machine_wrapped("i286") == None
    assert machine_wrapped("i786") == None
    assert machine_wrapped("x386") == None
    assert machine_wrapped("x686") == None
    assert machine_wrapped("80386") == None

    # It's i686 compatible
    assert machine_wrapped("i386") == "i686"
    assert machine_wrapped("i486") == "i686"
    assert machine_wrapped("i586") == "i686"
    assert machine_wrapped("i686") == "i686"
    assert machine_wrapped("x86") == "i686"

    # It's not x86_64 compatible
    assert machine_wrapped("amd") == None
    assert machine_wrapped("amd_64") == None
    assert machine_wrapped("ix86_64") == None

    # It's x86_64 compatible
    assert machine_wrapped("amd64") == "x86_64"
    assert machine_wrapped("x86_64") == "x86_64"
    assert machine_wrapped("x64") == "x86_64"

def test_system_matching():
    def system_wrapped(value: str) -> str | None:
        try:
            return ArgType.system(value)
        except ValueError:
            return None

    # It's not linux compatible
    assert system_wrapped("l") == None
    assert system_wrapped("aix") == None
    assert system_wrapped("bsd") == None
    assert system_wrapped("gnu") == None
    assert system_wrapped("linus") == None
    assert system_wrapped("manylinux") == None
    assert system_wrapped("sunos") == None
    assert system_wrapped("Ubuntu") == None
    assert system_wrapped("unix") == None
    assert system_wrapped("wsl") == None

    # It's linux compatible
    assert system_wrapped("linux") == "linux"
    assert system_wrapped("Linux") == "linux"
    assert system_wrapped("linux2") == "linux"

    # It's not macos compatible
    assert system_wrapped("d") == None
    assert system_wrapped("m") == None
    assert system_wrapped("Mc") == None
    assert system_wrapped("osx") == None
    assert system_wrapped("OS X") == None

    # It's macos compatible
    assert system_wrapped("darwin") == "macos"
    assert system_wrapped("Darwin") == "macos"
    assert system_wrapped("mac") == "macos"
    assert system_wrapped("Mac") == "macos"
    assert system_wrapped("MAC") == "macos"
    assert system_wrapped("macos") == "macos"
    assert system_wrapped("MacOS") == "macos"
    assert system_wrapped("macOS") == "macos"
    assert system_wrapped("macOSX") == "macos"
    assert system_wrapped("MacOS X") == "macos"
    assert system_wrapped("Mac OS X") == "macos"
    assert system_wrapped("Macintosh") == "macos"
    
    # It's not windows compatible
    assert system_wrapped("w") == None
    assert system_wrapped("min") == None
    assert system_wrapped("won") == None
    assert system_wrapped("wondins") == None
    assert system_wrapped("wimdoms") == None
    
    # It's windows compatible
    assert system_wrapped("cygwin") == "windows"
    assert system_wrapped("Cygwin") == "windows"
    assert system_wrapped("mingw") == "windows"
    assert system_wrapped("MinGW") == "windows"
    assert system_wrapped("MSYS") == "windows"
    assert system_wrapped("ms") == "windows"
    assert system_wrapped("nt") == "windows"
    assert system_wrapped("NT") == "windows"
    assert system_wrapped("win") == "windows"
    assert system_wrapped("WIN") == "windows"
    assert system_wrapped("win32") == "windows"
    assert system_wrapped("win64") == "windows"
    assert system_wrapped("WinXP") == "windows"
    assert system_wrapped("win7") == "windows"
    assert system_wrapped("win8") == "windows"
    assert system_wrapped("win10") == "windows"
    assert system_wrapped("Windows") == "windows"
    assert system_wrapped("windows") == "windows"
    assert system_wrapped("WindowsNT") == "windows"
