import winreg
from typing_extensions import LiteralString


class RegiMan():
    def __init__(self, hkeytype: LiteralString, software_folder: LiteralString) -> None:
        self.hkeytype = hkeytype
        self.software_folder = software_folder

    def enum_regapps(self) -> list:  # TODO
        pass

    def status_check(self, apps: list) -> bool:  # TODO
        pass

    def create_key(self, apikey: LiteralString):  # TODO
        pass

    def enum_key(self) -> LiteralString:
        pass
