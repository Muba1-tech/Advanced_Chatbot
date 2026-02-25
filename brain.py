import random

def detect_intent(user_input):
    user_input = user_input.lower()

    study_keywords = ["study", "exam", "learn", "subject", "homework"]
    health_keywords = ["health", "diet", "exercise", "sleep", "fitness"]
    ai_keywords = ["ai", "machine learning", "ml", "artificial intelligence"]

    if any(word in user_input for word in study_keywords):
        return "study"
    elif any(word in user_input for word in health_keywords):
        return "health"
    elif any(word in user_input for word in ai_keywords):
        return "ai"
    else:
        return "general"


def remember_name(user_input, memory):
    user_input = user_input.lower()

    if "my name is" in user_input:
        name = user_input.split("my name is")[-1].strip().title()
        memory["name"] = name
        return f"Nice to meet you, {name}! I will remember your name."
    
    if "what is my name" in user_input:
        if memory.get("name"):
            return f"Your name is {memory['name']}."
        else:
            return "I don't know your name yet. You can tell me by saying 'My name is ___'."
    
    return None


def study_responses():
    responses = [
        "Consistency is the key to effective studying. Try using the Pomodoro technique!",
        "Break your study sessions into small focused intervals for better retention.",
        "Revise regularly and practice active recall for stronger memory.",
        "Make short notes while studying — it improves understanding."
    ]
    return random.choice(responses)


def health_responses():
    responses = [
        "Remember to drink enough water and get 7-8 hours of sleep daily.",
        "Regular exercise and a balanced diet are essential for good health.",
        "Take short breaks and stretch if you study for long hours.",
        "Mental health is as important as physical health — take care of both."
    ]
    return random.choice(responses)


def ai_responses():
    responses = [
        "Artificial Intelligence enables machines to simulate human intelligence.",
        "Machine Learning is a subset of AI that learns from data patterns.",
        "AI is widely used in healthcare, education, and automation systems.",
        "Deep Learning is an advanced branch of Machine Learning using neural networks."
    ]
    return random.choice(responses)


def general_responses():
    responses = [
        "That's interesting! Tell me more.",
        "I'm here to assist you with anything related to study, health, or AI.",
        "Can you elaborate a bit more?",
        "I understand. How can I help you further?"
    ]
    return random.choice(responses)


def generate_response(user_input, memory):
    # Check name memory first (advanced personalization)
    name_memory = remember_name(user_input, memory)
    if name_memory:
        return name_memory

    # Detect intent
    intent = detect_intent(user_input)

    if intent == "study":
        return study_responses()
    elif intent == "health":
        return health_responses()
    elif intent == "ai":
        return ai_responses()
    else:
        return general_responses()