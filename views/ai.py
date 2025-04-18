
from openai import OpenAI

import streamlit as st
st.markdown(
    """<p style="text-align: center; font-size: 25px;"> Use Deepseek API chat with memory</p>""",
    unsafe_allow_html=True
)
colai = st.columns(2)
API_KEY = colai[0].text_input("Please enter your Deepseek API key")
API_URL = "https://api.deepseek.com"
client = OpenAI(api_key=API_KEY, base_url=API_URL)
st.divider()

# API_KEY = "sk-d5e0ddf5b01a49aeb3270c89e597322d"

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "I am a AI assistant"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    if not API_KEY:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        response = client.chat.completions.create(model="deepseek-chat", messages=st.session_state.messages,stream=False)
        result = response.choices[0].message.content
        message_placeholder.markdown(result)

    st.session_state.messages.append({"role": "assistant", "content": result})
