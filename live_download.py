import subprocess
import const
import os

def download(video_id):
    # My personal use set ytarchive path to whatever you have it to
    fileFound = os.path.isfile('/home/pi/go/bin/ytarchive')
    if not fileFound:
        if os.path.isfile('ytarchive'):
            ytarchive_path = 'ytarchive'
        elif os.path.isfile('ytarchive.py'):
            ytarchive_path = 'ytarchive.py'
    if fileFound:
        ytarchive_path = '/home/pi/go/bin/ytarchive'
    setDownloaded = False
    command_list = ['lxterminal', '-e']
    command_list += [ytarchive_path, '-o',
                     const.DOWNLOAD,
                     '--add-metadata', '-t', '--ipv6', '--vp9', '--write-description', '--write-thumbnail', '--threads', '1',
                     '-w']
    command_list += [f'https://www.youtube.com/watch?v={video_id}', 'best']

    try:
        print("[INFO] Downloading Live Stream")
        output = subprocess.run(command_list)
        # If theres an error then this ensures a redownload, but only works if the program crashes by itself immediately
        # print("[Debug] Output: ", output)
        print("[Debug] Immediate Return Code:", output.returncode)
        if output.returncode != 0:
            setDownloaded = False
        setDownloaded = True
    except Exception as e:
        print(e)
        setDownloaded = False

    return setDownloaded
