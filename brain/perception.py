from core.intent import detect_intent


def perceive(message):

    return {

        "message": message,

        "intent": detect_intent(message),

        "confidence": 100

    }
