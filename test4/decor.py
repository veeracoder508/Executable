import os
from colorama import Fore, Back, Style, init

init()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_exe():
    print(" -------------------- ")
    print("|WELCOM TO EXECUTABLE|")
    print(" -------------------- ")
    print("\n\nvirsion 0.1\n\n\n")

def welcome_main():
    print(" -------------------- ")
    print("|WELCOM TO EXECUTABLE|")
    print(" -------------------- ")
    print("\n\nvirsion 0.1\n\n\n")

def error():
    print(Fore.RED + " -------------------------------------" + Style.RESET_ALL)
    print(Fore.RED + "|an error occered during the execution|" + Style.RESET_ALL)
    print(Fore.RED + " -------------------------------------" + Style.RESET_ALL)
    print("")

def main_error(error_code):
    print(Fore.RED + f"<there is no command as [{error_code}]>" + Style.RESET_ALL)