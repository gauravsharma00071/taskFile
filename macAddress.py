import socket
import platform
import uuid
import subprocess

"""
in this program hostname, serial number and mac address of system to be findout using function 
and python modules for windows. 

DocString By:
Gaurav Sharma
"""
# get hostname function declartion
def get_hostname():
    return socket.gethostname()

# serial number
def get_serial_number():
    system_platform = platform.system()
    serial_number = "Not Available"

    if system_platform == "Windows":
        try:
            result = subprocess.check_output("wmic bios get serialnumber", shell=True)
            serial_number = result.decode().split("\n")[1].strip()
        except Exception as e:
            print(f"Error fetching serial number on Windows: {e}")

    elif system_platform == "Linux":
        pass

    return serial_number
# mac address
def get_mac_address():
    mac_address = None
    if platform.system() == "Windows":
        try:
            result = subprocess.check_output("ipconfig /all", shell=True).decode()
            for line in result.splitlines():
                if "Physical" in line:
                    mac_address = line.split(":")[-1].strip()
                    break
        except Exception as e:
            print(f"Error fetching MAC address on Windows: {e}")

    elif platform.system() == "Linux":
        try:
            pass
        except Exception as e:
            print(f"Error fetching MAC address on Linux: {e}")

    return mac_address or ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0,2*6,2)][::-1])

#calling all function here
def main():
    hostname = get_hostname()
    serial_number = get_serial_number()
    mac_address = get_mac_address()

    print(f"Hostname: {hostname}")
    print(f"Serial Number: {serial_number}")
    print(f"MAC Address: {mac_address}")

if __name__ == "__main__":
    main()
