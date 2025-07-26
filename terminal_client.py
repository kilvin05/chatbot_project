from chat.chatbot import chatbot

print("Talk to the bot (type 'exit' to stop):")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bot: Goodbye!")
        break

    response = chatbot.get_response(user_input)
    print("Bot:", response)
