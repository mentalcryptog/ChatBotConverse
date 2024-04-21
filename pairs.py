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
        r"what's your name ?",
        ["You can call me ChatBotConverse.", "I'm just a chatbot, so you can call me ChatBotConverse."]
    ],
    [
        r"who created you ?",
        ["I was created by a developer.", "I'm a product of programming magic!"]
    ],
    [
        r"tell me a joke|jokes",
        ["Why don't scientists trust atoms? Because they make up everything!", 
         "Parallel lines have so much in common. It's a shame they'll never meet."]
    ],
    [
        r"(.*) (location|city) ?",
        ["I'm a virtual entity, so I don't have a physical location.", "I exist in the digital realm."]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!"]
    ],
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Start chatting
print("Welcome to ChatBotConverse. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    response = chatbot.respond(user_input)
    print("ChatBotConverse: " + response)
