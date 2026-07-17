import subprocess
import time

print("Partner Action Service Started...")

while True:
    try:
        with open("action.txt", "r") as f:
            command = f.read().strip()

        if command:

            if command == "youtube":
                subprocess.run([
                    "am",
                    "start",
                    "-a",
                    "android.intent.action.MAIN",
                    "-n",
                    "com.google.android.youtube/com.google.android.apps.youtube.app.WatchWhileActivity"
                ])

            elif command == "chrome":
                subprocess.run([
                    "am",
                    "start",
                    "-a",
                    "android.intent.action.MAIN",
                    "-p",
                    "com.android.chrome"
                ])

            with open("action.txt", "w") as f:
                f.write("")

    except Exception:
        pass

    time.sleep(1)
