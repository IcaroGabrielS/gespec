import os
import platform
from colorama import init, Fore, Style
from cpuGetter import get_cpu_summary
from gpuGetter import get_gpu_name
from ramGetter import get_ram_info
from videoGetter import get_simple_monitor_info

init(autoreset=True)

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def print_section_title(title):
    print(f"\n{Fore.CYAN}{Style.BRIGHT}{title}")

def print_info(label, value):
    if value is not None and value != "":
        print(f"{Fore.GREEN}{label}: {Fore.WHITE}{value}")

def display_cpu_info():
    cpu_info = get_cpu_summary()
    print_section_title("CPU INFORMATION")
    print_info("Processor", cpu_info.get("processor_brand"))
    print_info("Operating System", cpu_info.get("system"))
    print_info("Physical Cores", cpu_info.get("physical_cores"))
    print_info("Total Threads", cpu_info.get("total_cores"))
    
    max_freq = cpu_info.get("max_frequency_mhz")
    if max_freq:
        print_info("Maximum Frequency", f"{max_freq/1000:.2f} GHz")
    
    min_freq = cpu_info.get("min_frequency_mhz")
    if min_freq:
        print_info("Minimum Frequency", f"{min_freq/1000:.2f} GHz")
# ------------------------------------------------------------------------------------------
def display_gpu_info():
    gpu_names = get_gpu_name()
    print_section_title("GPU INFORMATION")
    
    if not gpu_names:
        print(f"{Fore.RED}No GPU detected.")
        return
        
    for i, gpu in enumerate(gpu_names, 1):
        print_info(f"GPU {i}", gpu)
# ------------------------------------------------------------------------------------------
def display_ram_info():
    ram_info = get_ram_info()
    print_section_title("MEMORY INFORMATION")
    print_info("RAM Memory", f"{ram_info.get('physical_memory')} GB")
    print_info("Swap Memory", f"{ram_info.get('swap_memory')} GB")
# ------------------------------------------------------------------------------------------
def display_monitor_info():
    monitor_info = get_simple_monitor_info()
    print_section_title("MONITOR INFORMATION")
    
    if "error" in monitor_info:
        print(f"{Fore.RED}{monitor_info['error']}")
        return
    
    print_info("Monitor Name", monitor_info.get("device_name"))
    print_info("Resolution", monitor_info.get("resolution"))
# ------------------------------------------------------------------------------------------
def main():
    clear_screen()
    system_name = platform.node() or "System"
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}GESPEC - Hardware: {system_name}")
    
    display_cpu_info()
    display_gpu_info()
    display_ram_info()
    display_monitor_info()

if __name__ == "__main__":
    main()