import subprocess
import os

def download(files):
    for file in reversed(files):
        if '.json' in file:
            file = os.getcwd() + '\\' + file
            command_list = f'start cmd /k ytarchive-raw-go -t 12 -i "{file}"'
            try:
                print("[INFO] Downloading Video")
                output = subprocess.run(command_list, shell=True)
                # If theres an error then this ensures a redownload, but only works if the program crashes by itself immediately
                # print("[Debug] Output: ", output)
                print("[Debug] Immediate Return Code:", output.returncode)
            except Exception as e:
                print("[INFO] Retry Download")
                output = subprocess.run(command_list)

