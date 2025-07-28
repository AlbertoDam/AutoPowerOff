import customtkinter as ctk

class ActionButtons:
    def __init__(self, parent, row, columnspan, colors):
        frame = ctk.CTkFrame(parent, fg_color=colors["bg"], corner_radius=0)
        frame.grid(row=row, column=0, columnspan=columnspan, pady=(0,15))
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)

        self.start = ctk.CTkButton(
            frame,
            text="Start",
            text_color=colors["shutdown_btn_text"],
            fg_color=colors["shutdown_btn_bg"],
            width=140
        )
        self.start.grid(row=0, column=0, padx=10)

        self.cancel = ctk.CTkButton(
            frame,
            text="Cancel",
            text_color=colors["shutdown_btn_text"],
            fg_color=colors["time_elements"],
            width=140
        )
        self.cancel.grid(row=0, column=1, padx=10)
