import tkinter as tk
import os
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
import sys32.apps.supertext, sys32.apps.visionneuse

def error(titre='Erreur', message="Une erreur s'est produite"):
    showerror(title, message)
def menu():
    menu = tk.Toplevel(root)
    
def open_file_explorer():
    folder_path = filedialog.askdirectory()
    if folder_path:
        create_explorer_window(folder_path)

def open_text_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    text_window = tk.Toplevel(root)
    text_window.title("Contenu du fichier texte")
    text_widget = scrolledtext.ScrolledText(text_window, wrap=tk.WORD)
    text_widget.insert(tk.END, content)
    text_widget.pack(fill=tk.BOTH, expand=True)

def create_explorer_window(folder_path):
    explorer = tk.Toplevel(root)
    explorer.title("Explorateur de fichiers")
    explorer.iconbitmap("imagesa.ico")
    explorer.geometry("400x200")

    treeview = ttk.Treeview(explorer)
    treeview.pack()

    treeview.heading("#0", text="Nom")

    for item in os.listdir(folder_path):
        treeview.insert("", "end", text=item)

    def on_item_double_click(event):
        item_id = treeview.selection()[0]
        item_text = treeview.item(item_id, "text")
        item_path = os.path.join(folder_path, item_text)
        print(item_path)

        if os.path.isdir(item_path):
            create_explorer_window(item_path)
        elif item_text.endswith(".txt"):
            sys32.apps.supertext.open_editor(item_path)
    
    treeview.bind("<Double-1>", on_item_double_click)        

def open_start_menu():
    start_menu_window = tk.Toplevel(root)
    start_menu_window.title("Menu Démarrer Windows 98")

    button_program_1 = tk.Button(start_menu_window, text="Bloc-notes", command=sys32.apps.supertext.open_editor)
    button_program_1.pack()

    button_program_2 = tk.Button(start_menu_window, text="Explorateur", command=open_file_explorer)
    button_program_2.pack()

root = tk.Tk()
root.title("Windows 98")
root.geometry('800x400')

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Ouvrir", command=open_file_explorer)
file_menu.add_command(label="Enregistrer")
file_menu.add_separator()
file_menu.add_command(label="Quitter")

root.iconbitmap("imagesez.ico")

# Création d'un bouton "Démarrer"
start_button = tk.Button(root, text="Démarrer", command=open_start_menu)
start_button.pack(side="bottom")

icon_image = Image.open("imagesas.png")
icon_photo = ImageTk.PhotoImage(icon_image)

icon_image2 = Image.open("imagess.png")
icon_photo2 = ImageTk.PhotoImage(icon_image2)
# Ajouter un bouton avec l'icône "Ouvrir"
open_button = tk.Button(root, image=icon_photo, command=open_file_explorer)
open_button.pack()

open_button2 = tk.Button(root, image=icon_photo2, command=sys32.apps.supertext.open_editor)
open_button2.pack()

open_button3 = tk.Button(root, text="visionneuse", command=sys32.apps.visionneuse.open_view)
open_button3.pack()
try:
    root.mainloop()
except:
    error()
