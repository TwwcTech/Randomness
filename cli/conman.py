import os as ops


def clearcon(): ops.system("cls") if ops.name == "nt" else ops.system("clear")


def menu_padder(func):
    def wrapper(*args, **kwargs):
        print("\n")
        func(*args, **kwargs)
        print("\n")
    return wrapper
