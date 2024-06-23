import subprocess
from program_settings import program_settings


# todo: non nvidia and cuda support
def crop_video_to_9_16(input_path, output_path, with_audio=False):
    command = [
        'ffmpeg',
        '-hwaccel', 'cuda',  # Enable CUDA hardware acceleration
        '-i', input_path,
        '-vf', 'crop=ih*9/16:ih',
        '-c:v', 'h264_nvenc',  # Use NVENC encoder
        '-preset', 'slow',
        '-cq', '30',  # Constant Quality (CQ) mode with a lower value for higher quality
        output_path
    ]

    # todo: probably won't work
    if with_audio:
        command.insert(-1, '-c:a')
        command.insert(-1, 'aac')
        command.insert(-1, '-b:a')
        command.insert(-1, '192k')

    if program_settings["has_debug"]:
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True) as process:
            for line in process.stdout:
                print(line, end='')


# todo: standalone
input_path = "gameplay_footage/gta_v/Satisfying GTA 5 MEGA RAMP Gameplay ▸ No Copyright Gameplay ｜ GTA Gameplay for TikTok ｜ 4K ｜ 622.webm"
output_path = "output_test.mp4"
crop_video_to_9_16(input_path, output_path)
