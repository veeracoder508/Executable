import json
import os

class JsonFileManager:
    """
    A class to manage reading from and writing to JSON files.
    """

    def __init__(self, file_path):
        """
        Initializes the JsonFileManager with the path to the JSON file.

        Args:
            file_path (str): The full path to the JSON file (e.g., 'data/config.json').
        """
        if not isinstance(file_path, str) or not file_path:
            raise ValueError("file_path must be a non-empty string.")
        self.file_path = file_path
        self._ensure_directory_exists()

    def convert_to_dict(file: list[list[list[str,str]]]) -> None:
        dict_form: dict[str:list[list[str,str]]] = {}
        for program_index, program in enumerate(file):
            dict_form[f"{program_index}"] = program
        return dict_form

    def _ensure_directory_exists(self):
        """
        Ensures that the directory for the file_path exists.
        Creates it if it doesn't.
        """
        directory = os.path.dirname(self.file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

    def write_data(self, data: dict|list, indent=4):
        """
        Writes data (dictionary or list) to the JSON file.
        If the file exists, it will be overwritten.

        Args:
            data (dict or list): The Python data structure to write.
            indent (int, optional): The indentation level for pretty-printing JSON.
                                    Defaults to 4. Set to None for no indentation.

        Returns:
            bool: True if data was written successfully, False otherwise.
        """
        try:
            with open(self.file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=indent, ensure_ascii=False)
            print(f"Data successfully written to '{self.file_path}'")
            return True
        except TypeError as e:
            print(f"Error: Data is not JSON serializable. {e}")
            return False
        except IOError as e:
            print(f"Error writing to file '{self.file_path}': {e}")
            return False
        except Exception as e:
            print(f"An unexpected error occurred while writing: {e}")
            return False

    def read_data(self):
        """
        Reads data from the JSON file.

        Returns:
            dict or list: The data read from the JSON file. Returns an empty dict
                          if the file is empty or contains malformed JSON,
                          or None if the file doesn't exist or other I/O errors occur.
        """
        if not os.path.exists(self.file_path):
            print(f"Warning: File '{self.file_path}' does not exist. Returning None.")
            return None # Or raise FileNotFoundError depending on desired behavior

        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                # Handle empty file case
                content = f.read().strip()
                if not content:
                    print(f"Warning: File '{self.file_path}' is empty. Returning empty list.")
                    return []
                return json.loads(content) # Use loads if reading from string content directly
        except json.JSONDecodeError as e:
            print(f"Error: Could not decode JSON from '{self.file_path}'. File might be corrupted or malformed. {e}")
            return {} # Or raise an error
        except IOError as e:
            print(f"Error reading from file '{self.file_path}': {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred while reading: {e}")
            return None

    def get_file_path(self):
        """
        Returns the file path associated with this manager.
        """
        return self.file_path


if __name__ == "__main__":
    manager: JsonFileManager = JsonFileManager("support.json")
    for program in manager.read_data():
        print(program)