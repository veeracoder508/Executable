from decor import *
from code_screen import *
from files import *

import time
from colorama import Fore, Back, Style, init


init()
class HomeScreenPlan:
    def __init__(self) -> None:
        self.commands: dict[int:str] = {
            0:"exe",
            1:"run",
            2:"& C:/Users/Admin/AppData/Local/Programs/Python/Python313/python.exe \
                c:/Users/Admin/Desktop/vscode_projects/code_compiler/test4/main.py",
            3:"exit",
            4:"help",
            5:"list",
            6:"remove",
            7:"clear",
            8:"cls",
            9:"reboot"
        }
        self.files: FileManager = FileManager()

        clear()
        welcome_main()

    def executable(self) -> None:
        compile_code: Executeble = Executeble()
        compile_code.ask()
        compile_code.display()

        split_code: Split = Split(compile_code.code)
        self.files.add(split_code.split_code())

    def display(self) -> None:
        try:
            while True:
                code = input("-->")
                if code == self.commands[0]: self.executable()
                elif code == self.commands[1]: 
                    self.files.run(int(input("  -->")))
                elif code == self.commands[2]: os.system(self.commands[2])
                elif code == self.commands[3]: 
                    print("<exit from program>")
                    exit()
                elif code == self.commands[4]: print(self.commands)
        
                elif code == self.commands[5]:
                    try:
                        self.files.disp()
                    except TypeError:
                        error()
                        exit()
                elif code == self.commands[6]: 
                    self.files.delete(int(input("  -->")))
                elif code == self.commands[7]: self.files.files.clear()
                elif code == self.commands[8]: clear()
                elif code == self.commands[9]:
                    self.files.upload_to_file()
                    for i in [".","..","...","....","....."]:
                        print(Fore.LIGHTBLACK_EX + f"rebooting system{i}" + Style.RESET_ALL)
                        time.sleep(len(i)/2)
                    print(Fore.LIGHTBLACK_EX + "reboot succussful!" + Style.RESET_ALL)
                    time.sleep(1)
                    screen: HomeScreenPlan = HomeScreenPlan()
                    screen.display()
                    self.files.upload_from_file()
                else: main_error(code)
        except KeyboardInterrupt:
            print(Fore.RED + "\n<you have force stoped the program>" + Style.RESET_ALL)
            exit()
