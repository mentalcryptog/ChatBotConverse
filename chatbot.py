import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi, how can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!", "I'm just a program, but I'm functioning perfectly!"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!"]
    ],
    # More patterns and responses can be added here
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Start chatting
print("Welcome to ChatBotConverse. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("ChatBotConverse: " + response)
