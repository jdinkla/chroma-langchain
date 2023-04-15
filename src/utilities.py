from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
import logging
import os
import requests

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def split(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return text_splitter.split_documents(documents)

def texts(filename):
    loader = TextLoader(filename)
    documents = loader.load()
    return split(documents)

def db(texts):
    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(texts, embeddings, persist_directory="chroma-db-temporary")

def retriever(db):
    retriever = db.as_retriever()
    return RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)

def cleanup(documents):
    for obj in documents:
        obj.page_content = obj.page_content.replace('\n', ' ').replace('\\n', ' ').replace('  ', ' ')

def download(filename, url):
    if not os.path.exists(filename):
        logging.info(f'file {filename} does not exist, downloading')
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                f.write(response.content)
            logging.info('File downloaded successfully!')
        else:
            logging.error('File download failed.')
            exit
