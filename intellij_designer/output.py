import random
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma
import os
import intellij_designer.designer as designer
import intellij_designer.poi_sort as poi_sort


def tourism_deisgner(requirement):
    info = designer.get_info(requirement)
    resuqet = info["style"]
    point_num = random.randrange((info["duration"][0]+1)*2, (info["duration"][0]+1)*3)
    ids = designer.get_resort(resuqet,point_num)
    return poi_sort.poiSort(ids)
    
    
