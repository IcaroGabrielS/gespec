import psutil
import json

def get_ram_info():
    virtual_mem = psutil.virtual_memory()
    swap_mem = psutil.swap_memory()
    
    bytes_to_gb = 1024 ** 3
    
    ram_data = {
        "physical_memory": round(virtual_mem.total / bytes_to_gb, 2), 
        "swap_memory": round(swap_mem.total / bytes_to_gb, 2)}
    
    return ram_data

if __name__ == "__main__":
    print(get_ram_info())