from typing import Literal

class ArgType:
    @staticmethod
    def machine(arg: str) -> Literal["aarch64", "i686", "x86_64"]:
        from re2 import match

        if match(r"^(?:arm(?:v8|v9|64)|aarch64)\w*$", arg):
            return "aarch64"
        elif match(r"^(?:(?:i[3-6]|x)86)$", arg):
            return "i686"
        elif match(r"^(?:(?:amd|x(?:86_)?)64)$", arg):
            return "x86_64"
        else:
            raise ValueError(f"Unsupported machine type: {arg}")

    @staticmethod
    def system(arg: str) -> Literal["linux", "macos", "windows"]:
        result = arg.lower()

        if result.startswith("cygwin"):
            result = "windows"  
        elif result.startswith("darwin"):
            result = "macos"
        elif result.startswith("linux"):
            result = "linux"
        elif result.startswith("mac"):
            result = "macos"
        elif result.startswith("mingw"):
            result = "windows"
        elif result.startswith("ms"):
            result = "windows"
        elif result.startswith("nt"):
            result = "windows"
        elif result.startswith("win"):
            result = "windows"
        else:
            raise ValueError(f"Unsupported system name: {arg}")

        return result
