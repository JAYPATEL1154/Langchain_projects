import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# Langsmith tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACKING_V2'] = "True"
os.environ['LANGCHAIN_PROJECT'] = os.getenv("LANGCHAIN_PROJECT")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful AI bot. Your name is Carl."),
        ("user","Question:{question}")
    ]
)

# Streamlit Framwork
st.title("First chat model")
input_text = st.text_input("What question you have in mind?")

# Ollama LLAMMA2 
llm = Ollama(model="llama3")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

# To invoke model
if input_text:
    st.write(chain.invoke({"question":input_text}))