import math
import re

def calculator_command(message):
    message = message.lower().strip()

    # Remove common words
    for word in ["calculate", "what is", "solve"]:
        message = message.replace(word, "").strip()

    # Replace symbols
    message = message.replace("^", "**")
    message = message.replace("x", "*")

    # Allow only safe characters
    if not re.fullmatch(r"[0-9+\-*/(). %*a-zA-Z]+", message):
        return None

    try:
        result = eval(
            message,
            {"__builtins__": None},
            {
                "sqrt": math.sqrt,
                "pow": pow,
                "abs": abs,
                "round": round
            }
        )

        return f"The answer is {result}."

    except Exception:
        return None
