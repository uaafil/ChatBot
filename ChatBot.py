import openai

# Set your OpenAI API key
openai.api_key = "OPENAI_API_KEY"

# Initial message to start the conversation
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me a joke."},
]

# Continuously interact with the chatbot
print("Chatbot: Hi there! I'm here to help. What can I assist you with?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break

    # Append user input to the conversation
    conversation.append({"role": "user", "content": user_input})

    # Use GPT-3 to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the latest model name
        messages=conversation
    )

    # Extract and print the chatbot's response
    chatbot_response = response['choices'][0]['message']['content']
    print("Chatbot:", chatbot_response)

    # Append chatbot response to the conversation
    conversation.append({"role": "assistant", "content": chatbot_response})
