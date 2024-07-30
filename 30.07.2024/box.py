import random

responses = [
    "Hello! How can I help you?",
    "Hi there! What's up?",
    "Hey! What can I do for you?"
]

def chatbot_response(user_input):
    return random.choice(responses)

print(chatbot_response("Hi"))
