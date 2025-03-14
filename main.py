from model.ItiNera import ItiNera

provider = "deepseek"
model = "deepseek-chat"

provider2 = "dashscope"
model2 = "qwen-plus"

input1 = "去江汉路附近热闹点的地方走走，然后找个好吃的小吃街"

def run(input: str):
    day_planner = ItiNera(user_input = input1, provider=provider2, model=model2)
    

if __name__ == '__main__':
    run(input)