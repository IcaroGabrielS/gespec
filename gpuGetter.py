import platform
import subprocess

try:
    import GPUtil
except ImportError:
    GPUtil = None

try:
    import WMI
except ImportError:
    WMI = None

def get_gpu_name():
    gpu_names_list = []
    
    if GPUtil:
        try:
            gpus = GPUtil.getGPUs()
            if gpus:
                for gpu in gpus:
                    gpu_names_list.append(gpu.name)
                return gpu_names_list
        except Exception:
            pass
    
    system = platform.system()

    if system == "Windows":
        if WMI is None:
            return ["Error: The 'WMI' library is not installed. Please run: pip install WMI"]
        try:
            wmi_obj = WMI.WMI()
            for controller in wmi_obj.Win32_VideoController():
                gpu_names_list.append(controller.Name)
            return gpu_names_list
        except Exception as e:
            return [f"Error: Failed to query WMI. Details: {str(e)}"]

    elif system == "Linux":
        try:
            result = subprocess.run(['lspci'], stdout=subprocess.PIPE, text=True)
            for line in result.stdout.splitlines():
                if "VGA compatible controller" in line or "Display controller" in line:
                    gpu_name = line.split(': ', 1)[1]
                    gpu_names_list.append(gpu_name)
            return gpu_names_list
        except (FileNotFoundError, Exception) as e:
            return [f"Error: Failed to run 'lspci'. Details: {str(e)}"]
            
    if not gpu_names_list:
        return ["Error: Could not determine GPU information on this platform."]
    
    return gpu_names_list

if __name__ == "__main__":
    gpu_names = get_gpu_name()
    if gpu_names:
        for name in gpu_names:
            print(name)