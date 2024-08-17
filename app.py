import streamlit as st
from chatbot_model import chatbot

def app():
    st.set_page_config(page_title="Remote work productivity bot", page_icon="🤖", layout="wide")

    # Load external CSS for styling
    st.markdown(
        """
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <link rel="stylesheet" href="static/custom.css">
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="container-fluid">
        <div class="header-container text-center">
            <h1 class="header">Remote work Productivity Chatbot</h1>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    # Initialize session state to store chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    st.write("Tell me your Query!")

    # Capture user input
    user_input = st.text_input("You:", "")
    if user_input:
        # Get the chatbot's response
        response = chatbot(user_input)

        # Add user input and bot response to chat history
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(f"Bot: {response}")

    # Display chat history
    for message in st.session_state.chat_history:
        st.write(message)

    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    app()
