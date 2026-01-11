import google.generativeai as genai

print("🔥 THIS FILE IS RUNNING 🔥")

# Configure Gemini API
genai.configure(api_key="api_ley")

model = genai.GenerativeModel("gemini-2.5-flash")

def chat_with_gemini():
    print("Chatbot (Gemini 2.5 Flash). Type 'exit' to end the conversation.")
    
    while True:  # Infinite loop for continuous interaction
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Ending the conversation. Goodbye!")
            break
        
        response = model.generate_content(user_input)  # Send user input to the model
        print("Chatbot:", response.text)

if __name__ == "__main__":
    chat_with_gemini()

