from ui.main_window import AutoPowerOffWindow
from timer_logic import ShutdownTimer
from utils.theme_config import get_theme_colors

class AppController:
    def __init__(self):
        self.colors = get_theme_colors()
        self.window = AutoPowerOffWindow(self.colors)
        self.timer = ShutdownTimer()
        self.timer.set_callbacks(self._on_tick, self._on_finish)

        self.window.on_start = self.start
        self.window.on_cancel = self.cancel

    def start(self):
        minutes = self.window.time_input.get_minutes()
        if minutes is None:
            self.window.set_message("Please provide a valid minute value.")
            return
        self.window.set_countdown(minutes, 0)
        self.timer.start(minutes)
        self.window.buttons.start.configure(state="disabled")

    def cancel(self):
        self.timer.cancel()
        self.window.set_message("Cancelled")
        self.window.buttons.start.configure(state="normal")

    def _on_tick(self, mins, secs):
        self.window.set_countdown(mins, secs)

    def _on_finish(self):
        self.window.set_message("Shutting down...")

    def run(self):
        self.window.mainloop()
