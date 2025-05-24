# Define some example FAQs

def get_response(user_input):
    faq_pairs = {
        "what is ai": "AI stands for Artificial Intelligence. It's the simulation of human intelligence in machines.",
        "what is codealpha": "CodeAlpha is a platform that provides internships and hands-on projects for learners.",
        "who are you": "I'm your lovely little FAQ bot created by Akshat.",
        "what is machine learning": "Machine Learning is a subset of AI that allows systems to learn from data.",
        "Hii": "Hello, How can i help you.",
        "thank you": "You're most welcome!",
        "what is deep learning": "Deep Learning is a subset of machine learning involving neural networks with multiple layers.",
        "what is natural language processing": "NLP allows computers to understand, interpret, and respond to human language.",
        "how to apply for codealpha internship": "Visit www.codealpha.tech and fill out the internship application form.",
        "how to submit task": "You need to upload your project to GitHub and submit the link in your WhatsApp group.",
        "what is chatbot": "A chatbot is a program that simulates human conversation using text or voice.",
        "what is neural network": "Neural networks are computing systems inspired by the human brain’s network of neurons.",
        "what is api": "API stands for Application Programming Interface. It allows different software apps to communicate.",
        "what is github": "GitHub is a platform to host and share code repositories online.",
        "what is python": "Python is a popular programming language known for its simplicity and readability.",
        "what is data science": "Data Science is the field of analyzing data to extract useful insights and support decision-making."
    }
    user_input = user_input.lower().strip()

    for question in faq_pairs:
        if question in user_input:
            return faq_pairs[question]
    return "Sorry, I don't know the answer to that yet."

print("Hello! I’m your CodeAlpha FAQ bot. Ask me something (type 'exit' to quit).")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Bot: Bye! Have a great day.")
        break
    response = get_response(user_input)
    print("Bot:", response)