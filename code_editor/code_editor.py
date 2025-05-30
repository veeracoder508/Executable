import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, simpledialog
import subprocess
import os

class PythonCodeEditor:
    def __init__(self, master):
        self.master = master
        master.title("PyEditor")
        master.geometry("1000x700")

        self.current_file_path = None

        # --- Menu Bar ---
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        # File Menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open...", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=master.quit)

        # Edit Menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Undo", command=self.undo_text)
        self.edit_menu.add_command(label="Redo", command=self.redo_text)

        # Run Menu
        self.run_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Run", menu=self.run_menu)
        self.run_menu.add_command(label="Run Code", command=self.run_code)

        # --- Code Editor Frame ---
        self.editor_frame = tk.Frame(master)
        self.editor_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Line Numbers (left side)
        self.line_numbers = tk.Text(self.editor_frame, width=4, padx=3, pady=3, bd=0,
                                    bg="#282c34", fg="#abb2bf", state="disabled")
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        # Code Editor (main text area)
        self.code_text = scrolledtext.ScrolledText(self.editor_frame, wrap=tk.WORD, undo=True,
                                                   bg="#282c34", fg="#abb2bf",
                                                   insertbackground="#abb2bf", selectbackground="#3e4451",
                                                   font=("Consolas", 12))
        self.code_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar for line numbers to sync with code_text
        self.code_text.vbar.config(command=self.sync_scroll)
        self.line_numbers.vbar.config(command=self.code_text.yview)

        # --- Output Console ---
        self.output_frame = tk.LabelFrame(master, text="Output", padx=5, pady=5)
        self.output_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.output_text = scrolledtext.ScrolledText(self.output_frame, wrap=tk.WORD,
                                                     bg="#282c34", fg="#abb2bf",
                                                     insertbackground="#abb2bf", state="disabled",
                                                     font=("Consolas", 10))
        self.output_text.pack(fill=tk.BOTH, expand=True)

        # --- Status Bar ---
        self.status_bar = tk.Label(master, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # --- Event Bindings ---
        self.code_text.bind("<KeyRelease>", self.update_line_numbers_and_highlight)
        self.code_text.bind("<MouseWheel>", self.sync_scroll_mouse)
        self.code_text.bind("<Button-4>", self.sync_scroll_mouse) # For Linux
        self.code_text.bind("<Button-5>", self.sync_scroll_mouse) # For Linux
        self.master.bind("<Control-s>", self.save_file)
        self.master.bind("<Control-o>", self.open_file)
        self.master.bind("<Control-n>", self.new_file)
        self.master.bind("<F5>", self.run_code)

        # --- Syntax Highlighting Configuration ---
        self.setup_syntax_highlighting()
        self.update_line_numbers_and_highlight() # Initial update

    def setup_syntax_highlighting(self):
        # Define tags for different syntax elements
        self.code_text.tag_configure("keyword", foreground="#c678dd")  # Purple
        self.code_text.tag_configure("string", foreground="#98c379")   # Green
        self.code_text.tag_configure("comment", foreground="#5c6370")  # Grey
        self.code_text.tag_configure("builtin", foreground="#e6c07b")  # Yellow/Orange
        self.code_text.tag_configure("definition", foreground="#61afef") # Blue
        self.code_text.tag_configure("number", foreground="#d19a66") # Orange

        # Python keywords
        self.keywords = ["False", "None", "True", "and", "as", "assert", "async", "await",
                         "break", "class", "continue", "def", "del", "elif", "else",
                         "except", "finally", "for", "from", "global", "if", "import",
                         "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise",
                         "return", "try", "while", "with", "yield"]

        # Built-in functions/types
        self.builtins = ["abs", "all", "any", "ascii", "bin", "bool", "bytearray", "bytes",
                         "callable", "chr", "classmethod", "compile", "complex", "delattr",
                         "dict", "dir", "divmod", "enumerate", "eval", "exec", "filter",
                         "float", "format", "frozenset", "getattr", "globals", "hasattr",
                         "hash", "help", "hex", "id", "input", "int", "isinstance", "issubclass",
                         "iter", "len", "list", "locals", "map", "max", "memoryview", "min",
                         "next", "object", "oct", "open", "ord", "pow", "print", "property",
                         "range", "repr", "reversed", "round", "set", "setattr", "slice",
                         "sorted", "staticmethod", "str", "sum", "super", "tuple", "type",
                         "vars", "zip", "__import__"]

    def apply_syntax_highlighting(self):
        for tag in self.code_text.tag_names():
            self.code_text.tag_remove(tag, "1.0", tk.END)

        content = self.code_text.get("1.0", tk.END)

        # Highlight comments
        for match in self.find_all(content, r"#[^\n]*"):
            start, end = match
            self.code_text.tag_add("comment", f"1.0+{start}c", f"1.0+{end}c")

        # Highlight strings (single and double quoted)
        for match in self.find_all(content, r"(\".*?\")|(\'.*?\')"):
            start, end = match
            self.code_text.tag_add("string", f"1.0+{start}c", f"1.0+{end}c")

        # Highlight numbers
        for match in self.find_all(content, r"\b\d+\b"):
            start, end = match
            self.code_text.tag_add("number", f"1.0+{start}c", f"1.0+{end}c")

        # Highlight keywords
        for keyword in self.keywords:
            for match in self.find_all(content, r"\b" + keyword + r"\b"):
                start, end = match
                self.code_text.tag_add("keyword", f"1.0+{start}c", f"1.0+{end}c")

        # Highlight built-ins
        for builtin in self.builtins:
            for match in self.find_all(content, r"\b" + builtin + r"\b"):
                start, end = match
                self.code_text.tag_add("builtin", f"1.0+{start}c", f"1.0+{end}c")

        # Highlight function/class definitions
        for match in self.find_all(content, r"\b(def|class)\s+([a-zA-Z_][a-zA-Z0-9_]*)\b"):
            start_def, end_def = match
            # Find the actual function/class name within the match
            def_keyword_index = content.find("def", start_def)
            if def_keyword_index == -1: # Try "class"
                def_keyword_index = content.find("class", start_def)

            if def_keyword_index != -1:
                name_start = content.find(" ", def_keyword_index) + 1
                name_end = name_start
                while name_end < len(content) and (content[name_end].isalnum() or content[name_end] == '_'):
                    name_end += 1
                if name_start < name_end:
                    self.code_text.tag_add("definition", f"1.0+{name_start}c", f"1.0+{name_end}c")

    def find_all(self, text, pattern):
        import re
        matches = []
        for match in re.finditer(pattern, text):
            matches.append((match.start(), match.end()))
        return matches

    def update_line_numbers(self):
        line_count = self.code_text.get("1.0", tk.END).count("\n")
        self.line_numbers.config(state="normal")
        self.line_numbers.delete("1.0", tk.END)
        for i in range(1, line_count + 1):
            self.line_numbers.insert(tk.END, f"{i}\n")
        self.line_numbers.config(state="disabled")

    def update_line_numbers_and_highlight(self, event=None):
        self.update_line_numbers()
        self.apply_syntax_highlighting()
        self.sync_scroll() # Ensure scroll sync after updates

    def sync_scroll(self, *args):
        # Syncs vertical scroll between code_text and line_numbers
        self.line_numbers.yview_moveto(self.code_text.yview()[0])

    def sync_scroll_mouse(self, event):
        # Syncs vertical scroll when using mouse wheel
        self.code_text.yview_scroll(-1 * (event.delta // 120), "units")
        self.line_numbers.yview_moveto(self.code_text.yview()[0])
        return "break" # Prevent default scrolling on the line numbers widget

    def new_file(self, event=None):
        if messagebox.askyesno("New File", "Do you want to save the current file?"):
            self.save_file()
        self.code_text.delete("1.0", tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state="disabled")
        self.current_file_path = None
        self.master.title("PyEditor - Untitled")
        self.status_bar.config(text="New file created.")
        self.update_line_numbers_and_highlight()

    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(defaultextension=".py",
                                               filetypes=[("Python files", "*.py"),
                                                          ("All files", "*.*")])
        if file_path:
            self.current_file_path = file_path
            with open(file_path, "r") as file:
                content = file.read()
                self.code_text.delete("1.0", tk.END)
                self.code_text.insert("1.0", content)
            self.master.title(f"PyEditor - {os.path.basename(file_path)}")
            self.status_bar.config(text=f"Opened: {os.path.basename(file_path)}")
            self.update_line_numbers_and_highlight()
            self.output_text.config(state="normal")
            self.output_text.delete("1.0", tk.END)
            self.output_text.config(state="disabled")

    def save_file(self, event=None):
        if self.current_file_path:
            with open(self.current_file_path, "w") as file:
                file.write(self.code_text.get("1.0", tk.END))
            self.status_bar.config(text=f"Saved: {os.path.basename(self.current_file_path)}")
        else:
            self.save_file_as()

    def save_file_as(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                                 filetypes=[("Python files", "*.py"),
                                                            ("All files", "*.*")])
        if file_path:
            self.current_file_path = file_path
            with open(file_path, "w") as file:
                file.write(self.code_text.get("1.0", tk.END))
            self.master.title(f"PyEditor - {os.path.basename(file_path)}")
            self.status_bar.config(text=f"Saved As: {os.path.basename(file_path)}")

    def run_code(self, event=None):
        if not self.current_file_path:
            messagebox.showwarning("Run Code", "Please save the file before running.")
            self.save_file_as()
            if not self.current_file_path: # If user cancels Save As
                return

        code = self.code_text.get("1.0", tk.END)
        # It's safer to save the file and then run it
        self.save_file()

        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, "Running code...\n")
        self.output_text.config(state="disabled")
        self.output_text.update_idletasks() # Force update

        try:
            # Use subprocess to run the Python file
            # Capture stdout and stderr
            process = subprocess.run(["python", self.current_file_path],
                                     capture_output=True, text=True, check=False)

            self.output_text.config(state="normal")
            self.output_text.insert(tk.END, "\n--- Output ---\n")
            if process.stdout:
                self.output_text.insert(tk.END, process.stdout)
            if process.stderr:
                self.output_text.insert(tk.END, "\n--- Error ---\n", "error_tag")
                self.output_text.tag_configure("error_tag", foreground="red")
                self.output_text.insert(tk.END, process.stderr)
            self.output_text.insert(tk.END, "\n--- Run Complete ---\n")
            self.output_text.config(state="disabled")
            self.output_text.see(tk.END) # Scroll to end of output
            self.status_bar.config(text="Code execution complete.")

        except FileNotFoundError:
            messagebox.showerror("Error", "Python interpreter not found. Make sure Python is installed and in your PATH.")
            self.output_text.config(state="normal")
            self.output_text.insert(tk.END, "\nError: Python interpreter not found.\n")
            self.output_text.config(state="disabled")
        except Exception as e:
            self.output_text.config(state="normal")
            self.output_text.insert(tk.END, f"\nAn unexpected error occurred: {e}\n")
            self.output_text.config(state="disabled")


    # --- Basic Editing Functions ---
    def cut_text(self):
        self.code_text.event_generate("<<Cut>>")

    def copy_text(self):
        self.code_text.event_generate("<<Copy>>")

    def paste_text(self):
        self.code_text.event_generate("<<Paste>>")

    def undo_text(self):
        try:
            self.code_text.edit_undo()
        except tk.TclError:
            pass # No more undo history

    def redo_text(self):
        try:
            self.code_text.edit_redo()
        except tk.TclError:
            pass # No more redo history


if __name__ == "__main__":
    root = tk.Tk()
    editor = PythonCodeEditor(root)
    root.mainloop()