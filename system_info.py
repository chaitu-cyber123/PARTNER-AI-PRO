import subprocess
import datetime


def system_status():

    time = datetime.datetime.now().strftime("%I:%M %p")
    date = datetime.datetime.now().strftime("%d %B %Y")

    try:
        battery = subprocess.check_output(
            ["termux-battery-status"]
        ).decode()

        return f"""
Partner System Status:
Time: {time}
Date: {date}
Battery: {battery}
All systems operational.
"""

    except:
        return f"""
Partner System Status:
Time: {time}
Date: {date}
Battery information unavailable.
All systems operational.
"""
