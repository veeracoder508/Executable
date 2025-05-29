from split import Split
from decor import *
import json


init()
class FileManager:
    def __init__(self) -> None:
        self.files: list[list[list[str,str]]] = []
        self.old_files: list[list[list[str,str]]] = []
        self.new_files: list[list[list[str,str]]] = []
        self.json: dict[int:list[list[str,str]]] = {}
        self.filename: str = "sopport.txt"

    def add(self, split_code: list[list[str,str]]) -> None:
        self.files.append(split_code)
        self.files.sort()

    def delete(self, file_index: int = -1) -> None:
        self.files.pop(file_index)

    def display(self) -> None:
        for program in self.files:
            print(program)

    def clear(self) -> None:
        self.files.clear()

    def disp(self) -> None:
        for program_index, program in enumerate(self.files):
            print(f"{program_index}: {program}")

    def run(self, program_index: int) -> None:
        try:
            code:list[list[str,str]] = self.files[program_index]
            com: Split = Split("")
            com.split_code_word = code
            com.compile_code()
        except IndexError:
            print(Fore.RED + f"\n<there is no file of index {program_index}>" + Style.RESET_ALL)

    def upload_to_file(self) -> None:
        try:
            with open(self.filename, "a") as file:
                for program in self.files:
                        file.write(f"{program}\n\n")

        except IOError as e:
            print(Fore.RED + f"<error writing to file [{e}]>" + Style.RESET_ALL)

    def upload_from_file(self) -> None:
        try:
            with open(self.filename, "r") as file:
                for program in list(file):
                    self.files.append(program)
        except IOError as e:
            print(Fore.RED + f"<error retriving from file [{e}]>" + Style.RESET_ALL)