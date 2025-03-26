import csv
import os
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_community.embeddings import DashScopeEmbeddings

def get_document(file_path: str):
    documents = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  
        for row in reader:
            documents.append(Document(
                page_content = row['desc'],
                metadata = {
                    "id": row['id'],
                    "name": row["name"],
                    "coord": [row["longtitude"], row["latitude"]]
                }
            ))
    return documents
            

if __name__=="__main__":

    db = Chroma.from_documents(
        get_document(os.path.join("model","data","test.csv")), 
        DashScopeEmbeddings(dashscope_api_key=os.getenv("DASHSCOPE_API_KEY")),
        persist_directory="model/chroma_db",
    )