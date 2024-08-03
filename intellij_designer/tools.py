from langchain_core.tools import tool
from langchain.tools import Tool
from intellij_designer.data_poccessing import tourist_spots
import math

def get_distance(input: list) -> float:
    print(type(input))
    
    """根据两个地点的id计算它们之间的距离。"""

    lat1=0
    lon1=0
    lat2=0
    lon2=0

    for spot in tourist_spots:
        if spot['id']==input[0]:
            lat1=spot['lan']
            lon1=spot['lon']
        if spot['id']==input[1]:
            lat2=spot['lan']
            lon2=spot['lon']

    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    # 经纬度之差
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    
    # Haversine公式
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return 6371*c


distance_tool = Tool(
    name="get_distance",
    func=get_distance,
    description="根据两个地点的编号计算它们之间的距离。输入的参数为两个整型的列表，两个元素是两个景点的编号，返回的结果即为两个景点之间的距离。"
)

"""
class GetDistance(Tool):
    def __init__(self):
        super().__init__(name="get_distance", description="根据两个地点的id计算它们之间的距离。")

    def run(self, input_data):
        id1, id2 = input_data
        distance =self.calculate_distance(id1,id2)
        return distance

    def calculate_distance(id1: int, id2: int) -> float:
        lat1=0
        lon1=0
        lat2=0
        lon2=0

        for spot in tourist_spots:
            if spot['id']==id1:
                lat1=spot['lan']
                lon1=spot['lon']
            if spot['id']==id2:
                lat2=spot['lan']
                lon2=spot['lon']

        lat1_rad = math.radians(lat1)
        lon1_rad = math.radians(lon1)
        lat2_rad = math.radians(lat2)
        lon2_rad = math.radians(lon2)
    
        dlat = lat2_rad - lat1_rad
        dlon = lon2_rad - lon1_rad
    
        a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return 6371*c
"""