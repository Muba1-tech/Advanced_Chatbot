import streamlit as st
import json
from brain import generate_response
from commands import handle_command

# Load memory
def load_memory():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)
    except:
        return {"name": "", "history": []}

# Save memory
def save_memory(memory):
    with open("memory.json", "w") as file:
        json.dump(memory, file, indent=4)

# Initialize memory
memory = load_memory()

st.set_page_config(page_title="Advanced AI Chatbot", page_icon="🤖")
st.title("🤖 Advanced AI Chatbot with Memory")
st.write("Your personal AI assistant (Day 1 Project)")

# Chat history display
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input
user_input = st.text_input("Type your message:")

if user_input:
    # Check for commands first
    command_response = handle_command(user_input)

    if command_response:
        bot_response = command_response
    else:
        bot_response = generate_response(user_input, memory)

    # Store in session history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_response))

    # Save conversation to memory file
    memory["history"].append({"user": user_input, "bot": bot_response})
    save_memory(memory)

# Display chat
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 Bot:** {message}")

# Sidebar Memory Info (Advanced Feature)
st.sidebar.title("🧠 Memory Panel")

if memory["name"]:
    st.sidebar.write(f"👤 Name: {memory['name']}")
else:
    st.sidebar.write("👤 Name not set")

st.sidebar.write(f"💬 Conversations Stored: {len(memory['history'])}")

if st.sidebar.button("Clear Memory"):
    memory = {"name": "", "history": []}
    save_memory(memory)
    st.sidebar.success("Memory Cleared!")