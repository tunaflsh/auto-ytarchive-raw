import utils

def get_private_check_text(status, video_id=None):
    # import getjson
    # with utils.build_req(video_id) as res:
    #     html = res.read().decode()
    # info = getjson.get_youtube_video_info(html)
    # # Do some if-else using info object

    if status is utils.PlayabilityStatus.PRIVATED:
        return "[{video_id}](https://youtu.be/{video_id}) is privated on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.REMOVED:
        return "[{video_id}](https://youtu.be/{video_id}) is removed on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.COPYRIGHTED:
        return "[{video_id}](https://youtu.be/{video_id}) is copyrighted on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.UNKNOWN:
        return "[{video_id}](https://youtu.be/{video_id}) occurred sth weird on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.MEMBERS_ONLY:
        return "[{video_id}](https://youtu.be/{video_id}) is member-only on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.LOGIN_REQUIRED:
        return "[{video_id}](https://youtu.be/{video_id}) requires login to watch on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    elif status is utils.PlayabilityStatus.OFFLINE: # Should not be here though. But I do dumb things.
        return "[{video_id}](https://youtu.be/{video_id}) offlined on [{channel_name}](https://www.youtube.com/channel/{channel_id})."
    else:
        return "[{video_id}](https://youtu.be/{video_id}) occurred sth very weird on [{channel_name}](https://www.youtube.com/channel/{channel_id})."

def get_onlive_message(video_id):
    return "[{video_id}](https://youtu.be/{video_id}) is live on [{channel_name}](https://www.youtube.com/channel/{channel_id})!"

MULTI_MANIFEST_MESSAGE = "[{video_id}](https://youtu.be/{video_id}) has multiple manifest on [{channel_name}](https://www.youtube.com/channel/{channel_id})!"

PUSHALERT_TITLE = "🔴 Hololive Live Alert"
PUSHALERT_MESSAGE = "{channelName} is Live now!"

FCM_TITLE = "🔴 {channelName}"
FCM_MESSAGE = "{title}"