import scipy
import numpy as np
import networkx as nx

class SpatialHandler:
    def __init__(self, data:list, min_cluters=True, min_pois=True, citywalk=False, citywalk_tresh=5000):
        self.data = data
        self.min_pois = min_pois
        self.min_cluters = min_cluters
        self.citywalk = citywalk
        self.citywalk_tresh = citywalk_tresh

    def get_clusters(self, poi_idList:list, thresh:int=0.015):
        coords = np.array([[item['longtitude'], item['latitude']] for item in self.data])
        dist_matrix = scipy.spatial.distance.cdist(coords, coords)
        np.fill_diagonal(dist_matrix, thresh+100)
        N = len(coords)
        G = nx.Graph()
        for i in range(N):  # 添加距离小于阈值的边
            G.add_edge(i,i)
            for j in range(i+1, N):
                if dist_matrix[i,j] < thresh:
                    G.add_edge(i,j)

        all_clusters = []

        if G.number_of_edges() == 0:
            all_clusters = [[i for i in poi_idList]]
            return all_clusters
        
        while G.number_of_nodes()>0:
            cliques = list(nx.find_cliques(G))
            index_of_longest = max(enumerate(cliques),key=lambda x:len(x[1]))[0]
            biggest_cluster_list = list(set(cliques[index_of_longest]))
            G.remove_nodes_from(biggest_cluster_list)
            all_clusters.append(set(np.array(poi_idList)[np.array(biggest_cluster_list)].tolist()))
        return all_clusters
    
    def get_poi_candidates(self, allpoi_idList:list, must_see_poi_idList:list, req_topk_pois_idList:list, min_num_candidate:int, tresh:int, pseudo_must_see_pois: list=[]):
        poi_candidates, num_clutsters, selected_clusters, mark_citywalk = [], 9999, [], True
        cur_ids = req_topk_pois_idList

        for poi in pseudo_must_see_pois:
            pass
        for poi in must_see_poi_idList:
            pass

        if self.citywalk:
            clusters = self.getclusters()