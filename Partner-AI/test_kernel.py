from kernel.kernel import kernel

while True:

    message = input("You: ")

    if message == "exit":
        break

    print()

    print(kernel.run(message))

    print()
