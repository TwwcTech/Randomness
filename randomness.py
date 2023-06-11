from time import sleep
from cli.menu import Menus
from cli.conman import clearcon
from backend.regiman import RegiMan
from rdoclient import RandomOrgClient
from typing_extensions import LiteralString
from resources.statics import RegistryVariables as rv
from resources.statics import ConsoleResponses as conr

if __name__ == "__main__":
    regiman: object = RegiMan(
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
        apikey: LiteralString = regiman.enum_key()
        rd: object = RandomOrgClient(
            apikey
        )
        clearcon()
        Menus(
            title="MAIN MENU",
            dash_count=10
        ).show_main()
        menu_choice: str = input(conr.MENU_OPTIONS).strip()
        match menu_choice:
            case "1":
                index_input: int = int(input("index: ").strip())
                index_input = index_input + 2 if index_input == 0 else index_input + \
                    1 if index_input == 1 else index_input
                minimum_input: str = input("Min: ").strip()
                maximum_input: str = input("Max: ").strip()
                gen_ints: list = rd.generate_integers(
                    index_input,
                    minimum_input,
                    maximum_input
                )
                print(f"\nResults:\n{gen_ints}\n")
                input(conr._CONTINUE)
            case "2":  # TODO
                pass
            case "3":
                clearcon()
                exit(0)
            case _:
                print(conr.INVALID_INPUT)
                sleep(1.5)
