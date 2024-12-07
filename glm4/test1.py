from langchain_community.chat_models import ChatZhipuAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# 设置API密钥
import os
os.environ["ZHIPUAI_API_KEY"] = os.environ["ZP_KEY"]  # 填入你自己的API Key 
print( os.environ["ZHIPUAI_API_KEY"] )
# 初始化GLM-4模型
chat = ChatZhipuAI(
    model="glm-4",
    temperature=0.5,
    zhipuai_api_key= os.environ["ZP_KEY"] , 
    zhipuai_api_base= 'https://open.bigmodel.cn/api/paas/v4/chat/completions'
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