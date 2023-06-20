import streamlit as st
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
import os
import openai


@st.cache_resource
def load_indexes():
    """load the pipeline object for preprocessing and the ml model"""

    # Loading Index from local storage
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context)
    return index

# api key
openai.api_key = os.environ["OPENAI_API_KEY"]

# load indices
index = load_indexes()

st.header('Dune Docs Wizard')

# query the selected index
query = st.text_input('Enter Your Query')
button = st.button(f'Response')

if button:
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    st.write(response)
