from split import Split
from decor import *


init()
class Executeble:
    def __init__(self) -> None:
        self.code: str = """"""
        self.split_code: list[list[str]] 
        self.code_line_index = 0

        welcome_exe()

    def ask(self) -> None:
        exit_code: bool = False

        while not exit_code:
            try:
                self.code_line_index += 1
                code = input(f"{self.code_line_index}>")
                if code == "exit": exit_code = not exit_code
                self.code += code + "\n"
            except KeyboardInterrupt:
                print(Fore.CYAN + "\n<you have force stoped the compiler>" + Style.RESET_ALL)
                exit_code = not exit_code

    def display(self) -> None:
        self.split_code: Split = Split(self.code)  
        self.split_code.split_code().pop(-1)
        self.split_code.compile_code()


if __name__ == "__main__":
    clear()

    compile: Executeble = Executeble()
    compile.ask()
    compile.display()
                