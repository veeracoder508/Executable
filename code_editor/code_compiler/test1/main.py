import split

def main():
    # file_name = input("Enter the path to the text file: ")
    words = split.Code()
    words.read_and_separate_words()
    print(words)

if __name__ == "__main__":
    main()