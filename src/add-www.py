import argparse
import logging
import os
from langchain.document_loaders import BSHTMLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from utilities import download, cleanup, split

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Add a HTML page to db.')
parser.add_argument('url')
args = parser.parse_args()
logging.debug(f'url={args.url}')

filename = f'/tmp/query-www-{os.getpid()}.html'
download(filename, args.url)

loader = BSHTMLLoader(filename)
documents = loader.load()
cleanup(documents)

embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="chroma-db", embedding_function=embeddings)
vectordb.add_documents(split(documents))
vectordb.persist()
