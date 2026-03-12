import json
import os
import boto3
import streamlit as st
import numpy as np

# Modern LangChain Imports
from langchain_community.embeddings import BedrockEmbeddings
from langchain_aws import ChatBedrock
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate

# Fix for the create_retrieval_chain import
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


## Bedrock Clients
bedrock = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock)

## Data ingestion
def data_ingestion():
    if not os.path.exists("data"):
        os.makedirs("data")
    loader = PyPDFDirectoryLoader("data")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1500, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    return docs

## Vector Embedding and vector store
def get_vector_store(docs):
    vectorstore_faiss = FAISS.from_documents(docs, bedrock_embeddings)
    vectorstore_faiss.save_local("faiss_index")

def get_claude_llm():
    return ChatBedrock(
        model_id="us.anthropic.claude-3-haiku-20240307-v1:0",
        client=bedrock,
        model_kwargs={
            "max_tokens": 1000,
            "temperature": 0.5,
            "top_p": 0.9
        }
    )

def get_llama_llm():
    return ChatBedrock(
        model_id="us.meta.llama3-2-1b-instruct-v1:0",
        client=bedrock,
        model_kwargs={
            "max_gen_len": 800,
            "temperature": 0.5
        }
    )

# The prompt uses 'input' as the key to match modern retrieval chains
prompt_template = """
Human: Use the following context to provide a detailed, 150-word answer. 
If the answer is not in the context, say you don't know.

<context>
{context}
</context>

Question: {input}

Assistant:"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "input"]
)

def get_response_llm(llm, vectorstore_faiss, query):
    combine_docs_chain = create_stuff_documents_chain(llm, PROMPT)
    retrieval_chain = create_retrieval_chain(
        retriever=vectorstore_faiss.as_retriever(search_kwargs={"k": 3}),
        combine_docs_chain=combine_docs_chain
    )
    # The modern chain uses 'input' and returns 'answer'
    response = retrieval_chain.invoke({"input": query})
    return response["answer"]

def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using AWS Bedrock💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    with st.sidebar:
        st.title("Update Or Create Vector Store:")
        if st.button("Vectors Update"):
            with st.spinner("Processing..."):
                docs = data_ingestion()
                get_vector_store(docs)
                st.success("Done")

    if st.button("Claude Output"):
        if not os.path.exists("faiss_index"):
            st.error("Please update vectors first!")
        else:
            with st.spinner("Processing..."):
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
                llm = get_claude_llm()
                st.write(get_response_llm(llm, faiss_index, user_question))

    if st.button("Llama Output"): # Renamed for clarity
        if not os.path.exists("faiss_index"):
            st.error("Please update vectors first!")
        else:
            with st.spinner("Processing..."):
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
                llm = get_llama_llm() # Fixed function name typo here
                st.write(get_response_llm(llm, faiss_index, user_question))

if __name__ == "__main__":
    main()


