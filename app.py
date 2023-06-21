import streamlit as st
from llama_index import StorageContext, load_index_from_storage
import os
import openai


# Configure Streamlit Page
page_icon = "https://dune.com/assets/DuneLogoCircle.svg"
st.set_page_config(page_title="Dune Docs Wizard", page_icon=page_icon)

# Read Custom CSS
with open("assets/css/style.css", "r") as f:
    css_text = f.read()
custom_css = f"<style>{css_text}</style>"
st.markdown(custom_css, unsafe_allow_html=True)

# Headings
st.write(
    '<h1><img src="https://dune.com/assets/DuneLogoCircle.svg" alt="OpenAI logo" height="36" style="margin-bottom:6px">  Dune Docs Wizard</h1>',
    unsafe_allow_html=True,
)
st.write(
    "<h5>Ask any question about Dune's <a href='https://dune.com/docs/'>technical docs</a>.</h5>",
    unsafe_allow_html=True,
)

# Example
with st.expander("Example Question:"):
    st.code("What are Spellbooks?")


@st.cache_resource
def load_indexes():
    # Loading Index from local storage
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    return index


# API Key
openai.api_key = os.environ["OPENAI_API_KEY"]

# Load index
index = load_indexes()

# Query index
query = st.text_input("Question", help="")
button = st.button("Answer")

if button:
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    st.write(response)
