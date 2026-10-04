import streamlit as st

from iso_assistant.agent import build_agent


def run() -> None:
    st.set_page_config(page_title="Atlas Components Quality Assistant", page_icon="🤖")
    st.title("🤖 Atlas Components Quality Assistant")
    st.caption("Ask a question about ISO 9001 or internal procedures.")

    @st.cache_resource
    def get_agent():
        with st.spinner("Indexing documents..."):
            return build_agent()

    agent = get_agent()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Your question...")
    if not question:
        return

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Searching documents..."):
            answer = agent.run(question).content
        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
