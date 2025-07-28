import tkinter as tk

class SettingsMenu:
    def __init__(self, parent, esp_image, eng_image):
        """
        Crea una barra de menú con Settings → Language → Español/English.
        esp_image y eng_image deben ser objetos PhotoImage ya cargados.
        """
        menubar = tk.Menu(parent)
        settings_menu = tk.Menu(menubar, tearoff=0)
        language_menu = tk.Menu(settings_menu, tearoff=0)

        language_menu.add_command(
            label="Español", image=esp_image, compound="left"
        )
        language_menu.add_command(
            label="English", image=eng_image, compound="left"
        )

        settings_menu.add_cascade(label="Language", menu=language_menu)
        menubar.add_cascade(label="Settings", menu=settings_menu)
        parent.config(menu=menubar)
