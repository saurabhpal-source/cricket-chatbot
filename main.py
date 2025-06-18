import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LLM and memory
llm = ChatOpenAI(temperature=0.7, openai_api_key=api_key)
memory = ConversationBufferMemory()

# Set up Wikipedia search tool
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

def cricket_chatbot(question):
    if "cricket" in question.lower():
        return wiki.run(question)
    else:
        chat = ConversationChain(llm=llm, memory=memory)
        return chat.run(question)

# Main loop
while True:
    query = input("\nAsk about cricket 🏏 (type 'exit' to stop): ")
    if query.lower() == "exit":
        break
    answer = cricket_chatbot(query)
    print(f"\n🤖 Chatbot: {answer}")
