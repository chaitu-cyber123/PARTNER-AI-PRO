from voice import listen, speak
from commands import handle_command
from ai import ask


speak("Hello sir. Partner AI is online. Systems are operational.")


while True:

    command = listen()

    if command == "":
        continue

    if "exit" in command or "shutdown" in command:
        speak("Partner shutting down")
        break

    response = handle_command(command)

    if "I don't understand" in response:
        response = ask(command)

    speak(response)
