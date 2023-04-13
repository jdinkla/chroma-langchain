from text_query import texts, db, retriever
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

texts = texts('texts/baerbock_in_china.txt')
vectordb = db(texts)
qa = retriever(vectordb)
query = "Was ist die Haltung Taiwans?"
#query = "Was sagte die Außenministerin?"
#query = "Welche Politiker werden im Artikel genannt?"
#query = "Welche Länder werden genannt?"
r = qa.run(query)
print(r)
