
import openai
import os
from datetime import datetime

class SimpleLLMChatbot:
    def __init__(self, api_key):
        """Initialize the chatbot with API key"""
        openai.api_key = api_key
        self.conversation_history = []
        
    def get_response(self, user_input):
        """Get response from the LLM"""
        try:
            self.conversation_history.append({
                "role": "user",
                "content": user_input,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            # Create messages for API
            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
            
            # Get response from OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            
            # Extract and store response
            bot_response = response.choices[0].message['content']
            self.conversation_history.append({
                "role": "assistant",
                "content": bot_response,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            return bot_response
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def save_conversation(self, filename="conversation_log.txt"):
        """Save conversation history to file"""
        with open(filename, 'w') as f:
            for message in self.conversation_history:
                f.write(f"[{message['timestamp']}] {message['role']}: {message['content']}\n")
                f.write("-" * 50 + "\n")

# Main program
def main():
    # Get API key from environment variable
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        api_key = input("Please enter your OpenAI API key: ")
    
    # Create chatbot instance
    chatbot = SimpleLLMChatbot(api_key)
    
    print("Simple LLM Chatbot (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        # Get user input
        user_input = input("\nYou: ")
        
        # Check for quit command
        if user_input.lower() in ['quit', 'exit']:
            # Save conversation before exiting
            chatbot.save_conversation()
            print("\nConversation saved to conversation_log.txt")
            print("Goodbye!")
            break
        
        response = chatbot.get_response(user_input)
        print("\nBot:", response)

if __name__ == "__main__":
    main()
