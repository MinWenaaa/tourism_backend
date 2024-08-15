import random
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma
import os
import intellij_designer.designer as designer
import intellij_designer.poi_sort as poi_sort


def tourism_deisgner(requirement, num):
    info = designer.get_info(requirement)
    resuqet = info["style"]
    ids = designer.get_resort(resuqet,num)


    return poi_sort.poiSort(ids)
    
    
