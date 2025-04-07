
from llama_index.llms.huggingface_api import HuggingFaceInferenceAPI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.chat_engine import ContextChatEngine
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.base.llms.types import ChatMessage, MessageRole
import streamlit as st
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.chat_engine import ContextChatEngine
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

# llm
hf_model = "mistralai/Mistral-7B-Instruct-v0.3"
llm = HuggingFaceInferenceAPI(model_name = hf_model, task = "text-generation")

# embeddings
embedding_model = "sentence-transformers/all-MiniLM-l6-v2"
embeddings_folder = "/content/"
embeddings = HuggingFaceEmbedding(model_name=embedding_model,
                                  cache_folder=embeddings_folder)

# load Vector Database
storage_context = StorageContext.from_defaults(persist_dir="/content/Vector_index")
vector_index = load_index_from_storage(storage_context, embed_model=embeddings)

# retriever
retriever = vector_index.as_retriever(similarity_top_k=2)

# prompt
prompts = [
    ChatMessage(role=MessageRole.SYSTEM, content="You are a nice chatbot having a conversation with a human."),
    ChatMessage(role=MessageRole.SYSTEM, content="Answer the question based only on the following context and previous conversation."),
    ChatMessage(role=MessageRole.SYSTEM, content="Keep your answers short and succinct.")
]

# memory
memory = ChatMemoryBuffer.from_defaults()


# bot with memory
@st.cache_resource
def init_bot():
    return ContextChatEngine(llm=llm, retriever=retriever, memory=memory, prefix_messages=prompts)
rag_bot = init_bot()


##### streamlit #####

st.title("Footprint Analyzer")


# Display chat messages from history on app rerun
for message in rag_bot.chat_history:
  if hasattr(message, "blocks") and message.blocks:  # Check if blocks exist and are not empty
    with st.chat_message(message.role):
        st.markdown(message.blocks[0].text)


# React to user input
if prompt := st.chat_input("Curious minds wanted!"):

    # Display user message in chat message container
    st.chat_message("human").markdown(prompt)

    # Begin spinner before answering question so it's there for the duration
    with st.spinner("Going down the rabbithole for answers..."):

        # send question to chain to get answer
        answer = rag_bot.chat(prompt)

        # extract answer from dictionary returned by chain
        response = answer.response

        # Display chatbot response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
