import datetime
import random
import math

def handle_command(user_input):
    user_input = user_input.lower().strip()

    # ⏰ Time Command
    if "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # 📅 Date Command
    if "date" in user_input or "today" in user_input:
        today_date = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Today's date is {today_date}."

    # 💪 Motivation Command
    if "motivate" in user_input or "motivation" in user_input:
        quotes = [
            "Believe in yourself. You are capable of amazing things!",
            "Small daily progress leads to big success.",
            "Stay consistent — success comes with discipline.",
            "Do something today that your future self will thank you for."
        ]
        return random.choice(quotes)

    # 📚 Study Tips Command
    if "study tip" in user_input or "how to study" in user_input:
        tips = [
            "Use the Pomodoro technique: 25 min focus + 5 min break.",
            "Revise regularly instead of last-minute studying.",
            "Practice active recall for better memory retention.",
            "Create a distraction-free study environment."
        ]
        return random.choice(tips)

    # 🏥 Health Tips Command
    if "health tip" in user_input or "health" in user_input:
        health_tips = [
            "Drink enough water and maintain a balanced diet.",
            "Get at least 7-8 hours of sleep daily.",
            "Exercise regularly for both physical and mental health.",
            "Take short breaks during long study sessions."
        ]
        return random.choice(health_tips)

    # 🧮 Basic Calculator Command (example: calculate 5+3)
    if "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            return f"The result is: {result}"
        except:
            return "Sorry, I couldn't calculate that. Try something like 'calculate 5 + 3'."

    # 🤖 About Bot Command
    if "who are you" in user_input or "about you" in user_input:
        return "I am an Advanced AI Chatbot with memory, smart commands, and context-aware responses built using Python."

    # 🎯 Help Command
    if "help" in user_input:
        return (
            "Here are some things you can ask me:\n"
            "- 'What is the time?'\n"
            "- 'Give me motivation'\n"
            "- 'Study tips'\n"
            "- 'Health tips'\n"
            "- 'Calculate 10 + 5'\n"
            "- 'My name is ___' (I will remember!)"
        )

    # If no command matched
    return None