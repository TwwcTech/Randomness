from time import sleep
from cli.menu import Menus
from cli.conman import clearcon
from backend.regiman import RegiMan
from backend.rdoc import RDOProcessor
from typing_extensions import LiteralString
from resources.statics import RegistryVariables as rv
from resources.statics import ConsoleResponses as conr

"""
TODO: FIGURE OUT WHY WHEN CALLING THE API IT RETURNS 'NONE' [BIG PROBLEM] -> LINE: 38 | 'RANDOMNESS.PY' || LINE: 7 | 'RDOC.PY'
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
        menu_choice: str = input(conr.MENU_OPTIONS).strip()
        match menu_choice:
            case "1":
                # TODO: FIX THIS [NOTHING IS POPULATING WHEN INPUTTING CORRECT REQUESTS - WAS WORKING BEFORE (NOTHING HAS CHANGED)]
                apikey = regiman.enum_key()
                print(f"API Key: {apikey}")
                rdoc = RDOProcessor(
                    apikey
                )
                index_input = input("index: ").strip()
                minimum_input = input("Min: ").strip()
                maximum_input = input("Max: ").strip()
                gen_ints = rdoc.generate_ints(
                    index_input,
                    minimum_input,
                    maximum_input
                )
                print(gen_ints)
                input(conr._CONTINUE)
            case "2":  # TODO
                pass
            case "3":
                clearcon()
                exit(0)
            case _:
                print(conr.INVALID_INPUT)
                sleep(1.5)
