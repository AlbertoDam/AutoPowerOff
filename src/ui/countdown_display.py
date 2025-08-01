import customtkinter as ctk

class CountdownDisplay:
    def __init__(self, parent, row, columnspan, colors):
        self.label = ctk.CTkLabel(
            parent,
            text="00:00",
            text_color=colors["time_elements"]
        )
        self.label.grid(row=row, column=0, columnspan=columnspan, pady=(0,20))

    def set_time(self, mins: int, secs: int):
        self.label.configure(text=f"{mins:02d}:{secs:02d}")

    def set_message(self, text: str):
        self.label.configure(text=text)
