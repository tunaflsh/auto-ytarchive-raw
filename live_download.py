import subprocess


def download(video_id, fetchDownload):
    command_list = ['lxterminal', '-e', 'python3']
    command_list += ['ytarchive.py', '-o',
                     "/media/pi/Samsung256/NoArchive/%(channel)s/%(upload_date)s - %(title)s/%(upload_date)s - %(title)s (%(id)s)",
                     '--add-metadata', '-t', '--vp9', '--write-description', '--write-thumbnail', '--threads', '2',
                     '-w']
    command_list += [f'https://www.youtube.com/watch?v={video_id}', 'best']

    try:
        print("[INFO] Downloading Live Stream")
        output = subprocess.run(command_list)
        # If theres an error then this ensures a redownload, but only works if the program crashes by itself immediately
        # print("[Debug] Output: ", output)
        print("[Debug] Return Code:", output.returncode)
        if output.returncode != 0:
            fetchDownload = False
    except Exception as e:
        print(e)
        fetchDownload = False
