import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from shared_functions import *

label_color = "#000000"

class ProcessAdministrator(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#000000")

        title_label = ctk.CTkLabel(self, text="Archys Package Manager", font=ctk.CTkFont(size=38))
        title_label.place(x=30, y=30)

        question_icon = load_image(f"{BASE_DIR}/package_manager/question.png", (25, 25))
        button = ctk.CTkButton(self, text="", image=question_icon, fg_color=label_color, compound="left", width=30, corner_radius=0)
        button.place(x=590, y=45)
        