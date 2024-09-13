import subprocess
import json

"""In this program a function make for finding all software installed in this system by command for windows
DocString BY:
Gaurav Sharma
"""
def get_installed_software_windows():
    try:
        command = 'powershell "Get-WmiObject -Class Win32_Product|Select-Object -Property Name, Version| ConvertTo-Json"'
        result = subprocess.check_output(command, shell=True, text=True)
        software_list = json.loads(result)
        return software_list
    except Exception as e:
        print(f"Error fetching installed software on Windows: {e}")
        return []

def main():
    software = get_installed_software_windows()
    print("Installed Software on Windows:")
    for item in software:
        print(f"Software Name: {item['Name']}, Version: {item['Version']}")

if __name__ == "__main__":
    main()
