import os
import datetime
import stat
#This python script is made for macOS, you might have to change a few things if running on WindowsOS or LinuxOS.

# Gets the information about each file in the directory
def get_file_info(root, file_name):
    file_path = os.path.join(root, file_name)
    stat_info = os.stat(file_path)

    # Print all available file information
    print(f"File Information for: {file_path}")
    print(f"  Size: {stat_info.st_size} bytes")
    print(f"  Last Access Time: {datetime.datetime.fromtimestamp(stat_info.st_atime)}")
    print(f"  Last Modification Time: {datetime.datetime.fromtimestamp(stat_info.st_mtime)}")
    
    # Check if the files creation time is available or not
    try:
        creation_time = datetime.datetime.fromtimestamp(stat_info.st_birthtime)
        print(f"  Creation Time: {creation_time}")
    except AttributeError:
        print("  Creation Time: Not available on this file system")

    print("\n")


#  Checks to see if the files in the directory during the os.walk is a .py file. If it is, then it calls to get_file_info function to get the info on the .py file
def find_python_files(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            if file_name.endswith(".py"):
                get_file_info(root, file_name)

# Replace 'PATH-NAME-HERE' with the directory you want to scan
directory_to_scan = 'PATH-NAME-HERE'

find_python_files(directory_to_scan)
