from langchain.document_loaders import BSHTMLLoader
from text_query import db, retriever, split
import logging
from download import download

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

filename = '/tmp/baerbock-china.html'
download(filename, 'https://www.zeit.de/politik/ausland/2023-04/baerbock-china-reise-ukraine-taiwan')

loader = BSHTMLLoader(filename)
documents = loader.load()
qa = retriever(db(split(documents)))

#query = "Was sagte die Außenministerin?"
query = "Was ist die Haltung Taiwans?"
#query = "Welche Politiker werden im Artikel genannt?"
#query = "Welche Länder werden genannt?"
r = qa.run(query)
print(r)
