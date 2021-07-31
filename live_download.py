import subprocess
import const

def download(video_id):
    setDownloaded = False
    command_list = ['lxterminal', '-e', 'python3']
    command_list += ['ytarchive.py', '-o',
                     const.DOWNLOAD,
                     '--add-metadata', '-t', '--vp9', '--write-description', '--write-thumbnail', '--threads', '2',
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
