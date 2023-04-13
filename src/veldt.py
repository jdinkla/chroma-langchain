from text_query import texts, db, retriever
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

texts = texts('texts/veldt.txt')
vectordb = db(texts)
qa = retriever(vectordb)
query = "Who is having this dialogue?"
r = qa.run(query)
print(r)

