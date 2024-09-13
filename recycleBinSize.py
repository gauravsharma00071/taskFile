import os

"""for finding values of recycle bin size implementatin using list comphresion and for loop
DocString By:
Gaurav Sharma
"""

def get_recycle_bin_size_windows():
    drives = [f"{d}\\" for d in os.popen("wmic logicaldisk get caption").read().split() if d]
    total_size = 0

    for drive in drives:
        recycle_bin_path = os.path.join(drive, "$Recycle.Bin")
        if os.path.exists(recycle_bin_path):
            for foldername, subfolders, filenames in os.walk(recycle_bin_path):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    total_size += os.path.getsize(filepath)

    return total_size


def main():
    size_bytes = get_recycle_bin_size_windows()
    print(f"Recycle Bin size: {size_bytes / (1024 * 1024):.2f} MB")


if __name__ == "__main__":
    main()
