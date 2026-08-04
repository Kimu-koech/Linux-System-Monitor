import psutil
from monitor.utils import format_bytes

def get_bytes_sent():
    network=psutil.net_io_counters()
    return format_bytes(network.bytes_sent)

def get_bytes_received():
    network=psutil.net_io_counters()
    return format_bytes(network.bytes_recv)
def get_packets_sent():
    network =psutil.net_io_counters()
    return network.packets_sent
def get_packets_received():
    network =psutil.net_io_counters()
    return network.packets_recv

