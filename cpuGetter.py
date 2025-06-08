import platform
import psutil
import cpuinfo
import json

def get_cpu_summary():
    info = {}

    try:
        info["processor_brand"] = cpuinfo.get_cpu_info().get('brand_raw', 'N/A')
    except Exception:
        info["processor_brand"] = None

    try:
        info["system"] = platform.system()
    except Exception:
        info["system"] = None

    try:
        info["physical_cores"] = psutil.cpu_count(logical=False)
        info["total_cores"] = psutil.cpu_count(logical=True)
    except Exception:
        info["physical_cores"] = None
        info["total_cores"] = None

    try:
        cpu_freq = psutil.cpu_freq()
        info["max_frequency_mhz"] = cpu_freq.max
        info["min_frequency_mhz"] = cpu_freq.min
    except Exception:
        info["max_frequency_mhz"] = None
        info["min_frequency_mhz"] = None
        
    return info

if __name__ == "__main__":
    print(get_cpu_summary())