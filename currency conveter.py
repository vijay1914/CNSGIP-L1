import random

# Define possible user inputs and corresponding bot responses
responses = {
    "hi": "Hello!",
    "how are you?": "I'm good, thank you.",
    "what's your name?": "I'm a chatbot. What's yours?",
    "default": "I'm sorry, I don't understand.",
}

def respond(message):
    # Check if the message is in the responses
    if message.lower() in responses:
        return responses[message.lower()]
    else:
        return responses["default"]

# Main loop to run the chatbot
print("Welcome! Ask me something or say hi to start.")

while True:
    user_input = input("You: ").strip()
    
    # Check for exit command
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    
    # Generate a response
    bot_response = respond(user_input)
    print("Bot:", bot_response)

