from model.Utils.proxy_call import ProxyCall
from model.Utils.prompts import process_input_prompt

import json
import re

class ItiNera:
    def __init__(self, user_input: str, provider: str, model: str):
        self.proxy = ProxyCall(provider=provider)
        self.model = model
        parsed_input = self.parser_user_input(user_input=user_input)
        self.must_see_poi_names, self.itinerary_pos_reqs, self.itinerary_neg_reqs, self.user_pos_reqs, self.user_neg_reqs, self.start_poi, self.end_pos = self.parse_user_request(parsed_input)

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
        
    def parse_user_input(self, structured_input):
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
