import winreg
from typing_extensions import LiteralString


class WinReg():
    def __init__(self, hkeytype: LiteralString, software_folder: LiteralString) -> None:
        self.hkeytype = hkeytype
        self.software_folder = software_folder

    def status_check(self) -> bool:  # TODO
        pass

    def enum_key(self) -> list:  # TODO
        pass

    def create_key(self):  # TODO
        pass
