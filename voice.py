import subprocess


def speak(text):
    print("Partner:", text)
    subprocess.run(
        ["termux-tts-speak", text]
    )


def listen():
    print("Partner is listening...")

    result = subprocess.check_output(
        ["termux-speech-to-text"]
    ).decode().strip()

    print("You:", result)

    return result.lower()
