from openai import OpenAI
import streamlit as st

st.title('ChatGPT Clone')

key: str = st.text_input('Enter OpenAI secret key.. ', type='password')
st.markdown("<p style='font-size: 14px'>Never upload your OpenAI secret key in public. This app is stateless and your secret key is not safe anywhere. Only use for testing app. For safety purposes, delete your secret key after using </p>", unsafe_allow_html=True)

if key:
    client = OpenAI(api_key=key)

    if OpenAI(api_key=key):
        
        if 'messages' not in st.session_state:
            st.session_state.messages = [
                {'role': 'system', 'content': 'You are ChatGPT. You have to respond to user queries in brief and concise manner'}
            ]
        
        for message in st.session_state.messages:
            if message['role'] == 'system':
                continue
            with st.chat_message(message['role']):
                st.markdown(message['content'])
                
        prompt = st.chat_input('Ask ChatGPT...')
        
        if prompt:
            with st.chat_message('user', avatar='🧑‍💻'):
                st.markdown(prompt)

            st.session_state.messages.append({'role': 'user', 'content': prompt})
            
            with st.chat_message('assistant', avatar='🤖'):
                response_placeholder = st.empty()
                assistant_response = ''
                
                for response in client.chat.completions.create(
                    model = 'gpt-3.5-turbo',
                    messages = [
                        {'role':m['role'], 'content': m['content']}
                        for m in st.session_state.messages
                    ],
                    stream = True
                ):
                    if response.choices[0].delta.content is not None:
                        assistant_response += response.choices[0].delta.content
                        response_placeholder.markdown(assistant_response + "| ")
                    response_placeholder.markdown(assistant_response )
                st.session_state.messages.append({'role': 'assistant', 'content': assistant_response})
                        