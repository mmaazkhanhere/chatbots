import streamlit as st

st.title('Echo bot')

if 'e_messages' not in st.session_state:
    st.session_state.e_messages = []
    
for message in st.session_state.e_messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])
        
prompt = st.chat_input('Wassup')
if prompt:
    with st.chat_message('user'):
        st.markdown(prompt)
        
    st.session_state.e_messages.append({'role': 'user', 'content': prompt})
    
    with st.chat_message('assistant'):
        response = f"Echo: {prompt}"
        st.markdown(response)

    st.session_state.e_messages.append({'role':'assistant', 'content': response})    

