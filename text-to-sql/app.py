import streamlit as st
import openai
import langchain
import google.generativeai as genai
import os, sqlite3
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv


load_dotenv()

# Fucntion to load LLM and provide sql query as a response

def get_LLM_response(query, prompt):
    llm = ChatOpenAI(model = os.getenv("model"), openai_api_key = os.getenv("openai_api_key"))
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.invoke(query)
    print(response)
    return response.text
    

# Function to receive generated sql query and execute it on sqlite3 db
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are a code assistant in converting English questions to SQL query!
    The SQL database is connected.
    also the sql code should not have ``` in beginning or end and sql word in output

    """


]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

# if submit is clicked
if submit:
    model=ChatOpenAI()
    response=model.invoke([prompt[0],question])
    print(response.content)
    response=read_sql_query(response.content,"sqlitesakila.db")
    st.subheader("The REsponse is")
    for row in response:
        print(row)
        st.header(row)


#get_LLM_response(query,prompt)