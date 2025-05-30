from sys import exit
from decor import clear


class Split:
    def __init__(self, code:str) -> None:
        self.code: str = code
        self.split_code_line: list[str] = []
        self.split_code_word: list[str] = []
        self.output: str = """"""
        self.commands: dict[int:str] ={
            0:"file",
            1:"print",
            2:"exit"
        }
        self.error: dict[str:list[int,str]] = {
            "basic":[0,f"<error>"],
            "file name = ''":[0,"<file name is not giver>"],
            "print = ''":[1,"<print has no argument>"]
        }
        
    def split_code(self) -> list[list[str]]:
        self.split_code_line = self.code.split("\n")

        split_code_word: list[str] = []
        for line in self.split_code_line:
            split_code_word = line.split(":")
            self.split_code_word.append(split_code_word)

        return self.split_code_word

    def compile_code(self) -> None:
        for key in self.split_code_word:
            try:
                if key[0] == self.commands[0]: print(f"<{key[1]}>\n") 
                elif key[0] == self.commands[1]: print(f"{key[1]}")

                if key[0] == self.commands[0] and key[1] == "": print(f"{self.error["file name = ''"]}")
                if key[0] == self.commands[1] and key[1] == "": print(self.error["print = ''"])
            except IndexError:
                print(" -------------------------------------")
                print("|an error occered during the execution|")
                print(" -------------------------------------")
                exit()

    def debug(self, data_mode) -> None:
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


if __name__ == "__main__":
    clear()

    code: str = """file:
print:veeraragavan
print:nffs"""

    compile: Split = Split(code)
    print(compile.split_code())