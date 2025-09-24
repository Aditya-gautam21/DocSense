import os
from vectorstore import Vectorstore
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_together import ChatTogether 
from langchain.schema import HumanMessage 

class Chain:
    def get_conversation_chain(self, vectorstore):
        llm = ChatTogether(
            together_api_key=os.getenv('TOGETHER_API_KEY'),  
            model="meta-llama/Llama-3-70b-chat-hf",      
            temperature=0.7
        )

        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        return conversation_chain
