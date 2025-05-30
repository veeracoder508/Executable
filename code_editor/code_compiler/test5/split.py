from sys import exit
from decor import *


class Split:
    """
    class to split and compile code
    """
    def __init__(self, code:str) -> None:
        """
        Agrs:
        code (str): the code that is to be compiled
        self.code: str = code
        """
        self.code = code
        self.split_code_line: list[str] = []
        self.split_code_word: list[str] = []
        self.output: str = """"""
        self.commands: dict[int:str] ={
            0:"file",
            1:"print",
            2:"exit",
            3:"help"
        }
        self.error: dict[str:list[int,str]] = {
            "basic":[0,f"<error>"],
            "file name = ''":[0,"<file name is not giver>"],
            "file > 1":[1,"<there is more than one file name>"],
            "print = ''":[0,"<print has no argument>"]
        }
        
    def split_code(self) -> list[list[str]]:
        """
        a method to split the code that python can understand
        """
        self.split_code_line = self.code.split("\n")

        split_code_word: list[str] = []
        for line in self.split_code_line:
            split_code_word = line.split(":")
            self.split_code_word.append(split_code_word)

        return self.split_code_word

    def compile_code(self) -> None:
        """
        the method to compile the split code
        """
        num_of_file: int = 0
        for key in self.split_code_word:
            try:
                if key[0] == self.commands[0]: 
                    print(f"<{key[1]}>\n")
                    num_of_file += 1
                elif key[0] == self.commands[1]: print(f"{key[1]}")
                elif key[0] == self.commands[3]: print(self.commands)

                if key[0] == self.commands[0] and key[1] == "": print(self.error["file name = ''"])
                if key[0] == self.commands[1] and key[1] == "": print(self.error["print = ''"])
                if key[0] == self.commands[1] and num_of_file > 1: print(self.error["file > 1"])
            except IndexError:
                error()
                exit()

    def debug(self, data_mode) -> None:
        """
        a method to see that the compiler is working
        Args:
            date_mode (str): the type of data to be seen
        """
        self.split_code()
        if data_mode == "print data":
            print("\n")
            print(f"code:\n{self.code}\n")
            print(f"split_code_line:\n{self.split_code_line}\n")
            print(f"split_code_word:\n{self.split_code_word}\n")
            print(f"output:\n{self.compile_code()}\n")
        elif data_mode == "print code":
            print("\n")
            print(f"code:\n{self.code}\n")
        elif data_mode == "print split_code_line":
            print("\n")
            print(f"split_code_line:\n{self.split_code_line}\n")
        elif data_mode == "print split_code_word":
            print("\n")
            print(f"code:\n{self.split_code_word}\n")
        elif data_mode == "print output":
            print("\n")
            print(f"split_code_line:\n{self.compile_code()}\n")
        else:
            print("data_mode is not given")
