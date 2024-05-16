import os 
import streamlit as st
from dotenv import load_dotenv
import openai

from llama_index.core import ServiceContext, VectorStoreIndex,SimpleDirectoryReader
from llama_index.llms.openai import OpenAI

load_dotenv()



openai.api_key = os.getenv("OPEN_API_KEY")

def main ():
    st.header("商品に関する質問をしてください")

    input_dir = "./data"

    try:
        reader = SimpleDirectoryReader(input_dir=input_dir,recursive=True)
        docs = reader.load_data()

        service_context = ServiceContext.from_defaults(
            llm=OpenAI(model="gpt-3.5-turbo",temperature=0.5,
                       system_prompt="あなたは提供されたデータセットの専門家です。ユーザーの質問に対して、的確な答えを出してください")
        )
        index = VectorStoreIndex.from_documents(docs,service_context=service_context)

        query = st.text_input("商品に関する質問を入力してください")

        if query:
            chat_engine = index.as_chat_engine(chat_mode="condense_question",verbose=True)
            response = chat_engine.chat(query)

            st.markdown(f"**回答**")
            st.write(response.response.strip())
    except Exception as e:
        st.error(f"データセット読み込みエラー:{e}")

if __name__ == '__main__':
    main()


