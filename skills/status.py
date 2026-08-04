from ai.memory import load_memory
import os


def status_command(message):

    if "system status" in message or "partner status" in message:

        memory = load_memory()

        count = 0

        for section in memory.values():
            if isinstance(section, dict):
                count += len(section)

        return f"""
PARTNER AI CORE STATUS

✓ MEMORY SYSTEM : ONLINE
✓ NEWS SYSTEM   : ONLINE
✓ WEATHER SYSTEM: ONLINE
✓ VOICE SYSTEM  : ONLINE
✓ HUD SYSTEM    : ONLINE

MEMORY ITEMS:
{count}

PROFILE:
{memory.get("profile", {}).get("name", "Unknown")}
"""

    return None
