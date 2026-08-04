import os


def speak(text):

    try:
        os.system(
            f'termux-tts-speak "{text}"'
        )

    except Exception as e:
        print("VOICE ERROR:", e)
