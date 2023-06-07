import os as ops
from datetime import datetime


class SystemVaraibles:
    CURRENT_USER = ops.getlogin()
    DATE_STAMP = datetime.today().date()
    TIME_STAMP = datetime.today().time()


class RegistryVariables:
    HKEY = "Software"
    APPNAME = "Randomness"
