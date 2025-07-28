import customtkinter as ctk
import os
import tkinter as tk
from utils.theme_detector import is_light_mode
from utils.theme_config import get_theme_colors
from PIL import Image, ImageTk

from ui.header import Header
from ui.time_input import TimeInput
from ui.action_buttons import ActionButtons
from ui.countdown_display import CountdownDisplay
from ui.settings_menu import SettingsMenu

class AutoPowerOffApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Auto Power Off")
        self.resizable(False, False)

        ctk.set_appearance_mode("Light" if is_light_mode() else "Dark")
        self.colors = get_theme_colors()
        self.configure(fg_color=self.colors["bg"])

        base = os.path.dirname(__file__)
        icon_path = os.path.abspath(os.path.join(base, "../..", "assets", "icon.ico"))
        if os.path.exists(icon_path):
            self.iconbitmap(icon_path)

        esp_img = ImageTk.PhotoImage(
            Image.open(os.path.join(base, "../..", "assets", "esp.ico")).resize((16,16))
        )
        eng_img = ImageTk.PhotoImage(
            Image.open(os.path.join(base, "../..", "assets", "gb.ico")).resize((16,16))
        )
        self._esp_img, self._eng_img = esp_img, eng_img

        SettingsMenu(self, esp_img, eng_img)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        Header(self, row=0, columnspan=2, colors=self.colors)
        TimeInput(self, row=1, columnspan=2, colors=self.colors)
        ActionButtons(self, row=3, columnspan=2, colors=self.colors)
        CountdownDisplay(self, row=4, columnspan=2, colors=self.colors)

        self.update_idletasks()
        w, h = self.winfo_reqwidth(), self.winfo_reqheight()
        self.geometry(f"{w}x{h}")
