import platform
import socket
import sys
import psutil
from datetime import datetime


def get_os():
    return platform.system()


def get_hostname():
    return socket.gethostname()


def get_python_version():
    return f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"


def get_machine():
    return platform.machine()


def get_processor():
    return platform.processor()


def get_cpu_count():
    return psutil.cpu_count()


def get_boot_time():
    return datetime.fromtimestamp(psutil.boot_time())
