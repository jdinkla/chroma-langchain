from text_query import split, db, retriever
import logging
from langchain.document_loaders import PyMuPDFLoader
from download import download

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

filename = '/tmp/cathedral.pdf'
url = 'http://www.giuliotortello.it/ebook/cathedral.pdf'

download(filename, url)

loader = PyMuPDFLoader(filename)
documents = loader.load()

for obj in documents:
    obj.page_content = obj.page_content.replace('\n', ' ').replace('  ', ' ')

qa = retriever(db(split(documents)))
#query = "How did they keep in touch?"
#query = "What did she not like about her life?"
query = "Who is Beulah?"
r = qa.run(query)
print(r)
