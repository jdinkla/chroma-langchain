import argparse
import logging
import os
from download import download
from langchain.document_loaders import BSHTMLLoader
from text_query import db, retriever, split

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Download a file and query it with GPT.')

parser.add_argument('url')
parser.add_argument('query')

args = parser.parse_args()
logging.debug(f'url={args.url}')
logging.debug(f'query={args.query}')

filename = f'/tmp/get-and-query-{os.getpid()}.html'
download(filename, args.url)

loader = BSHTMLLoader(filename)
documents = loader.load()

for obj in documents:
    obj.page_content = obj.page_content.replace('\n', ' ').replace('\\n', ' ').replace('  ', ' ')

qa = retriever(db(split(documents)))
response = qa.run(args.query)
print(response)
