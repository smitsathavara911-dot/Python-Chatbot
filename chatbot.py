
print("================================")
print("     WELCOME TO PYTHON BOT")
print("================================")

print("Bot: Hello! Welcome.")
print("Bot: You can talk with me.")
print("Bot: Type bye to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "hi":
        print("Bot: Hello! How are you?")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "what is your name":
        print("Bot: My name is Python Bot.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")
