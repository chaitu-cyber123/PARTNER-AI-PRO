from brain.cortex import think

while True:

    message = input("You: ")

    if message.lower() == "exit":
        break

    print()

    print("Partner:")

    print(think(message))

    print()
