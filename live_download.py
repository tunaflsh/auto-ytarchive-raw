import subprocess
import const

def download(video_id):
    setDownloaded = False
    # Download if download process hasn't already been initiated
    # change back to /k
    command_list = ['start', 'cmd', '/k']
    command_list += ['ytarchive.exe', '-o',
                     const.DOWNLOAD,
                     '--add-metadata', '-t', '--vp9', '--write-description', '--write-thumbnail', '--threads', '2',
                     '-w']
    command_list += [f'https://www.youtube.com/watch?v={video_id}', 'best']

    try:
        print("Downloading Live Stream")
        output = subprocess.run(command_list, check=True, shell=True)
        # If theres an error then this ensures a redownload, but only works if the program crashes by itself immediately
        print("[Debug]Output: ", output)
        print("[Debug]Return Code:", output.returncode)
        if output.returncode != 0:
            setDownloaded = False
        setDownloaded = True
    except Exception as e:
        print(e)
        setDownloaded = False

    return setDownloaded