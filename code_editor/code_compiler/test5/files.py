from split import Split
from decor import *
import json_


init()
class FileManager:
    """
    the class for the class manager for the terminal
    """
    def __init__(self) -> None:
        self.files: list[list[list[str,str]]] = []
        self.filename: str = "support.json"

    def add(self, split_code: list[list[str,str]]) -> None:
        """
        the method to add a file to the database
        
        Args:
            split_code (list[list[str,str]]): the code that is to be appended
        """
        self.files.append(split_code)
        self.files.sort()

    def delete(self, file_index: int = -1) -> None:
        """
        the method to delete the last file in the database
        
        Args:
            file_index (int): the index of the file (-1)
        """
        self.files.pop(file_index)

    def display(self) -> None:
        """
        the method to list the data in the database
        """
        for program in self.files:
            print(program)

    def clear(self) -> None:
        """
        the method to clear the database
        """
        self.files.clear()

    def disp(self) -> None:
        """
        the method to list the data in the database
        """
        for program_index, program in enumerate(self.files):
            print(f"{program_index}: {program}")

    def run(self, program_index: int) -> None:
        """
        the method to run a file in the database
        """
        try:
            code:list[list[str,str]] = self.files[program_index]
            com: Split = Split("")
            com.split_code_word = code
            com.compile_code()
        except IndexError:
            print(Fore.RED + f"\n<there is no file of index {program_index}>" + Style.RESET_ALL)

    def open(self, mode: str) -> None:
        if mode == "WRITE":
            json_.JsonFileManager(self.filename).write_data(self.files)
        elif mode == "READ":
            self.files = json_.JsonFileManager(self.filename).read_data()