from time import sleep
from cli.menu import Menus
from cli.conman import clearcon
from backend.regiman import RegiMan
from rdoclient import RandomOrgClient
from typing_extensions import LiteralString
from resources.statics import RDOVariables as rdv
from resources.statics import RegistryVariables as rv
from resources.statics import ConsoleResponses as conr

"""
TODO: STARTING @ LINE 44 [MAIN MENU OPTION 1: GENERATE PASSWORD | 2: GENERATE PIN]
TODO: STARTING @ LINE 56 [USE THE GENERATE STRING METHOD TO CREATE THE PASSWORD]
TODO: STARTING @ LING 50 [USE THE GENERATE INTEGER METHOD TO CREATE THE PIN]
"""

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
                pass_length: int = int(
                    input("Length of Password [MUST BE AT LEAST 8 CHARACTERS]: ").strip())
                pass_length = (8 - pass_length) + \
                    pass_length if pass_length < 8 else pass_length
                print(pass_length)  # TODO
                gen_string = rd.generate_strings(
                    n=1,
                    length=pass_length,
                    characters=rdv.PASSWORD_CHAR
                )
                print(f"\nResults:\n{gen_string}\n")
                input(conr._CONTINUE)
            case "2":
                # index_input: int = int(input("index: ").strip())
                # index_input = index_input + 2 if index_input == 0 else index_input + \
                #     1 if index_input == 1 else index_input
                # minimum_input: str = input("Min: ").strip()
                # maximum_input: str = input("Max: ").strip()
                # gen_ints: list = rd.generate_integers(
                #     index_input,
                #     minimum_input,
                #     maximum_input
                # )
                # print(f"\nResults:\n{gen_ints}\n")
                input(conr._CONTINUE)
            case "3": clearcon(), exit(0)
            case _: print(conr.INVALID_INPUT), sleep(1.5)
