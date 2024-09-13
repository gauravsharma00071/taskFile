import ctypes

"""
here ctype is python module which executes command for recycle bin using try except.

DocString BY;
Gaurav Sharma
"""

def empty_recycle_bin():
    try:
        ctypes.windll.shell32.SHEmptyRecycleBinW(None, None, 1)
        print("Recycle Bin empty successfully.")
    except Exception as e:
        print(f"Error empty Recycle Bin: {e}")

if __name__ == "__main__":
    empty_recycle_bin()
