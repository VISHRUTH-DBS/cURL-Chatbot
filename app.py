import os
import re

import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY is not configured.")
    st.stop()


st.set_page_config(
    page_title="cURL AI Chatbot",
    page_icon="🔗",
    layout="centered"
)

st.title("cURL AI Chatbot")
st.write("Ask for an API based on what you need.")


def load_curls():
    curls = []

    with open("curl.txt", "r", encoding="utf-8") as file:
        content = file.read()

    pattern = r'curl\s+(?:"([^"]+)"|\'([^\']+)\'|(\S+))'

    matches = re.findall(pattern, content, re.IGNORECASE)

    for match in matches:
        url = next((value for value in match if value), None)

        if url:
            curls.append({
                "curl": f'curl "{url}"',
                "url": url
            })

    return curls


def find_best_match(question, curls):
    curl_list = "\n".join(
        f"{index + 1}. {item['curl']}"
        for index, item in enumerate(curls)
    )

    prompt = f"""
You are an API and cURL retrieval assistant.

The user will describe the type of API or information they need.

Select the single most relevant cURL from the provided list.

Understand the semantic meaning of the user's request.
Do not rely only on exact keyword matching.

Available cURLs:

{curl_list}

User request:

{question}

Rules:
1. Select the most relevant cURL.
2. Return only the number of the selected cURL.
3. If none are relevant, return 0.
4. Do not return explanations.
5. Do not return markdown.
"""

    response = llm.invoke(prompt)
    answer = response.content.strip()

    match = re.search(r"\b(\d+)\b", answer)

    if not match:
        return None

    index = int(match.group(1))

    if index == 0 or index > len(curls):
        return None

    return curls[index - 1]


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    groq_api_key=groq_api_key
)


curls = load_curls()

if not curls:
    st.error("No cURLs were found in curl.txt.")
    st.stop()


if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        if message["role"] == "user":
            st.write(message["content"])

        else:
            if message.get("url"):
                st.markdown("**Matching API**")
                st.code(message["curl"], language="bash")
                st.markdown(f"[Open API]({message['url']})")
            else:
                st.write(message["content"])


question = st.chat_input(
    "Example: I need a free fake REST API for testing"
)


if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Searching APIs..."):

            result = find_best_match(question, curls)

        if result:

            st.markdown("**Matching API**")

            st.code(
                result["curl"],
                language="bash"
            )

            st.markdown(
                f"[Open API]({result['url']})"
            )

            st.session_state.messages.append({
                "role": "assistant",
                "content": "Matching API",
                "curl": result["curl"],
                "url": result["url"]
            })

        else:

            response = "I couldn't find a relevant API in `curl.txt`."

            st.write(response)

            st.session_state.messages.append({
                "role": "assistant",
                "content": response
            })