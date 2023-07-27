import subprocess
import os
import const


def download(files):
    for file in reversed(files):
        if '.json' in file:
            file_path = os.getcwd() + '\\' + file
            command_list = ['start', f'ytarchive-raw-go {file[6:-5]}', '/min', 'cmd', '/k', 'ytarchive-raw-go.exe', '-t', str(const.PRIVATED_DOWNLOAD_THREADS)]
            command_list += ['-i', file_path, '-o', const.PRIVATED_DOWNLOAD]
            # command_list = f'start cmd /k ytarchive-raw-go -t {const.PRIVATED_DOWNLOAD_THREADS} -i "{file_path} -o {const.PRIVATED_DOWNLOAD}"'
            try:
                print(f"[INFO] Downloading Privated Video {file}")
                output = subprocess.run(command_list, shell=True, start_new_session=True)
                # If theres an error then this ensures a redownload, but only works if the program crashes by itself immediately
                # print("[Debug] Immediate Return Code:", output.returncode)
            except Exception as e:
                print('[ERROR]', e)
                print("[INFO] Retry Download")
                output = subprocess.run(command_list)
            finally:
                continue

