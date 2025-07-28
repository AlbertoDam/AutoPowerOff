import customtkinter as ctk

class TimeInput:
    def __init__(self, parent, row, columnspan, colors):
        lbl = ctk.CTkLabel(
            parent,
            text="Time (minutes):",
            text_color=colors["text"]
        )
        lbl.grid(row=row, column=0, columnspan=columnspan, padx=20, pady=(0,5), sticky="w")

        self.entry = ctk.CTkEntry(
            parent,
            fg_color=colors["entry_bg"],
            border_color=colors["entry_border"],
            border_width=2,
            text_color=colors["text"]
        )
        self.entry.grid(row=row+1, column=0, columnspan=columnspan, padx=20, pady=(0,15), sticky="ew")
