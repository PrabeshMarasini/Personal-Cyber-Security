import psutil


def get_packet_counts():
    stats = psutil.net_io_counters(pernic=True)

    return {
        iface: stats[iface].packets_recv + stats[iface].packets_sent
        for iface in stats
    }


class InterfaceMonitor:
    def __init__(self):
        self.start_counts = get_packet_counts()

    def get_counts_since_start(self):
        current = get_packet_counts()

        result = {}

        for iface in self.start_counts:
            result[iface] = (
                current[iface] - self.start_counts[iface]
            )

        return result

    def get_active_interfaces(self):
        counts = self.get_counts_since_start()

        return {
            iface: packets
            for iface, packets in counts.items()
            if packets > 0
        }

    def get_most_active_interface(self):
        counts = self.get_counts_since_start()

        if not counts:
            return None

        return max(counts, key=counts.get)