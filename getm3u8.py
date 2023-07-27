import re
import utils


def get_m3u8(url):
    use_cookie=False
    try:
        with utils.urlopen(url, use_cookie=use_cookie) as response:
            html = response.read().decode()
            regex = r"hlsManifestUrl\":\"([^\"]+)"
            result = re.search(regex, html).group(1)   
    except AttributeError:
        use_cookie=True
        with utils.urlopen(url, use_cookie=use_cookie) as response:
            html = response.read().decode()
            regex = r"hlsManifestUrl\":\"([^\"]+)"
            try:
                result = re.search(regex, html).group(1)
            except AttributeError as att_error:
                print(f"[ERROR] {att_error}")
    return result, use_cookie


def get_m3u8_id(m3u8_url):
    regex = r"/id/(.+?)/"
    result = re.search(regex, m3u8_url).group(1)
    return result