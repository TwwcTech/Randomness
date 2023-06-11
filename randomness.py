from time import sleep
from cli.menu import Menus
from cli.conman import clearcon
from backend.regiman import RegiMan
from typing_extensions import LiteralString
from resources.statics import RegistryVariables as rv
from resources.statics import ConsoleResponses as conr

"""
TODO: CREATE NEW FILE TO PROCESS THE API CALLS [BACKEND]
"""

if __name__ == "__main__":
    regiman = RegiMan(
        hkeytype=rv.HKEY,
        software_folder=rv.APPNAME
    )
    regapps: list = regiman.enum_regapps()
    regstatus: bool = regiman.status_check(
        apps=regapps
    )
    match regstatus:
        case False:
            clearcon()
            apikey_input: LiteralString = input("API key: ").strip()
            regiman.create_key(
                apikey=apikey_input
            )
    while regstatus is True:
        clearcon()
        Menus(
            title="MAIN MENU",
            dash_count=10
        ).show_main()
        menu_choice: str = input("Select a menu option: ").strip()
        match menu_choice:
            case "1":  # TODO
                pass
            case "2":  # TODO
                pass
            case "3":
                clearcon()
                exit(0)
            case _:
                print(conr.INVALID_INPUT)
                sleep(1.5)
