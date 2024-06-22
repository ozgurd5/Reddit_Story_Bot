import yt_dlp
from program_settings import youtube_downloader_settings


def download_youtube_video(url, with_audio=False):
    youtube_downloader_options = {
        'format': 'bestvideo',
        'outtmpl': f'{youtube_downloader_settings["youtube_download_path"]}/%(title)s.%(ext)s',
    }

    if with_audio:
        youtube_downloader_options['format'] = 'bestvideo+bestaudio/best'

    try:
        with yt_dlp.YoutubeDL(youtube_downloader_options) as yt:
            yt.download([url])
        print(f'Video downloaded successfully and saved to {youtube_downloader_settings["youtube_download_path"]}')
    except Exception as e:
        print(f'An error occurred while trying to download youtube video: {e}')
