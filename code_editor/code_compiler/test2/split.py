class SplitFile:
    """
        it is a class to convert the file into a readable 
        form for python
        
        
        **Arguments:**
            *file_path[str]* file path to the txt file that
            is to be compiled
        
        **Returns:**
            *None*   
        """
    def __init__(self, file_path: str = "test2/test.txt"):
        self.file_path: str = file_path    # file path
        self.lines: list[str] = []         # each line in the file
        self.words: list[list[str]] = [[]] # each word in a line

    def split_file(self):
        """
        it splits the file into each line in an list


        **Arguments:**
            *None*

        **Returns:**
            pass
        """
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    content = file.read()
                    lines = content.split(";")  # Split the content into a list of lines  
                    self.lines.append(lines) 
                return self.lines
        except FileNotFoundError:
            return f"Error: File not found at '{self.file_path}'"
        except Exception as e:
            return f"An error occurred: {e}"
        

if __name__ == "__main__":
    code = SplitFile()
    print(code.split_file())