import psutil


def get_memory_usage():
    memory=psutil.virtual_memory()
    return memory.percent

def get_total_memory():
    memory=psutil.virtual_memory()
    return memory.total

def get_used_memory():
    memory=psutil.virtual_memory()
    return memory.used

def get_available_memory():
    memory=psutil.virtual_memory()
    return memory.available

