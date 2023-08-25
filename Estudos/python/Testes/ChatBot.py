import random

# Define patterns and responses
patterns = {
    "hello": ["Hi there!", "Hello!", "Hey!"],
    "how are you": ["I'm good, thank you!", "I'm doing well.", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def get_response(user_input):
    for pattern, responses in patterns.items():
        if pattern in user_input.lower():
            return random.choice(responses)
    return "I'm sorry, I don't understand that."

def main():
    print("Chatbot: Hi! I'm a simple chatbot. How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
