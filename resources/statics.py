import os as ops
from datetime import datetime
from typing_extensions import LiteralString


class SystemVaraibles:
    CURRENT_USER: LiteralString = ops.getlogin()
    DATE_STAMP: LiteralString = datetime.today().date()
    TIME_STAMP: LiteralString = datetime.today().time()


class RegistryVariables:
    HKEY: LiteralString = "Software"
    APPNAME: LiteralString = "Randomness"

class ConsoleResponses:
    INVALID_INPUT: str = "\nNot a valid option. Please select a menu option [1-3]\n"

class ExceptionNotes:
    ENUM_APPS_ERROR = "ERROR: Unable to enumerate apps in the regkey [Line: 22 | File: 'regiman.py']"
    CREATE_KEY_ERROR = "ERROR: Unable to create the registry key [Line: 44 | File: 'regiman.py']"
    ENUM_REGKEY_ERROR = "ERROR: Unable to enumerate the regkey [Line: 62 | File: 'regiman.py']"
