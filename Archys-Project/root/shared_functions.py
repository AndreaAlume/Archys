import customtkinter as ctk
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_image(path, size):
    img = Image.open(os.path.join(BASE_DIR, path))
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)