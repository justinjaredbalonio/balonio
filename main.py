import streamlit as st

st.title('CHATBOT')

prompt = st.chat_input("Type Here")

if "messages" not in st.session_state:
	st.session_state.messages = []

for message in st.session_state.messages:
	user_input = st.chat_message('role')
	user_input.write(message['content'])

st.chat_message("user").write(prompt)

if prompt and prompt != '':
	st.session_state.messages.append({'role': 'user', 'content': prompt})

if prompt== 'hello':
	st.chat_message("assistant").write('How are you?')
	st.session_state.messages.append({'role': 'assistant', 'content': 'How are you?'})
elif prompt == 'who are you':
	st.chat_message("assistant").write('I am your assistant')
	st.session_state.messages.append({'role': 'assistant', 'content': 'I am your assistant'})
elif prompt == 'hi':
	st.chat_message("assistant").write('Hello!')
	st.session_state.messages.append({'role': 'assistant', 'content': 'Hello!'})
elif prompt == 'where you from':
	st.chat_message("assistant").write('Antipolo City')
	st.session_state.messages.append({'role': 'assistant', 'content': 'Antipolo City'})	
elif prompt == 'How is your day?':
	st.chat_message("assistant").write('Im Happy')
	st.session_state.messages.append({'role': 'assistant', 'content': 'Im Happy'})
elif prompt == 'I Love You!':
	st.chat_message("assistant").write('I Love You Too')
	st.session_state.messages.append({'role': 'assistant', 'content': 'Im Happy'})

		