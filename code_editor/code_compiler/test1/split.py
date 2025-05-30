class Code:
    def __init__(self,file_path = "test.txt", dev = True):
        self.file_path = file_path
        self.dev = dev
        self.code = []
        self.code1 = []
    
    def read_and_separate_words(self):
        """
        Reads a text file, separates words, and prints them to the console
        separated by semicolons.

        Args:
            file_path (str): The path to the text file to be read.
        """
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    content = file.read()
                    self.words = content.split(";")  # Split the content into a list of words
        except FileNotFoundError:
            return f"Error: File not found at '{self.file_path}'"
        except Exception as e:
            return f"An error occurred: {e}"

    def compile(self):
        c = ["list"]
        for word_number,word in enumerate(self.words):
            print("------")
            for pice_number,pice in enumerate(word.split(":")):
                if self.dev:
                    print(f"pos:({word_number},{pice_number})\nval:{pice}")
                self.code1 = self.code[word_number].append(pice)
                return self.code1[pice_number].append(pice)

    # all dounder methodes in the class
    def __str__(self):
        """
        Returns a string representation of the object, which is a list of words
        separated by semicolons.

        Returns:
            str: A string representation of the object.
        """
        for word in self.words:
            return ";".join(self.words)
        
    def __repr__(self):
        """
        Returns a string representation of the object for debugging purposes.

        Returns:
            str: A string representation of the object.
        """
        return f"Code(file_path='{self.file_path}', words={self.words})"


if __name__ == "__main__":
    # file_name = input("Enter the path to the text file: ")
    words = Code(dev=False)
    print(words.read_and_separate_words())
    print(f'"\n\n\n"{words.compile()}')