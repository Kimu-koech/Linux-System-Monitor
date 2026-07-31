import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_cpu_cores():
    return psutil.cpu_count(logical=False)

def get_cpu_frequency():
    frequency=psutil.cpu_freq()

    if frequency:
        return frequency.current
    else:
        return None

