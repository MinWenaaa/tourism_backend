from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
import numpy as np
import os

class SearchEngine:
    def __init__(self, embedding_path: str):
        self.vector_store = Chroma(
            persist_directory = embedding_path, 
            embedding_function = DashScopeEmbeddings(dashscope_api_key=os.getenv("DASHSCOPE_API_KEY"))
        )

    def get_top_similarity_poi(self, k: int):
        pass

    def query(self, desc: tuple = None, top_k: int = None):
        """
        desc: 用户的正向与负面需求
        返回按相似度排序的id列表与相似度列表
        """
        pos_desc, neg_desc = desc
        pos_result_list = self.vector_store.similarity_search_with_score(
            query= pos_desc, k = 10000)     # List<tuple<Document, float>>
        
        pos_id_list = [item[0].metadata['id'] for item in pos_result_list]
        pos_score_list = [item[1] for item in pos_result_list]      # 按相似度排序
        sorted_indices_desc = np.argsort(pos_id_list)
        pos_id_list = np.array(pos_id_list)[sorted_indices_desc]
        pos_score_list = np.array(pos_score_list)[sorted_indices_desc]      # 按id排序
        if neg_desc not in [None, ""]:
            neg_result_list = self.vector_store.similarity_search_with_score(
                query = neg_desc, k = 10000)
            neg_id_list = [item[0].metadata['id'] for item in neg_result_list]
            neg_score_list = [item[1] for item in neg_result_list]
            sorted_indices_desc = np.argsort(neg_id_list)
            neg_score_list = np.array(neg_score_list)[sorted_indices_desc]
            pos_score_list -= neg_score_list
        
        top_k_indices = np.argsort(pos_score_list)[0:top_k]
        print(top_k_indices)
        top_k_ids = pos_id_list[top_k_indices]
        top_k_scores = pos_score_list[top_k_indices]        # 按相似度排序
        return top_k_ids, top_k_scores
            
        
if __name__=="__main__":
    path = os.path.join("model", "chroma_db")
    search_engin = SearchEngine(embedding_path = path)
    search_engin.query(desc = ("风景优美，人多热闹", ""), top_k = 10)