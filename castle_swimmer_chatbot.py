import nltk
from nltk.tokenize import word_tokenize


nltk.download('punkt')

def chatbot_response(user_input):
    # Tokenize the user input
    tokens = word_tokenize(user_input.lower())
    

    if "castle swimmer" in tokens or "about" in tokens:
        return "Castle Swimmer is about a young swimmer who embarks on a journey filled with mystery and adventure in a fantastical underwater world."
    elif "main characters" in tokens or "characters" in tokens:
        return "The main characters include the brave swimmer and various mystical creatures he encounters on his journey."
    elif "who" in tokens:
        return "The story follows a young swimmer who discovers a new prophecy that changes his destiny."
    else:
        return "I'm sorry, I don't have information on that. Can you ask something else?"

def chat():
    print("Welcome to the Castle Swimmer Chatbot! Ask me anything about 'Castle Swimmer'. (type 'Done' to exit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'done' or user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

# Start the chat
if __name__ == "__main__":
    chat()
