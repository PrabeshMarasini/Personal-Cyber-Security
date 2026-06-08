from datetime import datetime


class CaptureManager:

    def __init__(self):
        self.session = {}

    def start_session(self, interface, pcap_file):
        self.session = {
            "interface": interface,
            "pcap_file": pcap_file,
            "start_time": datetime.now()
        }

    def stop_session(self):
        self.session["end_time"] = datetime.now()

    def get_session(self):
        return self.session