import random

# Predefined responses
responses = {
    "hello": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! Need any help?"],
    "how are you": ["I'm doing great! Thanks for asking.", "I'm a bot, but I'm functioning perfectly.", "All systems operational!"],
    "your name": ["I'm ChatBot, your virtual assistant!", "Just call me ChatBot.", "ChatBot at your service!"],
    "bye": ["Goodbye! Have a great day!", "See you soon!", "Bye! Take care."],
    "weather": ["I can't check the weather, but you could try an online forecast!", "It’s always sunny in the digital world!"],
    "hobbies": ["I enjoy chatting and helping people like you!", "My hobby is processing data and making conversations fun."],
    "favorite color": ["I love all colors equally. What about you?", "I’d say binary black and white are my favorites!"],
    "age": ["I'm as young as the latest software update!", "Age doesn't matter when you're a chatbot!"],
    "help": ["I can chat with you, tell jokes, and more. Ask me anything!", "Sure! What do you need help with?"],
    "joke": ["Why did the programmer quit his job? He didn’t get arrays!", "Why do Java developers wear glasses? Because they don’t see sharp!"],
    "default": ["I didn't quite catch that. Could you rephrase?", "Hmm, I'm not sure about that. Try asking something else!"]
}


def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return random.choice(responses["default"])

def chat():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("🤖 ChatBot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"🤖 ChatBot: {response}")


chat()
