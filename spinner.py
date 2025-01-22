import sys
import threading
import time

class Spinner:
    def __init__(self, message="Processing"):
        self.message = message
        self.stop_running = False
        self.spinner = ['|', '/', '-', '\\']
        self.index = 0

    def start(self):
        self.stop_running = False
        threading.Thread(target=self._spin, daemon=True).start()

    def stop(self):
        self.stop_running = True
        sys.stdout.write('\r')  # Clear the line
        sys.stdout.flush()

    def _spin(self):
        while not self.stop_running:
            sys.stdout.write(f'\r{self.message} {self.spinner[self.index % len(self.spinner)]}')
            sys.stdout.flush()
            self.index += 1
            time.sleep(0.1)  # Adjust spinner speed

