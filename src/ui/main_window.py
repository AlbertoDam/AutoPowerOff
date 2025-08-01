import customtkinter as ctk
import os
from pathlib import Path
from utils.theme_detector import is_light_mode
from utils.theme_config import get_theme_colors
from PIL import Image, ImageTk

from ui.header import Header
from ui.time_input import TimeInput
from ui.action_buttons import ActionButtons
from ui.countdown_display import CountdownDisplay
from ui.settings_menu import SettingsMenu
from timer_logic import ShutdownTimer 

class AutoPowerOffApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Auto Power Off")
        self.resizable(False, False)

        ctk.set_appearance_mode("Light" if is_light_mode() else "Dark")
        self.colors = get_theme_colors()
        self.configure(fg_color=self.colors["bg"])

        base = os.path.dirname(__file__)  # src/ui
        assets_dir = os.path.abspath(os.path.join(base, "../..", "assets"))

        icon_path = os.path.join(assets_dir, "icon.ico")
        if os.path.exists(icon_path):
            try:
                self.iconbitmap(icon_path)
            except Exception:
                pass

        def load_flag(name):
            for ext in (".ico", ".png"):
                filename = name if name.lower().endswith(ext) else name + ext
                path = os.path.join(assets_dir, filename)
                if os.path.exists(path):
                    try:
                        img = Image.open(path).convert("RGBA")
                        img = img.resize((16, 16), Image.LANCZOS)
                        return ImageTk.PhotoImage(img)
                    except Exception:
                        continue
            return None

        esp_img = load_flag("esp")
        eng_img = load_flag("gb")

        self._esp_img = esp_img
        self._eng_img = eng_img

        if esp_img and eng_img:
            SettingsMenu(self, esp_img, eng_img)
        else:
            SettingsMenu(self, esp_img or None, eng_img or None)

        for i in range(7):  
            self.grid_rowconfigure(i, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        Header(self, row=0, columnspan=2, colors=self.colors)
        self.time_input = TimeInput(self, row=1, columnspan=2, colors=self.colors)
        self.buttons = ActionButtons(self, row=5, columnspan=2, colors=self.colors)
        self.countdown = CountdownDisplay(self, row=6, columnspan=2, colors=self.colors)

        self.time_input.on_validity_change = lambda valid: self.buttons.start.configure(state="normal" if valid else "disabled")
        self.buttons.start.configure(state="normal" if self.time_input.is_valid() else "disabled")

        self.timer = ShutdownTimer()
        self.timer.set_callbacks(self._on_tick, self._on_finish)
        self.buttons.start.configure(command=self._start)
        self.buttons.cancel.configure(command=self._cancel)

        self.update_idletasks()
        w, h = self.winfo_reqwidth(), self.winfo_reqheight()
        self.geometry(f"{w}x{h+5}")

    def _start(self):
        minutes = self.time_input.get_minutes()
        if minutes is None:
            self.countdown.set_message("Please provide a valid minute value.")
            return
        self.countdown.set_time(minutes, 0)
        self.timer.start(minutes)
        self.buttons.start.configure(state="disabled")

    def _cancel(self):
        self.timer.cancel()
        self.countdown.set_message("Cancelled")
        self.buttons.start.configure(state="normal")

    def _on_tick(self, mins, secs):
        self.after(0, lambda: self.countdown.set_time(mins, secs))

    def _on_finish(self):
        self.after(0, lambda: self.countdown.set_message("Shutting down..."))
