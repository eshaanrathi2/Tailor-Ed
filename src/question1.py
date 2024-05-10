question = "grading policy for this class"

from langchain_community.document_loaders import JSONLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain_community.vectorstores import Chroma

import json
from pathlib import Path
from pprint import pprint

import gc


file_path='/Users/eshaan/Desktop/projects/Tailor-Ed/data/test.json'


json_data = json.loads(Path(file_path).read_text())


# len(json_data['docs'])


# json_data['docs'][0]['title']


for doc in range(len(json_data['docs'])):
    if doc>5:
        continue
# for doc in range(0,1):
    loader = JSONLoader(
        file_path=file_path,
        jq_schema=f'.docs[{doc}].content',
        text_content=False
    )

    data = loader.load()
    print("Original Data:\n", data[0].page_content[0:50])

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    split_data = text_splitter.split_documents(data)

    # print(split_data)

    vectorstore = Chroma.from_documents(
                        documents=split_data, embedding=GPT4AllEmbeddings()
                )
    
    matches = vectorstore.similarity_search(question, 1)
    
    print("Retrieved data based on query:\n", matches)
    print("\n")
    del vectorstore
    del matches
    gc.collect()