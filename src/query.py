import argparse
from text_query import retriever
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Query a PDF with GPT.')
parser.add_argument('query')

args = parser.parse_args()
logging.debug(f'query={args.query}')

embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="chroma-db", embedding_function=embeddings)

qa = retriever(vectordb)
response = qa.run(args.query)
print(response)
