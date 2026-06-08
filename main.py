from capture.interface_selector import InterfaceSelector
from capture.tshark_capture import TsharkCapture
from capture.capture_manager import CaptureManager


def main():
    selector = InterfaceSelector()
    capture = TsharkCapture()
    manager = CaptureManager()

    try:
        selected_interface = selector.choose_interface()

        print(f"\nSelected Interface: {selected_interface}")

        capture.start(selected_interface)

        manager.start_session(
            selected_interface,
            capture.capture_file
        )

        print(
            "\nCapture running..."
            "\nPress ENTER to stop."
        )

        input()

        capture.stop()

        manager.stop_session()

        print("\nSession Metadata:")

        for key, value in (
            manager.get_session().items()
        ):
            print(f"{key}: {value}")

    except KeyboardInterrupt:
        print("\nStopping capture...")
        capture.stop()
        manager.stop_session()

if __name__ == "__main__":
    main()