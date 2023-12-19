import tkinter as tk
import shutil
import os

def installer():
    path = tk.filedialog.askdirectory()
    shutil.copy(path, os.path.dirname(__file__))

installer(r"C:\Users\Jules07\OneDrive\Bureau\python\convert.py")
