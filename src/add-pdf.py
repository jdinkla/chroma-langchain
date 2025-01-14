import argparse
import logging
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from utilities import cleanup, split

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Add a PDF to db.')
parser.add_argument('filename')
args = parser.parse_args()
logging.debug(f'url={args.filename}')

loader = PyMuPDFLoader(args.filename)
documents = loader.load()
cleanup(documents)

embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="chroma-db", embedding_function=embeddings)
vectordb.add_documents(split(documents))
vectordb.persist()
