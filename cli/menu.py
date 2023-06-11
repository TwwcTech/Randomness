from cli.conman import menu_padder


class Menus():
    def __init__(self, title: str, dash_count: int) -> None:
        self.title = title
        self.dash_count = dash_count

    @menu_padder
    def show_main(self):
        menu_options: dict = {
            "1": "Random Password",
            "2": "Random Passphrase",
            "3": "Exit"
        }
        print(f"{'-'*self.dash_count} {self.title} {'-'*self.dash_count}")
        for num, options in menu_options.items():
            print(f"{num} - {options}")
