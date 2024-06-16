from utilities import debug_print
from reddit import get_random_text_from_reddit
import moviepy.editor as moviepy


def main():
    text = get_random_text_from_reddit()
    debug_print(text)

    clip = moviepy.VideoFileClip("gameplay_footage/subway_surfers.mp4")
    subclip = clip.subclip(20, 50)

    txt_clip = moviepy.TextClip(text, fontsize=20, color='white')
    txt_clip = txt_clip.set_position(("center", "center")).set_duration(10)

    final_clip = moviepy.CompositeVideoClip([subclip, txt_clip])
    final_clip.write_videofile("output.mp4")


# Call the main function
main()
