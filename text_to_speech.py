from gtts import gTTS

import requests
import textwrap
import base64

from dotenv import dotenv_values
from program_settings import text_to_speech_settings
from utilities import debug_print


def create_text_to_speech(text):
    if text_to_speech_settings["is_tiktok"]:
        tiktok_text_to_speech(text)
    else:
        google_text_to_speech(text)


def google_text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output_sound.mp3")


def tiktok_text_to_speech(text):
    text = text.replace("+", "plus")
    text = text.replace(" ", "+")
    text = text.replace("&", "and")
    text = text.replace("ä", "ae")
    text = text.replace("ö", "oe")
    text = text.replace("ü", "ue")
    text = text.replace("ß", "ss")

    env = dotenv_values(".env")
    tiktok_api_base_url = env.get("TIKTOK_API_BASE_URL")
    tiktok_user_agent = env.get("TIKTOK_USER_AGENT")
    tiktok_session_id = env.get("TIKTOK_SESSION_ID")
    tiktok_voice = text_to_speech_settings["tiktok_voice"]

    textlist = textwrap.wrap(text, width=200, break_long_words=True, break_on_hyphens=False)  # TikTok has a limit of 200 characters per request

    is_first = True
    for text in textlist:
        request = requests.post(
            f"{tiktok_api_base_url}?text_speaker={tiktok_voice}&req_text={text}&speaker_map_type=0&aid=1233",
            headers={
                'User-Agent': tiktok_user_agent,
                'Cookie': f'sessionid={tiktok_session_id}'
            }
        )

        voice_string = [request.json()["data"]["v_str"]][0]
        b64_decoded_binary = base64.b64decode(voice_string)

        write_mode = "wb" if is_first else "ab"
        is_first = False

        with open(text_to_speech_settings["output_sound_file_path"], mode=write_mode) as output_sound_file:
            output_sound_file.write(b64_decoded_binary)

        status_code = [request.json()["status_code"]][0]
        status_message = [request.json()["message"]][0]

        debug_print(f"Status Code: {status_code}, Status Message: {status_message}")
