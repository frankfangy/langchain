from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
 
# 初始化GLM-4模型
chat = ChatZhipuAI(
    model="glm-4",
    temperature=0.5 
  )

# 构建消息对象
messages = [
    AIMessage(content="你好。"),
    SystemMessage(content="你是一位诗人。"),
    HumanMessage(content="用四行写一首关于人工智能的短诗。"),
]

# 调用模型生成回复
response = chat.invoke(messages)
print(response.content)