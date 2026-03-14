import streamlit as st
from groq import Groq

st.title("General knowlage AI")
st.caption("Ask me absolutely anything!")

client = Groq(api_key=st.secrets["GROQ_API_KEY"])

system_prompt = "you are a hightly intelligent, friendly, and helpful AI assistant. answer any question the user asks clearly nad accurately."

if "message" not in st.session_state:
    st.session_state.message = [{"role": "system", "content"; system_prompt}]

for msg in st.session_state.messages:
    if msg["role"] != "system"
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

if prompt := st..chat_input(Ask me anything...):
    st.session_state.message.append({"role": "user, "content:prommmpt})
    with st.chat_message(user):
        st.markdown(prompt)

answer = client.chat.completions.create(
    moidel="llama-3.3-70b-versatile",
    messages=st.session_state.messsage
).choices[0].message.content

st.session_state.message.append({"role": 'assistant', "content": answer})
with  st.chat_message("assistant"):
    st.marskdown(answer)













