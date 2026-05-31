import psutil
import time


class InterfaceSelector:

    def get_packet_counts(self):
        stats = psutil.net_io_counters(pernic=True)

        return {
            iface: stats[iface].packets_recv + stats[iface].packets_sent
            for iface in stats
        }

    def get_activity(self, duration=2):
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

        while True:
            try:
                choice = int(
                    input("\nSelect interface: ")
                )

                if 1 <= choice <= len(interfaces):
                    return interfaces[choice - 1]

            except ValueError:
                pass

            print("Invalid selection.")