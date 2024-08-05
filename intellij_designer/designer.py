import intellij_designer.template as template
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_chroma import Chroma
from langchain.agents import initialize_agent
from langchain_community.llms import Tongyi
import os
#from langchain_mistralai import ChatMistralAI
#from langchain_core.messages import HumanMessage,ToolMessage


def get_info(requirement: str) ->dict:
    """
    获取用户对旅行的描述信息。
    """

    llm = ChatOpenAI(
	api_key=os.getenv("ALI_API_KEY"),
	base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
	model="qwen-turbo"
)
    
    output_parser = JsonOutputParser(pydantic_object=template.Requirement)
    prompt = PromptTemplate(
    template="提取用户对旅行的需求信息，没有提到或无特别要求或不需要则返回“无”.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)
    
    chain = prompt | llm | output_parser
    result=chain.invoke({"query":requirement})
    return result



def get_resort(query: str, num: int) -> list:
    """
    根据对景点的描述与数量选择景点。
    """
    #embedding.get_vectorstore()
    embedding_model = DashScopeEmbeddings(dashscope_api_key=os.getenv("ALI_API_KEY"))
    db3 = Chroma(
        persist_directory="intellij_designer/chroma_db", 
        embedding_function=embedding_model
        )
    docs = db3.similarity_search(query, num)
    resorts = []
    for doc in docs:
        resort=doc.metadata.get("id")
        resorts.append(resort)
        
    return resorts


"""
def path():
    
    llm = ChatMistralAI(
        model="mistral-large-latest",
        api_key=os.getenv("MISTRAL_API_KEY")
    )
    Tools = []

    messages = [HumanMessage(template.path_query)]
    llm_with_tools = llm.bind_tools(Tools, tool_choice="any")

    ai_msg = llm_with_tools.invoke(messages)
    messages.append(ai_msg)

    print("start")
    for tool_call in ai_msg.tool_calls:
        selected_tool = get_distance
        tool_output = selected_tool.invoke(tool_call["args"])
        messages.append(ToolMessage(tool_output, tool_call_id=tool_call["id"]))

    print(messages)

    result = llm_with_tools.invoke(messages)

    print(result)
    """

if __name__=="__main__":
    print("???")
    """
    llm=Tongyi(
        temperature=1,
        dashscope_api_key=os.getenv("ALI_API_KEY"),
    )

    agent = initialize_agent(
        tools=[distance_tool], 
        llm=llm, 
        agent="zero-shot-react-description", 
        verbose=True)
    
    result=agent.invoke(template.path_query)
    """
