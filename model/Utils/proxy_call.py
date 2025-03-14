from openai import OpenAI
from model.Utils.prompts import process_input_prompt
import os

input1 = "去江汉路附近热闹点的地方走走，然后找个好吃的小吃街"

class ProxyCall:
    def __init__(self, provider: str):
        if provider == "dashscope":
            self.client = OpenAI( api_key=os.getenv("DASHSCOPE_API_KEY"), 
                base_url="https://dashscope.aliyuncs.com/compatible-mode/v1")
        if provider == "deepseek":
            self.client = OpenAI(api_key = os.getenv("DEEPSEEK_API_KEY"),
                base_url = "https://api.deepseek.com")
        

    def chat(self, messages, model, temperature=0):
        response = self.client.chat.completions.create(
            model=model, 
            messages=messages)
        print(response)
        return response.choices[0].message.content
