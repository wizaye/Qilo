import streamlit as st
import requests
import time
import speech_recognition as sr
from gtts import gTTS
from io import BytesIO

# Streamed response emulator
def response_generator(response):
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

def is_greeting(message):
    greetings = ["hi", "hello", "hey", "howdy"]
    return any(greeting in message.lower() for greeting in greetings)

def is_about_whereabouts(message):
    whereabouts_questions = ["how are you", "how's it going", "where are you"]
    return any(question in message.lower() for question in whereabouts_questions)

st.title("Chat with Luke Skywalker")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Button to toggle speech audio output
enable_audio = st.sidebar.checkbox("Enable Speech Output")

# Accept user input
col1, col2 = st.columns([4, 1])
# with col1:
prompt = st.chat_input("Ask a Question?")
# with col2:
if st.button("🎙️"):
     # Record audio
    with st.spinner("Recording..."):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio_data = r.record(source, duration=5)
        try:
            prompt = r.recognize_google(audio_data)
        except sr.UnknownValueError:
            st.error("Could not understand audio.")
        except sr.RequestError as e:
            st.error(f"Error occurred: {e}")

# Process user input
if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Check if user input is a greeting
    if is_greeting(prompt):
        # Display a generic response
        with st.chat_message("assistant"):
            st.write_stream(response_generator("Hello there! How can I assist you today?"))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": "Hello there! How can I assist you today?"})
    elif is_about_whereabouts(prompt):
        # Respond to whereabouts question
        with st.chat_message("assistant"):
            st.write_stream(response_generator("I'm just here, ready to help! How about you?"))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": "I'm just here, ready to help! How about you?"})
    else:
        # Make request to /ask route
        response = requests.post("http://127.0.0.1:5000/ask", json={"question": prompt})
        if response.status_code == 200:
            data = response.json()
            answer = data["answer"]
            # Display assistant response with typing animation
            with st.chat_message("assistant"):
                st.write_stream(response_generator(answer))
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": answer})
            
            # Convert assistant response to speech audio if enabled
            if enable_audio:
                # Using gTTS to convert text to speech
                tts = gTTS(answer, lang='en')
                audio_bytes_io = BytesIO()
                tts.write_to_fp(audio_bytes_io)
                audio_bytes_io.seek(0)
                st.audio(audio_bytes_io, format='audio/mp3')
            
        else:
            st.error("Error occurred while fetching the answer. Please try again.")
            # Add error message to chat history
            st.session_state.messages.append({"role": "assistant", "content": "Error occurred while fetching the answer. Please try again."})
