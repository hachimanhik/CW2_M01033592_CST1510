import streamlit as st
from openai import OpenAI

# check login
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please login first on Home page.")
    st.stop()

# openai client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# page settings
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# title
st.title("🤖 AI Assistant")
st.caption("Chat using OpenAI API")

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# sidebar
with st.sidebar:
    st.subheader("Chat Options")

    # number of messages
    count = len([m for m in st.session_state.messages if m["role"] != "system"])
    st.metric("Messages", count)

    # clear chat button
    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

    # choose model
    model = st.selectbox("Model", ["gpt-4o", "gpt-4o-mini"])

    # choose domain
    domain = st.selectbox(
        "Domain",
        ["General", "Cybersecurity", "IT Support", "Datasets"]
    )

# short domain behaviour setup
def get_domain_instruction(domain):
    if domain == "Cybersecurity":
        return "You are a cybersecurity expert. Answer using cybersecurity knowledge."
    elif domain == "IT Support":
        return "You are an IT support technician. Explain troubleshooting steps."
    elif domain == "Datasets":
        return "You understand datasets, rows, columns, and analysis."
    else:
        return "You are a helpful assistant."

# create system message
system_message = {
    "role": "system",
    "content": get_domain_instruction(domain)
}

# put system message at top of history
if len(st.session_state.messages) == 0 or st.session_state.messages[0]["role"] != "system":
    st.session_state.messages.insert(0, system_message)
else:
    st.session_state.messages[0] = system_message

# show old messages
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# read user input
user_prompt = st.chat_input("Type your message...")

if user_prompt:
    # show user message
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # save user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_prompt
    })

    # call AI
    with st.spinner("AI is thinking..."):
        stream = client.chat.completions.create(
            model=model,
            messages=st.session_state.messages,
            stream=True
        )

    # show answer
    with st.chat_message("assistant"):
        box = st.empty()
        full_reply = ""

        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta.content:
                full_reply += delta.content
                box.markdown(full_reply + "▌")

        box.markdown(full_reply)

    # save AI answer
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_reply
    })
