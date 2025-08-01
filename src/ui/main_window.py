import customtkinter as ctk
import os
from pathlib import Path
from PIL import Image, ImageTk

from ui.header import Header
from ui.time_input import TimeInput
from ui.action_buttons import ActionButtons
from ui.countdown_display import CountdownDisplay
from ui.settings_menu import SettingsMenu


class AutoPowerOffWindow(ctk.CTk):
    def __init__(self, colors, esp_img=None, eng_img=None):
        super().__init__()
        self.title("Auto Power Off")
        self.resizable(False, False)
        self.colors = colors
        self.configure(fg_color=self.colors["bg"])

        base = Path(__file__).parent 
        assets = (base.parent / "assets").resolve()
        icon_path = assets / "icon.ico"
        if icon_path.exists():
            try:
                self.iconbitmap(str(icon_path))
            except Exception:
                pass 

        def make_flag(name):
            for ext in (".ico", ".png"):
                candidate = assets / f"{name}{ext}" if not name.lower().endswith(ext) else assets / name
                if candidate.exists():
                    try:
                        img = Image.open(candidate).convert("RGBA")
                        img = img.resize((16, 16), Image.LANCZOS)
                        return ImageTk.PhotoImage(img)
                    except Exception:
                        continue
            return None

        self._esp_img = esp_img if esp_img is not None else make_flag("esp")
        self._eng_img = eng_img if eng_img is not None else make_flag("gb")

        SettingsMenu(self, self._esp_img, self._eng_img)

        for i in range(7):
            self.grid_rowconfigure(i, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        Header(self, row=0, columnspan=2, colors=self.colors)
        self.time_input = TimeInput(self, row=1, columnspan=2, colors=self.colors)
        self.buttons = ActionButtons(self, row=5, columnspan=2, colors=self.colors)
        self.countdown = CountdownDisplay(self, row=6, columnspan=2, colors=self.colors)

        self.start_button = self.buttons.start
        self.cancel_button = self.buttons.cancel

        self.on_start = None
        self.on_cancel = None

        self.time_input.on_validity_change = lambda valid: self.start_button.configure(state="normal" if valid else "disabled")
        self.start_button.configure(state="normal" if self.time_input.is_valid() else "disabled")

        self.start_button.configure(command=lambda: self.on_start() if self.on_start else None)
        self.cancel_button.configure(command=lambda: self.on_cancel() if self.on_cancel else None)

        self.update_idletasks()
        w, h = self.winfo_reqwidth(), self.winfo_reqheight()
        self.geometry(f"{w}x{h+5}")

    def set_countdown(self, mins: int, secs: int):
        self.countdown.set_time(mins, secs)

    def set_message(self, msg: str):
        self.countdown.set_message(msg)
