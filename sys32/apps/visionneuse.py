import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_view():
    def create_image_viewer(file_path):
        root.title("Visionneuse de Photos")

        image = Image.open(file_path)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(root, image=photo)
        label.photo = photo
        label.pack()

    root = tk.Tk()
    root.title("Simple Photo Viewer")

    open_button = tk.Button(root, text="Ouvrir une image", command=open_view)
    open_button.pack()

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

    if file_path:
        create_image_viewer(file_path)

