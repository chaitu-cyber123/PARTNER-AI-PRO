class Personality:

    def __init__(self):

        self.name = "Partner"

        self.style = "Professional"

        self.humor = True

        self.proactive = True

        self.explain_reasoning = True

        self.learning = True

    def reply(self, text):

        return text

    def greeting(self):

        return "Hello. How can I help you today?"

    def unknown(self):

        return (
            "I don't know that yet. "
            "Would you like to teach me?"
        )


partner = Personality()

