import subprocess


class TsharkCapture:

    def __init__(self):
        self.process = None

    def start(self, interface):
        self.process = subprocess.Popen(
            [
                "tshark",
                "-i",
                interface
            ]
        )

        self.process.wait()

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process.wait()