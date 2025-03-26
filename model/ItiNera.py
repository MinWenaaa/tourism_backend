import json
import re
import os
import  concurrent.futures

import numpy as np
from model.Utils.proxy_call import ProxyCall
from model.Utils.prompts import process_input_prompt
from model.Utils.search_engine import SearchEngine

class ItiNera:
    def __init__(self, user_input: str, provider: str, model: str):
        self.proxy = ProxyCall(provider=provider)
        self.model = model
        parsed_input = self.parser_user_input(user_input=user_input)
        self.must_see_poi_names, self.itinerary_pos_reqs, self.itinerary_neg_reqs, self.user_pos_reqs, self.user_neg_reqs, self.start_poi, self.end_pos = self.struct_user_request(parsed_input)
        self.search_engine = SearchEngine(os.path.join("model", "chroma_db"))

    def parser_user_input(self, user_input: str):
        """解析用户需求"""
        response = self.proxy.chat(
            messages = [
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': process_input_prompt(user_input=user_input)}],
            model = self.model
        )
        print(response)
        try:
            return json.loads(response)
        except:
            match = re.search(r'\[(.*?)\]', response, re.DOTALL)
            if match:
                json_str = match.group(0)
                try:
                    return json.loads(json_str)
                except json.JSONDecodeError:
                    print("Found string is not a valid JSON.")
            else:
                print("No JSON found in the string.")
            return {}
        
    def struct_user_input(self, structured_input):
        must_see_poi_names = []
        itinerary_pos_reqs, itinerary_neg_reqs = [], []
        user_pos_reqs, user_neg_reqs = [], []
        start_poi, end_poi = None, None

        for req in structured_input:
            if req["type"] is None:
                req["type"] = "地点"
            if req["type"] == "行程":
                itinerary_pos_reqs.append(req["pos"])
                if req["neg"] != None:
                    itinerary_neg_reqs.append(req["neg"])
            
            elif req["type"] in ["地点", "起点", "终点"]:
                if req["mustsee"] == True:
                    must_see_poi_names.append(req["pos"])    
                user_pos_reqs.append(req["pos"])
                user_neg_reqs.append(req["neg"])
                if req["type"] == "起点":
                    start_poi = req["pos"]
                if req["type"] == "终点":
                    end_poi = req["pos"]
            else:
                raise ValueError
        if len(user_pos_reqs) == 0:
            user_pos_reqs = itinerary_pos_reqs
            
        return must_see_poi_names, itinerary_pos_reqs, itinerary_neg_reqs, user_pos_reqs, user_neg_reqs, start_poi, end_poi

    def get_reqs_topk(self):
        """每一对需求的最适配点与分数和最高的点"""
        def process_request(user_pos_req, user_neg_req):
            top_k = self.min_poi_candidate_num
            req_pois, score_list = self.search_engine.query(desc = (user_pos_req, user_neg_req), top_k = top_k)
            psedo_must_see_loc = [int(poi) for poi in req_pois[:2] if poi not in psedo_must_see_pois]
            return req_pois, score_list, psedo_must_see_loc

        all_reqs_topk, all_score, result, psedo_must_see_pois = [], [], [], []
        if len(self.user_pos_reqs) > 1:
            with concurrent.futures.ThreadPoolExcutor() as executor: 
                for req_pois, score_list, psedo_must_see_loc in executor.map(process_request, self.user_pos_reqs, self.user_neg_reqs):
                    psedo_must_see_pois.extend(psedo_must_see_loc)
                    all_scores.append(score_list)
                    all_reqs_topk.append(req_pois)
        elif len(self.user_pos_reqs) == 1:
            neg_req = self.user_neg_reqs[0] if self.user_neg_reqs else None
            req_pois, psedo_must_see_loc =  process_request(self.user_pos_reqs[0], neg_req)
            psedo_must_see_pois.extend(psedo_must_see_loc)
            all_reqs_topk.append(req_pois)
        else:
            raise ValueError("No positive request found")
        
        all_reqs_topk = np.concatenate(all_reqs_topk, axis = 0)
        all_scores = np.concatenate(all_scores, axis = 0)
        unique_ids = np.unique(all_reqs_topk)

        # 每个id的分数总和
        score_sum = [all_score[all_reqs_topk==ID].sum() for ID in unique_ids]
        sorted_id = all_reqs_topk[score_sum.argsort()]
        return sorted_id, psedo_must_see_loc

        
    def get_poi_candidates(self, req_topk_pois: list):
        pass

    def solve(self):
        req_topk_pois_id, pseudo_must_see_pois = self.get_reqs_topk()
        