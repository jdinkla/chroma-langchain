import argparse
import logging
import os
from langchain.document_loaders import BSHTMLLoader
from utilities import db, retriever, split, cleanup, download

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Download a file and query it with GPT.')
parser.add_argument('url')
parser.add_argument('query')
args = parser.parse_args()
logging.debug(f'url={args.url}')
logging.debug(f'query={args.query}')

filename = f'/tmp/query-www-{os.getpid()}.html'
download(filename, args.url)

loader = BSHTMLLoader(filename)
documents = loader.load()
cleanup(documents)

qa = retriever(db(split(documents)))
response = qa.run(args.query)
print(response)
