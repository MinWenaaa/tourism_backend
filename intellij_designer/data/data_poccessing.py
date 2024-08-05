from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document
import pandas
import json
import os

"""
将描述信息的语义向量保存到本地
"""

if __name__ == '__main__':

    file_path = 'intellij_designer/data/output.xlsx'
    df = pandas.read_excel(file_path, engine='openpyxl')
    ids = df['id'].tolist()
    descs = df['desc'].tolist()

    documents = []
    for id,desc in zip(ids, descs):
        doc = Document(page_content=desc, metadata={"id":id})
        documents.append(doc)
        print(doc)        



    embedding = DashScopeEmbeddings(dashscope_api_key=os.getenv("ALI_API_KEY"))

    langchain_chroma = Chroma.from_documents(
        documents,
        embedding,
        persist_directory="intellij_designer/chroma_db",
    )



