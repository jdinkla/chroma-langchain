from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader

def split(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    return text_splitter.split_documents(documents)

def texts(filename):
    loader = TextLoader(filename)
    documents = loader.load()
    return split(documents)

def db(texts):
    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(texts, embeddings, persist_directory="chroma-db")

def retriever(db):
    retriever = db.as_retriever()
    return RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="stuff", retriever=retriever)
