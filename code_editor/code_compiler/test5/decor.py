import os
from colorama import Fore, Back, Style, init
import time


init()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_exe() -> None:
    print(" -------------------- ")
    print("|WELCOM TO EXECUTABLE|")
    print(" -------------------- ")
    print("\n\nvirsion 0.1\n\n\n")

def welcome_main() -> None:
    print(" -------------------- ")
    print("|WELCOM TO EXECUTABLE|")
    print(" -------------------- ")
    print("\n\nvirsion 0.1\n\n\n")

def error() -> None:
    print(Fore.RED + " -------------------------------------" + Style.RESET_ALL)
    print(Fore.RED + "|an error occered during the execution|" + Style.RESET_ALL)
    print(Fore.RED + " -------------------------------------" + Style.RESET_ALL)
    print("")

def main_error(error_code: str) -> None:
    print(Fore.RED + f"<there is no command as [{error_code}]>" + Style.RESET_ALL)

def load_screen_reboot() -> None:
    for i in ["█","██","███","████","█████"]:
        clear()
        print(Fore.LIGHTBLACK_EX + f"rebooting[{i}]" + Style.RESET_ALL)
        time.sleep(len(i)/2)
    print(Fore.LIGHTBLACK_EX + f"rebooting succussful!" + Style.RESET_ALL)
    time.sleep(1)
    
def load_screen_load_data() -> None:
    for i in ["█","██","███","████","█████"]:
        clear()
        print(Fore.LIGHTBLACK_EX + f"rebooting[█████]" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + f"rebooting succussful!" + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + f"reloading[{i}]" + Style.RESET_ALL)
        time.sleep(len(i)/(2*2))
    print(Fore.LIGHTBLACK_EX + f"reloading succussful!" + Style.RESET_ALL)
    time.sleep(1)