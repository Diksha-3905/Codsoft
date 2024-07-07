import re
from datetime import datetime

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Predefined responses
    if re.search(r'\bhello\b|\bhi\b', user_input):
        return "Hello! How can I help you today?"
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just a bot, but I'm doing great! How about you?"
    elif re.search(r'\bwhat is your name\b', user_input):
        return "I am a simple chatbot created to assist you."
    elif re.search(r'\bwhat time is it\b|\bwhat is the time\b|\btell me the time\b', user_input):
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif re.search(r'\bwhat is the date\b|\btell me the date\b|\bwhat date is it\b', user_input):
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
    elif re.search(r'\bwhere are you doing your internship at\b', user_input):
        return "I am doing my internship at CodSoft."
    elif re.search(r'\bhow is it going\b', user_input):
        return "Very nice, I am enjoying it."
    elif re.search(r'\bwhat is your favorite color\b', user_input):
        return "I don't have a favorite color, but I like the color of the sky!"
    elif re.search(r'\bwho created you\b', user_input):
        return "I was created by a programmer using Python."
    elif re.search(r'\bwhat can you do\b', user_input):
        return "I can chat with you and answer basic questions about time, date, and more!"
    elif re.search(r'\btell me a joke\b', user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif re.search(r'\bwhat is the capital of france\b', user_input):
        return "The capital of France is Paris."
    elif re.search(r'\bwho is the president of the united states\b', user_input):
        return "As of my last update, the President of the United States is Joe Biden."
    elif re.search(r'\bwhat is the largest mammal\b', user_input):
        return "The largest mammal is the blue whale."
    elif re.search(r'\bwhat is the square root of (\d+)\b', user_input):
        number = int(re.search(r'\bwhat is the square root of (\d+)\b', user_input).group(1))
        return f"The square root of {number} is {number ** 0.5:.2f}."
    elif re.search(r'\bbye\b|\bgoodbye\b', user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop to interact with the chatbot
def chat():
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        if re.search(r'\bbye\b|\bgoodbye\b', user_input.lower()):
            break

# Start the chat
chat()
