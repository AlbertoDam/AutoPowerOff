import customtkinter as ctk

class Header:
    def __init__(self, parent, row, columnspan, colors):
        frame = ctk.CTkFrame(parent, fg_color=colors["bg"], corner_radius=0)
        frame.grid(row=row, column=0, columnspan=columnspan, sticky="ew", padx=20, pady=(20,10))
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=0)

        self.desc = ctk.CTkLabel(
            frame,
            text="Introduce los minutos que deseas retrasar el apagado automático del equipo.",
            text_color=colors["text"],
            wraplength=360,
            justify="left",
            font=ctk.CTkFont(size=14)
        )
        self.desc.grid(row=0, column=0, sticky="w")

