from monitor.utils import format_bytes
import psutil

def get_memory_usage():
    memory=psutil.virtual_memory()
    return format_bytes(memory.percent)

def get_total_memory():
    memory=psutil.virtual_memory()
    return format_bytes(memory.total)

def get_used_memory():
    memory=psutil.virtual_memory()
    return format_bytes(memory.used)

def get_available_memory():
    memory=psutil.virtual_memory()
    return format_bytes(memory.available)

