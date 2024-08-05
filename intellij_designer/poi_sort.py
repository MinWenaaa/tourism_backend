from sqlalchemy.sql import func
from model.db_model import pois
from create_app import db
import numpy as np
import math

def sort(id_list, location_list):

    AntCount = 50 #蚂蚁数量
    city_count = len(id_list) #城市数量
    alpha = 1  # 信息素重要程度因子
    beta = 2  # 启发函数重要程度因子
    rho = 0.1 #挥发速度
    Iter = 0  # 迭代初始值
    MAX_iter = 50  # 最大迭代值
    Q = 1

    Distance = np.zeros((city_count, city_count))
    for i in range(city_count):
        for j in range(city_count):
            if i != j:
                Distance[i][j] = (math.sqrt((location_list[i]['x'] - location_list[j]['x']) ** 2 + (location_list[i]['y'] - location_list[j]['y']) ** 2))*100
            else:
                Distance[i][j] = 100000

    pheromonetable = np.ones((city_count, city_count)) # 信息素矩阵
    candidate = np.zeros((AntCount, city_count)).astype(int) # 当前循环蚂蚁们的路径
    path_best = np.zeros((MAX_iter, city_count)) # 当前循环的最优路径
    distance_best = np.zeros( MAX_iter) # 每次循环的最优蚂蚁的距离
    etable = 1.0 / Distance 

    while Iter <  MAX_iter:

        # 循环开始，随机蚂蚁初始位置
        if AntCount <= city_count:          
            candidate[:, 0] = np.random.permutation(range(city_count))[:AntCount]
        else:
            m =AntCount -city_count
            n =2
            candidate[:city_count, 0] = np.random.permutation(range(city_count))[:]
            while m >city_count:
                candidate[city_count*(n -1):city_count*n, 0] = np.random.permutation(range(city_count))[:]
                m = m -city_count
                n = n + 1
            candidate[city_count*(n-1):AntCount,0] = np.random.permutation(range(city_count))[:m]

        length = np.zeros(AntCount) # 当前循环蚂蚁们走过的距离

        # 蚂蚁行动
        for i in range(AntCount):

            # 初始化未访问城市列表
            unvisit = list(range(city_count))  
            visit = candidate[i, 0]  
            unvisit.remove(visit)  

            # 访问剩下的city_count个城市，city_count次访问
            for j in range(1, city_count):

                # 当前没有访问的城市的转移概率矩阵
                protrans = np.zeros(len(unvisit))   
                for k in range(len(unvisit)):
                    protrans[k] = np.power(pheromonetable[visit][unvisit[k]], alpha) * np.power(
                        etable[visit][unvisit[k]], (alpha + 1))

                # 累计概率，轮盘赌选择
                cumsumprobtrans = (protrans / sum(protrans)).cumsum()
                cumsumprobtrans -= np.random.rand()
                k = unvisit[list(cumsumprobtrans > 0).index(True)]
                candidate[i, j] = k
                unvisit.remove(k)
                length[i] += Distance[visit][k]
                visit = k 

            length[i] += Distance[visit][candidate[i, 0]]  

        # 更新结果
        if Iter == 0:
            distance_best[Iter] = length.min()
            path_best[Iter] = candidate[length.argmin()].copy()
        else:
            if length.min() > distance_best[Iter - 1]:
                distance_best[Iter] = distance_best[Iter - 1]
                path_best[Iter] = path_best[Iter - 1].copy()
            else:
                distance_best[Iter] = length.min()
                path_best[Iter] = candidate[length.argmin()].copy()

        # 更新信息素
        changepheromonetable = np.zeros((city_count, city_count))
        for i in range(AntCount):
            for j in range(city_count - 1):
                changepheromonetable[candidate[i, j]][candidate[i][j + 1]] += Q / length[i]
                #Distance[candidate[i, j]][candidate[i, j + 1]]
            changepheromonetable[candidate[i, j + 1]][candidate[i, 0]] += Q / length[i]
        pheromonetable = (1 - rho) * pheromonetable + changepheromonetable

        Iter += 1

    path = (path_best[-1]).tolist()
    result=[]
    for point in path:
        result.append(id_list[int(point)])

    return result

def poiSort(poi_list):

    locations =[]
    for id in poi_list:
        query = db.session.query(
            func.ST_X(pois.plocation).label('x'),
            func.ST_Y(pois.plocation).label('y'),
        ).filter_by(pid=id).first()
        coordination = {key: value for key, value in query._asdict().items()}
        locations.append(coordination)

    return sort(poi_list, locations)

