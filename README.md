# Keeping Track of Channels Activity

This app checks channels in [channels.json](channels.json.example) if they are live or premiering a video.
When live or premiering, it generates a json file for each video stream that
[ytarchive-raw-go](https://github.com/HoloArchivists/ytarchive-raw-go) can run.

## Installation

1. Clone the repository.
2. Install `python3`
3. Install requirements by running `pip install -r requirements.txt`

## Basic Usage

1. Copy [*.example]() files and remove ".example" from their name.
2. Add channel ids to "channels.json" file that you want to check.
3. Other settings can be configured in [const.py](const.py.example).
4. Run `python3 index.py`

---

This README is incomplete.
