import re

def converter_command(message):

    text = message.lower().strip()

    m = re.search(r"(\d+(\.\d+)?)\s*km\s*(to|in)\s*miles", text)
    if m:
        km = float(m.group(1))
        return f"{km} km = {km * 0.621371:.2f} miles"

    m = re.search(r"(\d+(\.\d+)?)\s*miles\s*(to|in)\s*km", text)
    if m:
        miles = float(m.group(1))
        return f"{miles} miles = {miles / 0.621371:.2f} km"

    m = re.search(r"(\d+(\.\d+)?)\s*kg\s*(to|in)\s*pounds", text)
    if m:
        kg = float(m.group(1))
        return f"{kg} kg = {kg * 2.20462:.2f} pounds"

    m = re.search(r"(\d+(\.\d+)?)\s*pounds\s*(to|in)\s*kg", text)
    if m:
        pounds = float(m.group(1))
        return f"{pounds} pounds = {pounds / 2.20462:.2f} kg"

    m = re.search(r"(\d+(\.\d+)?)\s*c\s*(to|in)\s*f", text)
    if m:
        c = float(m.group(1))
        return f"{c}°C = {(c * 9/5) + 32:.2f}°F"

    m = re.search(r"(\d+(\.\d+)?)\s*f\s*(to|in)\s*c", text)
    if m:
        f = float(m.group(1))
        return f"{f}°F = {(f - 32) * 5/9:.2f}°C"

    return None

