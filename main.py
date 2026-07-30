from monitor.system import(
    get_os,
    get_hostname,
    get_python_version,
    get_machine,
    get_processor,
    get_cpu_count,
    get_boot_time
)

print("Linux System Monitor")
print("---------------------")

print("Operating Sytem:" ,get_os())
print("Hostname:" ,get_hostname())
print("Python Version:" ,get_python_version())
print("Machine:" ,get_machine())
print("Processor:" ,get_processor())
print("CPU count:" ,get_cpu_count())
print("Boot time:" ,get_boot_time())

