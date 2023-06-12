from time import sleep
from cli.menu import Menus
from cli.conman import clearcon
from backend.regiman import RegiMan
from rdoclient import RandomOrgClient
from typing_extensions import LiteralString
from resources.statics import RDOVariables as rdv
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
    regstatus: bool = regiman.status_check(regiman.enum_regapps())
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
                gen_pass = rd.generate_strings(
                    n=1,
                    length=pass_length,
                    characters=rdv.PASSWORD_CHAR
                )
                print(f"\nResults:\n{gen_pass}\n")
                input(conr._CONTINUE)
            case "2":
                while True:
                    clearcon()
                    Menus(
                        title="PIN GENERATOR",
                        dash_count=10
                    ).show_pin_submenu()
                    pinmenu_input = input(conr.MENU_OPTIONS)
                    match pinmenu_input:
                        case "1":
                            gen_pin = rd.generate_strings(
                                n=1,
                                length=4,
                                characters=rdv.PIN_CHAR
                            )
                            print(f"\nResults:\n{gen_pin}\n")
                            input(conr._CONTINUE)
                        case "2":
                            gen_secure_pin = rd.generate_strings(
                                n=1,
                                length=6,
                                characters=rdv.COMPLEX_PIN_CHAR
                            )
                            print(f"\nResults:\n{gen_secure_pin}\n")
                            input(conr._CONTINUE)
                        case "3": break
                        case _: print(conr.INVALID_INPUT), sleep(1.5)
            case "3": clearcon(), exit(0)
            case _: print(conr.INVALID_INPUT), sleep(1.5)
