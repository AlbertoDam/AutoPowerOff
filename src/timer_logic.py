import os
import threading
import time

class ShutdownTimer:
    def __init__(self):
        self.remaining_time = 0
        self.timer_running = False
        self._on_tick = None       
        self._on_finish = None     
        self._lock = threading.Lock()

    def set_callbacks(self, on_tick, on_finish):
        self._on_tick = on_tick
        self._on_finish = on_finish

    def start(self, minutes: int):
        with self._lock:
            if self.timer_running:
                return 
            self.remaining_time = minutes * 60
            self.timer_running = True
        threading.Thread(target=self._run_timer, daemon=True).start()

    def cancel(self):
        with self._lock:
            self.timer_running = False

    def _run_timer(self):
        while True:
            with self._lock:
                if not self.timer_running:
                    return  
                if self.remaining_time <= 0:
                    break
                mins, secs = divmod(self.remaining_time, 60)
            if self._on_tick:
                self._on_tick(mins, secs)
            time.sleep(1)
            with self._lock:
                self.remaining_time -= 1
       
        with self._lock:
            if self.timer_running and self.remaining_time <= 0:
                if self._on_finish:
                    self._on_finish()
                os.system("shutdown /s /t 0")
