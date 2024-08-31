def chatbot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but I'm functioning as expected. How can I help you?"
    elif "your name" in user_input:
        return "I am your friendly chatbot, here to assist you."
    elif "what can you do" in user_input:
        return "I can help you with basic queries and provide information. What would you like to know?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm sorry, I didn't understand that. Could you please rephrase your question?"

while True:
    user_input = input("You: ")
    
    response = chatbot_response(user_input)
    
    print(f"Chatbot: {response}")
    
    if "bye" in user_input.lower() or "goodbye" in user_input.lower():
        break

