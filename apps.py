import subprocess

APPS = {
    "youtube": "com.google.android.youtube",
    "chrome": "com.android.chrome",
    "whatsapp": "com.whatsapp",
    "settings": "com.android.settings",
    "gmail": "com.google.android.gm"
}

def open_app(name):
    name = name.lower()

    if name not in APPS:
        return "I couldn't find that app."

    package = APPS[name]

    try:
        subprocess.run([
            "am",
            "start",
            "-a",
            "android.intent.action.MAIN",
            "-c",
            "android.intent.category.LAUNCHER",
            "-p",
            package
        ], check=True)

        return f"Opening {name}."

    except Exception as e:
        return f"Failed to open {name}: {e}"
