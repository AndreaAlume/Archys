import customtkinter as ctk
from PIL import Image, ImageTk  # Pillow
import os

width, height = 1500, 1000
title = "Archys"

bg_color = "#000000"
frame_color = "#1a1a1a"
text_color = "#ffffff"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

def load_image(path, size):
    img = Image.open(os.path.join(BASE_DIR, path))
    img = img.resize(size, Image.LANCZOS)
    return ImageTk.PhotoImage(img)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{width}x{height}")
        self.title(title)
        logo = load_image("./logo.png", (500, 500))
        self.iconphoto(True, logo)
        self.resizable(False, False)
        self.configure(fg_color=bg_color)

        left_frame = ctk.CTkFrame(self, width=300, fg_color=frame_color)
        left_frame.pack(fill="y", side="left")
        left_frame.pack_propagate(False)

        menus = ["Package Manager", "Software Manager", "Backup and Export", "Maintainance System", "Networking and Security"]

        icon_folder = os.path.join(BASE_DIR, "./icons")
        icon_files = sorted(os.listdir(icon_folder)) 

        for i, menu_name in enumerate(menus):
            menu_frame = ctk.CTkFrame(left_frame, height=40, width=250, fg_color=frame_color)
            menu_frame.pack(pady=10)
            menu_frame.pack_propagate(False)

            icon_path = os.path.join(icon_folder, icon_files[i % len(icon_files)])

            img = Image.open(icon_path)
            img = img.resize((30, 30))
            photo = ImageTk.PhotoImage(img)

            label = ctk.CTkLabel(menu_frame, text=menu_name, width=250, image=photo, compound="left",
                                fg_color=frame_color, text_color=text_color, anchor="w", padx=10)
            label.pack(pady=(10, 0))

        settings_frame = ctk.CTkFrame(left_frame, height=40, width=250, fg_color=frame_color)
        settings_frame.pack(pady=10, side="bottom")
        settings_frame.pack_propagate(False)

        settings_icon_path = os.path.join(icon_folder, "06settings.png")
        settings_icon = Image.open(settings_icon_path)
        settings_icon = settings_icon.resize((30, 30))
        photo_settings = ImageTk.PhotoImage(settings_icon)

        settings_label = ctk.CTkLabel(settings_frame, text="Settings", image=photo_settings, compound="left", width=250,
            fg_color=frame_color,
            text_color=text_color,
            anchor="w",
        )
        settings_label.pack(padx=10)

app = App()
app.mainloop()
