import tkinter as tk
import shutil
import os

def installer(path):
    shutil.copy(path, os.path.dirname(__file__))

installer(r"C:\Users\Jules07\OneDrive\Bureau\python\convert.py")
