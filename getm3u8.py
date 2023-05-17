import re
import utils


def get_m3u8(url):
    try:
        with utils.urlopen(url, use_cookie=False) as response:
            html = response.read().decode()
            regex = r"hlsManifestUrl\":\"([^\"]+)"
            result = re.search(regex, html).group(1)   
    except AttributeError as att_error:
        with utils.urlopen(url, use_cookie=True) as response:
            html = response.read().decode()
            regex = r"hlsManifestUrl\":\"([^\"]+)"
            try:
                result = re.search(regex, html).group(1)
            except AttributeError as att_error:
                print("Result: ", re.search(regex, html))
                print(att_error)
    return result


def get_m3u8_id(m3u8_url):
    regex = r"/id/(.+?)/"
    result = re.search(regex, m3u8_url).group(1)
    return result