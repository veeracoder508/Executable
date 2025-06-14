## test4
this is the the first stage of executable.
### split.py
in class `Code()` there are
```python
__init__(self, file_path = "test.txt")
split_file(self)
compile_code(self)
debug(self, data_mode()
```
the `__init__()` gets the """
the `split_file()` splits the code that python can understand.

the `compile_code()` compiles the splited code.

### main_screen.py
in the class `HomeScreenPanal()` there are
```python
__init__(self)
executaqble(self)
display(self)
```
the `__init__()` gets nothing.

the `executable()` compiles the code and compiles to use it in `display()`

the `display()` is used for tha IO for the terminal

commands:
|command|discription|
|:---|---:|
|exe|to open the code editor|
|run|to run a program fron database|
|exit|to exit the terminal|
|help|to list all the command|
|list|to list all the data in database|
|remove|to delete the last program in the database|
|clear|to delete all the data in the database|
|cls|to clear the screen|
|reboot|to reboot the program|

### files.py
in the class `Filemanager()` there are
```python
__init__(self)
add(self, split_code)
delete(self, file_index = -1)
display(self) # not used
clear(self)
disp(self)
run(self, program_index)
```
the `__init__()` gets nothing.

the `add()` is used t store the data in `split_code` and store it in the database.

the `delete()` is used to delete the last data in the database.

the `disp()` is used to display the data in the database on the terminal.

the `clear()` is used to clear all the data in the database.

the `run()` is used to run a spicific program in the database.

### decor.py
```python
clear()
welcome_exe()
welcome_main()
error()
main_error()
```
the `clear()` is used to clear the terminal.

the `welcome_exe()` is used to display the welcome screen for the program screen.

the `welcome_main()` is used to display the welcome screen for the main terminal.

the `error()` is used to display an error screen and force stop the program if an unexpeted error occors.

the `main_error()` is used to display that the command entered in the terminal is not a valid command.

### code_screen.py
```python
__init__(self)
ask()
display()
```
the `ask()` is used to get the code from the code editor.

the `display()` is used to display the output of the program. 
### jason_.py
in the class `JsonFileManager()` we have
```python
__init__(self, file_path)
convert_to_dict(file) # not used
_ensure_directory_exits(self) # used only in the class
write_data(self, data)
read_data(self)
```
the `write_data()` is used to write all the data to a json file 'support.json'.

the `read_data()` is used to read data from the json file 'support.json'.
