import argparse
import logging
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Query a PDF with GPT.')
parser.add_argument('filename')
args = parser.parse_args()
logging.debug(f'url={args.filename}')

loader = PyMuPDFLoader(args.filename)
documents = loader.load()

for obj in documents:
    obj.page_content = obj.page_content.replace('\n', ' ').replace('\\n', ' ').replace('  ', ' ')

embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="chroma-db", embedding_function=embeddings)
vectordb.add_documents(documents)
vectordb.persist()
