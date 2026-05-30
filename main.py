from fastapi import FastAPI
from packetcapture.active_interface import InterfaceMonitor

app = FastAPI()

monitor = InterfaceMonitor()


@app.get("/")
def root():
    return {
        "message": "Network Interface Monitor"
    }


@app.get("/interfaces")
def all_interfaces():
    """
    Returns packet counts since app startup.
    """
    return monitor.get_counts_since_start()


@app.get("/interfaces/active")
def active_interfaces():
    """
    Returns only interfaces with traffic.
    """
    return monitor.get_active_interfaces()


@app.get("/interfaces/most-active")
def most_active_interface():
    """
    Returns the busiest interface.
    """
    iface = monitor.get_most_active_interface()

    return {
        "interface": iface
    }