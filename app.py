import streamlit as st
from llama_index import VectorStoreIndex, SimpleDirectoryReader, StorageContext, GPTVectorStoreIndex
import os
import openai
import pickle

@st.cache_resource
def load_indexes():
    # Loading Index from local storage
    with open("dune_docs.pkl", "rb") as f:
        docs = pickle.load(f)
    index = GPTVectorStoreIndex.from_documents(docs)
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
