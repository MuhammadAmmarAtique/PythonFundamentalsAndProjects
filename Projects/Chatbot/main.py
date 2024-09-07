# Chatbot using Python

print("Welcome to Ammmar's Chabot, Ask any question!")

# dictionary containing questions & answers as a key value pair
qna = {
    "hi": "Hey!",
    "What is your name?": "I am ChatGPT, your virtual assistant.",
    "How are you?": "I'm just a program, but I'm here and ready to help you!",
    "What can you do?": "I can assist with various tasks such as answering questions, providing information, and more.",
    "Tell me a joke.": "Why don't scientists trust atoms? Because they make up everything!",
    "What is the capital of France?": "The capital of France is Paris.",
    "Who wrote 'Pride and Prejudice'?": "Jane Austen wrote 'Pride and Prejudice'.",
    "What is the weather like today?": "I can't provide real-time updates, but you can check a weather website or app for current conditions.",
    "How old are you?": "I was created by OpenAI and have been evolving with updates since my initial release.",
    "Can you help me with my homework?": "Sure, I can help answer questions or provide explanations. What subject are you working on?",
    "What is the meaning of life?": "The meaning of life can be different for everyone. Many people find meaning in relationships, accomplishments, and personal growth.",
    "How do you work?": "I use artificial intelligence and natural language processing to understand and respond to your questions.",
    "What is 2 + 2?": "2 + 2 equals 4.",
    "Who is the president of the United States?": "As of my last update, Joe Biden is the president of the United States.",
    "Can you recommend a movie?": "Sure! If you like science fiction, you might enjoy 'Inception'. If you prefer a comedy, try 'The Grand Budapest Hotel'.",
    "How do I cook pasta?": "To cook pasta, bring a pot of water to a boil, add salt, then add the pasta. Cook for the time indicated on the package, usually around 8-12 minutes, then drain.",
    "What is artificial intelligence?": "Artificial intelligence is the simulation of human intelligence processes by machines, especially computer systems.",
    "What is your favorite color?": "I don't have preferences, but blue is often a favorite among many people!",
    "Can you speak other languages?": "Yes, I can understand and respond in several languages. What language would you like to communicate in?",
    "What is the largest planet in our solar system?": "The largest planet in our solar system is Jupiter."
}

# Creating an infinite loop to take input from user unlimited times
while True:
    UserQuestion = input()

    if UserQuestion.lower() == "quit":  # If user writes quit, end conversation with chatbot
        break
    elif UserQuestion in qna:  # Check if the user question is in the dictionary keys
        print(qna[UserQuestion])
    else:
        print("Sorry, no info about this!")
