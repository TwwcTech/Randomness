import re
import winreg
from typing_extensions import LiteralString
from resources.statics import SystemVaraibles as sv


class RegiMan():
    def __init__(self, hkeytype: LiteralString, software_folder: LiteralString) -> None:
        self.hkeytype = hkeytype
        self.software_folder = software_folder
        self.datestamp = sv.DATE_STAMP
        self.access_reg = winreg.ConnectRegistry(
            None,
            winreg.HKEY_CURRENT_USER
        )
        self.regsoft = winreg.OpenKey(
            self.access_reg,
            f"{self.hkeytype}"
        )

    def enum_regapps(self) -> list:
        try:
            appnames = []
            for softwarefolders in range(35):
                appnames.append(
                    winreg.EnumKey(
                        self.regsoft,
                        softwarefolders
                    )
                )
            return appnames
        except Exception as ex:
            ex.add_note()  # TODO
            raise Exception(ex)

    def status_check(self, apps: list) -> bool:
        return True if re.search(
            r"\b{}\b".format(
                self.software_folder
            ), str(apps)
        ) else False

    def create_key(self, apikey: LiteralString):
        try:
            appname_key = winreg.CreateKey(
                self.regsoft,
                self.software_folder
            )
            winreg.SetValueEx(
                appname_key, "Init DateTime", 0,
                winreg.REG_SZ, f"{sv.DATE_STAMP} {sv.TIME_STAMP}"
            )
            winreg.SetValueEx(
                appname_key, "APIKEY", 0,
                winreg.REG_SZ, apikey
            )
        except Exception as ex:
            ex.add_note()  # TODO
            raise Exception(ex)

    def enum_key(self) -> LiteralString:
        try:
            appname_key = winreg.OpenKey(
                self.regsoft,
                self.software_folder
            )
            api_key = winreg.QueryValueEx(
                appname_key,
                "APIKEY"
            )
            key, _ = api_key
            return key
        except Exception as ex:
            ex.add_note()  # TODO
            raise Exception(ex)
