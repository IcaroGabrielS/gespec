import json
import screeninfo

def get_simple_monitor_info():
    
    try:
        monitors = screeninfo.get_monitors()
    except screeninfo.common.ScreenInfoError as e:
        return {"error": "Could not retrieve monitor information.", "details": str(e)}

    if not monitors:
        return {"status": "No active monitors found."}

    for monitor in monitors:
        info = {"device_name": monitor.name, "resolution": f"{monitor.width}x{monitor.height}"}
        return info


if __name__ == "__main__":
    print(get_simple_monitor_info())