import tkinter as tk
from tkinter import filedialog

text_widget=None
current_text=""
undo_stack = []
redo_stack = []

def new_file():
    text_widget.delete('1.0', tk.END)
    update_text()

def open_file(file_path=None):
    if not file_path:
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, content)
        update_text()

def save_file():
    if not file_path:
        save_file_as()
    else:
        content = text_widget.get('1.0', tk.END)
        with open(file_path, 'w') as file:
            file.write(content)
        update_text()

def save_file_as():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        save_file()

def undo():
    if undo_stack:
        global current_text
        redo_stack.append(current_text)
        current_text = undo_stack.pop()
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, current_text)

def redo():
    if redo_stack:
        global current_text
        undo_stack.append(current_text)
        current_text = redo_stack.pop()
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, current_text)

def update_text():
    global current_text
    new_text = text_widget.get('1.0', tk.END)
    if new_text != current_text:
        undo_stack.append(current_text)
        redo_stack.clear()
        current_text = new_text

def open_editor(path=None):
    global text_widget
    
    root = tk.Tk()
    root.title("Bloc-notes")

    text_widget = tk.Text(root, wrap=tk.WORD)
    text_widget.pack(expand=True, fill='both')

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Fichier", menu=file_menu)
    file_menu.add_command(label="Nouveau", command=new_file)
    file_menu.add_command(label="Ouvrir", command=open_file)
    file_menu.add_command(label="Enregistrer", command=save_file)
    file_menu.add_command(label="Enregistrer sous...", command=save_file_as)
    file_menu.add_separator()
    file_menu.add_command(label="Quitter", command=root.destroy)

    edit_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Éditer", menu=edit_menu)
    edit_menu.add_command(label="Annuler", command=undo)
    edit_menu.add_command(label="Rétablir", command=redo)

    # Historique des modifications
    current_text = ""

    # Configuration des raccourcis clavier
    root.bind('<Control-z>', lambda event: undo())
    root.bind('<Control-y>', lambda event: redo)

    if path:
        open_file(path)

    root.mainloop()

if __name__ == "__main__":
    open_editor()
