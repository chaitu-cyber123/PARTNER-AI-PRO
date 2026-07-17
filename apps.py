import subprocess

APPS = {
    "youtube": "com.google.android.youtube",
    "chrome": "com.android.chrome",
    "whatsapp": "com.whatsapp",
    "settings": "com.android.settings",
    "gmail": "com.google.android.gm"
}
import subprocess

def open_app(name):
    if name.lower() != "youtube":
        return "Only testing YouTube."

    result = subprocess.run(
        [
            "am",
            "start",
            "-a",
            "android.intent.action.MAIN",
            "-n",
            "com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity"
        ],
        capture_output=True,
        text=True
    )

    return (
        f"Return code: {result.returncode}\n"
        f"STDOUT:\n{result.stdout}\n"
        f"STDERR:\n{result.stderr}"
    )
