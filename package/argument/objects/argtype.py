from typing import Literal

class ArgType:
    @staticmethod
    def library(arg: str) -> Literal["dynamic", "static"]:
        result = arg.lower()
        
        if result == "dynamic" or result == "d" or result == "shared":
            result = "dynamic"
        elif result == "static" or result == "s" or result == "archived":
            result = "static"
        else:
            raise ValueError(f"Unsupported library type: {arg}")

        return result

    @staticmethod
    def machine(arg: str) -> Literal["aarch64", "i686", "x86_64"]:
        from re2 import match

        if match(r"(?:arm(?:v8|v9|64)|aarch64)\w*$", arg):
            return "aarch64"
        elif match(r"(?:(?:i[3-6]|x)86)$", arg):
            return "i686"
        elif match(r"(?:(?:amd|x(?:86_)?)64)$", arg):
            return "x86_64"
        else:
            raise ValueError(f"Unsupported machine type: {arg}")

    @staticmethod
    def system(arg: str) -> Literal["linux", "macos", "windows"]:
        result = arg.lower()

        if result.startswith(("linux",)):
            result = "linux"
        elif result.startswith(("darwin", "mac")):
            result = "macos"
        elif result.startswith(("win", "nt", "mingw", "ms", "cygwin")):
            result = "windows"
        else:
            raise ValueError(f"Unsupported system name: {arg}")

        return result
