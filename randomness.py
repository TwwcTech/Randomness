from time import sleep
from cli.menu import Menus
from cli.conman import clearcon
from backend.regiman import RegiMan
from typing_extensions import LiteralString
from resources.statics import RegistryVariables as rv

"""
TODO: COMPLETE THE 'REGIMAN' CLASS
"""

if __name__ == "__main__":
    regiman = RegiMan(
        hkeytype=rv.HKEY,
        software_folder=rv.APPNAME
    )
    regapps = regiman.enum_regapps()
    regstatus: bool = regiman.status_check(
        apps=regapps
    )
    print(regapps)
    print(regstatus)
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
                print(
                    "\nNot a valid option. Please select a menu option [1-3]\n"
                )
                sleep(1.5)
