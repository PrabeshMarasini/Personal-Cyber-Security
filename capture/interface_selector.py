import psutil
import time
import threading


class InterfaceSelector:

    def get_packet_counts(self):
        stats = psutil.net_io_counters(pernic=True)

        return {
            iface: stats[iface].packets_recv + stats[iface].packets_sent
            for iface in stats
        }

    def get_activity(self, duration=5):
        start = self.get_packet_counts()

        time.sleep(duration)

        end = self.get_packet_counts()

        return {
            iface: end[iface] - start[iface]
            for iface in start
        }

    def choose_interface(self):
        activity = self.get_activity()

        interfaces = list(activity.keys())

        print("\nAvailable Interfaces:\n")

        for idx, iface in enumerate(interfaces, start=1):
            print(
                f"{idx}. {iface:<15} "
                f"({activity[iface]} packets)"
            )

        user_choice = {"value": None}

        def get_input():
            try:
                user_choice["value"] = input(
                    "\nSelect interface (30s timeout): "
                )

            except Exception:
                pass

        input_thread = threading.Thread(
            target = get_input,
            daemon = True
        )

        input_thread.start()

        input_thread.join(timeout=30)

        if user_choice["value"] is not None:
            try:
                choice = int(user_choice["value"])

                if 1 <= choice <= len(interfaces):
                    return interfaces[choice - 1]

            except ValueError:
                pass

        most_active = max(
            activity,
            key=activity.get
        )

        print(
            f"\nAutomatically selecting the Interface: "
            f"{most_active}"
            f"({activity[most_active]} packets)"
        )

        return most_active