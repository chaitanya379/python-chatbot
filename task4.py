import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Simple Python Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Chatbot Response Function
def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you today? 😊"

    elif user_input == "how are you":
        return "I'm doing great. Thanks for asking! 😄"

    elif user_input == "what is your name":
        return "I am a Simple Python Chatbot built with Streamlit. 🤖"

    elif user_input == "help":
        return """
You can try:
• hello
• how are you
• what is your name
• help
• bye
"""

    elif user_input == "bye":
        return "Goodbye! Have a great day! 👋"

    else:
        return "Sorry, I don't understand that. 😅"


# Title
st.title("🤖 Simple Python Chatbot")
st.write("Type a message and chat with the bot!")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User Input
user_input = st.chat_input("Type your message...")

if user_input:

    # Store User Message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Generate Bot Response
    response = get_response(user_input)

    # Store Bot Response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    # Refresh Page
    st.rerun()