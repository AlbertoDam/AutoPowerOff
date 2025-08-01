import customtkinter as ctk

class TimeInput:
    def __init__(self, parent, row, columnspan, colors, min_minutes=1, max_minutes=60*3):
        self.colors = colors
        self.min_minutes = min_minutes
        self.max_minutes = max_minutes
        self._last_valid_state = None
        self.on_validity_change = None 

        lbl = ctk.CTkLabel(
            parent,
            text="Time (minutes):",
            text_color=colors["text"],
            anchor="w"
        )
        lbl.grid(row=row, column=0, columnspan=columnspan, padx=20, pady=(0,2), sticky="w")

        self.var = ctk.StringVar()
        self.entry = ctk.CTkEntry(
            parent,
            textvariable=self.var,
            placeholder_text="e.g. 5",
            fg_color=colors["entry_bg"],
            border_color=colors["entry_border"],
            border_width=2,
            text_color=colors["text"]
        )
        self.entry.grid(row=row+1, column=0, columnspan=columnspan, padx=20, pady=(0,2), sticky="ew")

        self.helper_label = ctk.CTkLabel(
            parent,
            text=f"Enter between {self.min_minutes} and {self.max_minutes} minutes.",
            text_color=colors["text"],
            font=ctk.CTkFont(size=11),
            anchor="w"
        )
        self.helper_label.grid(row=row+2, column=0, columnspan=columnspan, padx=20, pady=(0,2), sticky="w")

        self.error_label = ctk.CTkLabel(
            parent,
            text="",
            text_color=colors["shutdown_btn_bg"], 
            font=ctk.CTkFont(size=11),
            anchor="w"
        )
        self.error_label.grid(row=row+3, column=0, columnspan=columnspan, padx=20, pady=(0,10), sticky="w")

        self.var.trace_add("write", self._on_change)
        self._validate_and_notify()

    def _on_change(self, *args):
        self._validate_and_notify()

    def _validate_and_notify(self):
        valid = self._validate()
        if valid != self._last_valid_state:
            self._last_valid_state = valid
            if self.on_validity_change:
                try:
                    self.on_validity_change(valid)
                except Exception:
                    pass

    def _validate(self) -> bool:
        s = self.var.get().strip()
        if s == "":
            self._set_invalid("You need to enter a number of minutes.")
            return False
        if not s.isdigit():
            self._set_invalid("Only positive integer numbers are allowed.")
            return False
        try:
            v = int(s)
        except Exception:
            self._set_invalid("Invalid value.")
            return False
        if v < self.min_minutes:
            self._set_invalid(f"The minimum is {self.min_minutes} minute{'s' if self.min_minutes != 1 else ''}.")
            return False
        if v > self.max_minutes:
            self._set_invalid(f"The maximum is {self.max_minutes} minutes ({self.max_minutes//60}h).")
            return False
        self._set_valid()
        return True

    def _set_invalid(self, msg: str):
        self.entry.configure(border_color=self.colors["shutdown_btn_bg"])
        self.error_label.configure(text=msg)

    def _set_valid(self):
        self.entry.configure(border_color=self.colors["entry_border"])
        self.error_label.configure(text="")

    def get_minutes(self):
        if self._validate():
            return int(self.var.get().strip())
        return None

    def is_valid(self):
        return self._validate()
