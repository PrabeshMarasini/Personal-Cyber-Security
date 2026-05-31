from capture.interface_selector import InterfaceSelector
from capture.tshark_capture import TsharkCapture


def main():
    selector = InterfaceSelector()
    capture = TsharkCapture()

    try:
        selected_interface = selector.choose_interface()

        print(f"\nSelected Interface: {selected_interface}")

        capture.start(selected_interface)

    except KeyboardInterrupt:
        print("\nStopping capture...")
        capture.stop()


if __name__ == "__main__":
    main()