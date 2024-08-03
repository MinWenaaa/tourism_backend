import intellij_designer.designer as designer
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma
import os

"""
if __name__=="__main__":
    info = designer.get_info("6月15日早上到达，17日晚上返回，共计三天两晚。想去想去东湖风景区，特别是听涛景区和磨山景区，还想去武汉大学，如果季节合适，希望能看到樱花。总体偏好好玩有意思、比较刺激的地方。希望住宿地点交通便利，靠近主要的旅游景点或地铁站，偏好舒适型酒店或具有特色的民宿。用餐环境偏好当地人常去的餐馆或小吃摊，不介意排队等待，但希望卫生条件良好。倾向于使用公共交通工具（地铁、公交、轮渡），对于较远的景点，可以考虑打车。预计总预算为1000元人民币，包括住宿、餐饮、交通、门票和一些小额购物。")
    resuqet = info["style"]
    print(resuqet)
    names = designer.get_resort(resuqet,4)
    print(names)
    """