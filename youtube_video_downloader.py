import yt_dlp
from program_settings import youtube_downloader_settings

# yt_dlp has print by default, so we will use print as well instead of debug_print
# from utilities import debug_print


def download_given_videos():
    videos = get_youtube_videos()
    for video in videos:
        print(f'Downloading video {videos.index(video) + 1} / {len(videos)}')
        download_youtube_video(video)


def download_youtube_video(url, is_max=False, with_audio=False):
    youtube_downloader_options = {
        'format': 'bestvideo',
        'outtmpl': f'{youtube_downloader_settings["youtube_download_path"]}/%(title)s.%(ext)s',
    }

    if with_audio:
        youtube_downloader_options['format'] = 'bestvideo+bestaudio/best'
        if not is_max:
            youtube_downloader_options['format'] = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'

    elif not is_max:
        youtube_downloader_options['format'] = 'bestvideo[height<=1080]'

    try:
        with yt_dlp.YoutubeDL(youtube_downloader_options) as yt:
            yt.download([url])
        print(f'Video downloaded successfully and saved to {youtube_downloader_settings["youtube_download_path"]}')
    except Exception as e:
        print(f'An error occurred while trying to download youtube video: {e}')


def get_youtube_videos():
    with open(youtube_downloader_settings["youtube_video_list_path"], 'r', encoding="utf-8-sig") as videos:
        return [line.strip() for line in videos.readlines()]


# Call the function to download the videos
download_given_videos()
