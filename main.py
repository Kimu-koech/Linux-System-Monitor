from monitor.system import(
    get_os,
    get_hostname,
    get_python_version,
    get_machine,
    get_processor,
    get_cpu_count,
    get_boot_time
)

from monitor.cpu import (
    get_cpu_cores,
    get_cpu_frequency,
    get_cpu_usage
)

from monitor.memory import(
    get_memory_usage,
    get_total_memory,
    get_used_memory,
    get_available_memory
)

from monitor.disk import(
    get_disk_usage,
    get_total_disk,
    get_free_disk,
    get_used_disk
)

from monitor.network import (
    get_bytes_sent,get_bytes_received,
    get_packets_sent,get_packets_received
)
from monitor.processes import (
    get_process_count,
    get_process_names,
)
print("=" * 40)
print("Linux System Monitor")
print("=" * 40)
print()
print("SYSTEM INFORMATION")
print("-"*40)


print("Operating Sytem:" ,get_os())
print("Hostname:" ,get_hostname())
print("Python Version:" ,get_python_version())
print("Machine:" ,get_machine())
print("Processor:" ,get_processor())
print("CPU count:" ,get_cpu_count())
print("Boot time:" ,get_boot_time())
print()

print("CPU INFORMATION")
print("-"*40)

print(f"Cpu usage:,{get_cpu_usage()}%")
print("Cpu cores:",get_cpu_cores())
print(f"Cpu frequency:{get_cpu_frequency()}MHZ")
print()


print("MEMORY INFORMATION ")
print("-"*40)
print(f"Memory usage:{get_memory_usage()}%")
print("Total memory:",get_total_memory())
print("Available memory:",get_available_memory())
print("Used memory:",get_used_memory())
print()

print("DISK INFORMATION")
print("-"*40)
print(f"Disk usage:{get_disk_usage()}%")
print("Total disk:",get_total_disk())
print("Used disk:",get_used_disk())
print("Free disk:",get_free_disk())
print()

print("NETWORK INFORMATION")
print("-"*40)
print("Bytes sent:",get_bytes_sent())
print("Bytes received:",get_bytes_received())
print("Packets sent:",get_packets_sent())
print("Packets received:",get_packets_received())
print()

print("PROCESS INFORMATION ")
print("-"*40)
print(f"Running Processes{get_process_count()}")
print("\nFirst 10 running processes:")
for process in get_process_names():
    print(f"-{process}")

    