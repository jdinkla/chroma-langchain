import argparse
from langchain.document_loaders import PyMuPDFLoader
from utilities import db, retriever, split, cleanup
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Query a PDF with GPT.')
parser.add_argument('filename')
parser.add_argument('query')
args = parser.parse_args()
logging.debug(f'url={args.filename}')
logging.debug(f'query={args.query}')

loader = PyMuPDFLoader(args.filename)
documents = loader.load()
cleanup(documents)

vectordb = db(split(documents))
qa = retriever(vectordb)
response = qa.run(args.query)
print(response)
