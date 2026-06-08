import subprocess
import os
from datetime import datetime

class TsharkCapture:

    def __init__(self):
        self.process = None
        self.capture_file = None

    def start(self, interface):
        os.makedirs("captures", exist_ok=True)

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        self.capture_file = (
            f"captures/capture_{timestamp}.pcap"
        )

        self.process = subprocess.Popen(
            [
                "tshark",
                "-i",
                interface,
                "-w",
                self.capture_file
            ]
        )

        print(
            f"\nCapture started."
            f"\nPCAP File: {self.capture_file}"
        )

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process.wait()

            print(
                f"\nCapture saved to:"
                f"\n{self.capture_file}"
            )

    def is_running(self):
        return (
            self.process is not None
            and self.process.poll() is None
        )