from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document
import json
import os

def get_vectorstore():
    print("start")
    with open("./data/attraction","r",encoding ="utf-8") as inputfile:
        lines=inputfile.readlines()

    ids = [str(i) for i in range(0,9)]
    documents = []

    for line, id in zip(lines,ids):
        doc=Document(page_content=line,metadata={"name":id})
        documents.append(doc)
        print(doc)

    embedding = DashScopeEmbeddings(dashscope_api_key=os.getenv("ALI_API_KEY"))

    langchain_chroma = Chroma.from_documents(
        documents,
        embedding,
        persist_directory="./chroma_db",
    )


def get_data(file_path: str):
    with open(file_path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data

tourist_spots=get_data("data/attractionData.json")