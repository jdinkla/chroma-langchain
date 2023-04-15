from langchain.chains.summarize import load_summarize_chain
from langchain import OpenAI, LLMChain
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
import argparse
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

parser = argparse.ArgumentParser(description='Summarize the db.')
parser.add_argument('query')
args = parser.parse_args()
logging.debug(f'query={args.query}')

llm = OpenAI()
embeddings = OpenAIEmbeddings()
vectordb = Chroma(persist_directory="chroma-db", embedding_function=embeddings)
docs=vectordb.as_retriever().get_relevant_documents(args.query)
chain = load_summarize_chain(llm, chain_type="map_reduce")
response=chain.run(docs)
print(response)
