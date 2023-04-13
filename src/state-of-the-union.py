from text_query import texts, db, retriever
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

texts = texts('texts/state_of_the_union.txt')
vectordb = db(texts)
qa = retriever(vectordb)
query = "What did the president say about Putin?"
r = qa.run(query)
print(r)
