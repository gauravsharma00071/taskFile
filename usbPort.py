import winreg

"""
in this code first i reached to the services of usb port then check usb port which accepted any signal 
if port is blocked successfully then it will print a message

DocString By 
Gaurav Sharma
"""


def block_usb_ports():
    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SYSTEM\CurrentControlSet\Services\USBSTOR", 0,
                                 winreg.KEY_WRITE)
        winreg.SetValueEx(reg_key, "Start", 0, winreg.REG_DWORD, 4)
        winreg.CloseKey(reg_key)

        print("USB ports have been blocked.")
    except Exception as e:
        print(f"Error blocking USB ports: {e}")


if __name__ == "__main__":
    block_usb_ports()
