import argparse
import logging
from langchain.document_loaders import PyMuPDFLoader
from text_query import db, retriever, split

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Query a PDF with GPT.')
parser.add_argument('filename')
parser.add_argument('query')

args = parser.parse_args()
logging.debug(f'url={args.filename}')
logging.debug(f'query={args.query}')

loader = PyMuPDFLoader(args.filename)
documents = loader.load()

for obj in documents:
    obj.page_content = obj.page_content.replace('\n', ' ').replace('  ', ' ')

qa = retriever(db(split(documents)))
response = qa.run(args.query)
print(response)
