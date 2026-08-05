import psutil
from monitor.utils import format_bytes

def get_disk_usage():
    disk=psutil.disk_usage("/")
    return disk.percent

def get_total_disk():
    disk=psutil.disk_usage("/")
    return format_bytes(disk.total)

def get_used_disk():
    disk=psutil.disk_usage("/")
    return format_bytes(disk.used)
def get_free_disk():
    disk=psutil.disk_usage("/")
    return format_bytes(disk.free)





                           
                           