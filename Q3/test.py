# import streamlit as st
# import requests
# import time

# # Streamed response emulator
# def response_generator(response):
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

# st.title("Chat with Luke SkyWalker")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# if prompt := st.chat_input("Ask a Question?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Make request to /ask route
#     response = requests.post("http://127.0.0.1:5000/ask", json={"question": prompt})
#     if response.status_code == 200:
#         data = response.json()
#         answer = data["answer"]
#         # Display assistant response with typing animation
#         with st.chat_message("assistant"):
#             st.write_stream(response_generator(answer))
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": answer})
#     else:
#         st.error("Error occurred while fetching the answer. Please try again.")
#         # Add error message to chat history
#         st.session_state.messages.append({"role": "assistant", "content": "Error occurred while fetching the answer. Please try again."})
        
# import streamlit as st
# import requests
# import time

# # Streamed response emulator
# def response_generator(response):
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

# def is_greeting(message):
#     greetings = ["hi", "hello", "hey", "howdy"]
#     return any(greeting in message.lower() for greeting in greetings)

# def is_about_whereabouts(message):
#     whereabouts_questions = ["how are you", "how's it going", "where are you"]
#     return any(question in message.lower() for question in whereabouts_questions)

# st.title("Chat with Luke Skywalker")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# if prompt := st.chat_input("Ask a Question?"):
#     # Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Check if user input is a greeting
#     if is_greeting(prompt):
#         # Display a generic response
#         with st.chat_message("assistant"):
#             st.write_stream(response_generator("Hello there! How can I assist you today?"))
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": "Hello there! How can I assist you today?"})
#     elif is_about_whereabouts(prompt):
#         # Respond to whereabouts question
#         with st.chat_message("assistant"):
#             st.write_stream(response_generator("I'm just here, ready to help! How about you?"))
#         # Add assistant response to chat history
#         st.session_state.messages.append({"role": "assistant", "content": "I'm just here, ready to help! How about you?"})
#     else:
#         # Make request to /ask route
#         response = requests.post("http://127.0.0.1:5000/ask", json={"question": prompt})
#         if response.status_code == 200:
#             data = response.json()
#             answer = data["answer"]
#             # Display assistant response with typing animation
#             with st.chat_message("assistant"):
#                 st.write_stream(response_generator(answer))
#             # Add assistant response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": answer})
#         else:
#             st.error("Error occurred while fetching the answer. Please try again.")
#             # Add error message to chat history
#             st.session_state.messages.append({"role": "assistant", "content": "Error occurred while fetching the answer. Please try again."})
# import streamlit as st
# import requests
# import time
# import speech_recognition as sr

# # Streamed response emulator
# def response_generator(response):
#     for word in response.split():
#         yield word + " "
#         time.sleep(0.05)

# def is_greeting(message):
#     greetings = ["hi", "hello", "hey", "howdy"]
#     return any(greeting in message.lower() for greeting in greetings)

# def is_about_whereabouts(message):
#     whereabouts_questions = ["how are you", "how's it going", "where are you"]
#     return any(question in message.lower() for question in whereabouts_questions)

# st.title("Chat with Luke Skywalker")

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # Accept user input
# input_type = st.radio("Select input type", ("Text", "Voice"))

# if input_type == "Text":
#     if prompt := st.chat_input("Ask a Question?"):
#         # Add user message to chat history
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         # Display user message in chat message container
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Check if user input is a greeting
#         if is_greeting(prompt):
#             # Display a generic response
#             with st.chat_message("assistant"):
#                 st.write_stream(response_generator("Hello there! How can I assist you today?"))
#             # Add assistant response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": "Hello there! How can I assist you today?"})
#         elif is_about_whereabouts(prompt):
#             # Respond to whereabouts question
#             with st.chat_message("assistant"):
#                 st.write_stream(response_generator("I'm just here, ready to help! How about you?"))
#             # Add assistant response to chat history
#             st.session_state.messages.append({"role": "assistant", "content": "I'm just here, ready to help! How about you?"})
#         else:
#             # Make request to /ask route
#             response = requests.post("http://127.0.0.1:5000/ask", json={"question": prompt})
#             if response.status_code == 200:
#                 data = response.json()
#                 answer = data["answer"]
#                 # Display assistant response with typing animation
#                 with st.chat_message("assistant"):
#                     st.write_stream(response_generator(answer))
#                 # Add assistant response to chat history
#                 st.session_state.messages.append({"role": "assistant", "content": answer})
#             else:
#                 st.error("Error occurred while fetching the answer. Please try again.")
#                 # Add error message to chat history
#                 st.session_state.messages.append({"role": "assistant", "content": "Error occurred while fetching the answer. Please try again."})
# else:  # Voice input
#     st.write("Click the button below and speak your question.")

#     # Record audio
#     with st.spinner("Recording..."):
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             audio_data = r.record(source, duration=5)
#         try:
#             prompt = r.recognize_google(audio_data)
#             # Add user message to chat history
#             st.session_state.messages.append({"role": "user", "content": prompt})
#             # Display user message in chat message container
#             with st.chat_message("user"):
#                 st.markdown(prompt)

#             # Check if user input is a greeting
#             if is_greeting(prompt):
#                 # Display a generic response
#                 with st.chat_message("assistant"):
#                     st.write_stream(response_generator("Hello there! How can I assist you today?"))
#                 # Add assistant response to chat history
#                 st.session_state.messages.append({"role": "assistant", "content": "Hello there! How can I assist you today?"})
#             elif is_about_whereabouts(prompt):
#                 # Respond to whereabouts question
#                 with st.chat_message("assistant"):
#                     st.write_stream(response_generator("I'm just here, ready to help! How about you?"))
#                 # Add assistant response to chat history
#                 st.session_state.messages.append({"role": "assistant", "content": "I'm just here, ready to help! How about you?"})
#             else:
#                 # Make request to /ask route
#                 response = requests.post("http://127.0.0.1:5000/ask", json={"question": prompt})
#                 if response.status_code == 200:
#                     data = response.json()
#                     answer = data["answer"]
#                     # Display assistant response with typing animation
#                     with st.chat_message("assistant"):
#                         st.write_stream(response_generator(answer))
#                     # Add assistant response to chat history
#                     st.session_state.messages.append({"role": "assistant", "content": answer})
#                 else:
#                     st.error("Error occurred while fetching the answer. Please try again.")
#                     # Add error message to chat history
#                     st.session_state.messages.append({"role": "assistant", "content": "Error occurred while fetching the answer. Please try again."})
#         except sr.UnknownValueError:
#             st.error("Could not understand audio.")
#         except sr.RequestError as e:
#             st.error(f"Error occurred: {e}")


import streamlit as st
import requests
import time
import speech_recognition as sr

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
        else:
            st.error("Error occurred while fetching the answer. Please try again.")
            # Add error message to chat history
            st.session_state.messages.append({"role": "assistant", "content": "Error occurred while fetching the answer. Please try again."})
