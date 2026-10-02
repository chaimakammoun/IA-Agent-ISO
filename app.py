import streamlit as st
from main import build_agent

st.set_page_config(page_title="Assistant Qualité Atlas Composants", page_icon="🤖")

st.title("🤖 Assistant Qualité — Atlas Composants")
st.caption("Pose une question sur ISO 9001 ou les procédures internes.")


@st.cache_resource
def get_agent():
    with st.spinner("Indexation des documents en cours..."):
        return build_agent()


agent = get_agent()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ta question...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Recherche en cours..."):
            response = agent.run(question)
            answer = response.content
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
