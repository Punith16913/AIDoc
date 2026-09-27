import streamlit as st
import os
from dotenv import load_dotenv
from src.document_loader import process_document
from src.vector_store import build_vector_store
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="AIDoc - Technical Assistant", page_icon="🤖")
st.title("🤖 AIDoc: Document Intelligence Assistant")

api_key = st.sidebar.text_input("Enter Gemini API Key", type="password") or os.getenv("GOOGLE_API_KEY")

uploaded_file = st.file_uploader("Upload Documentation (PDF or TXT)", type=["pdf", "txt"])

if uploaded_file and api_key:
    # Ensure temporary data folder exists and save file
    os.makedirs("./data", exist_ok=True)
    temp_path = f"./data/{uploaded_file.name}"
    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing document & generating embeddings..."):
        chunks = process_document(temp_path)
        vector_db = build_vector_store(chunks, api_key)
        retriever = vector_db.as_retriever(search_kwargs={"k": 3})
        st.sidebar.success("Document Indexed Successfully!")

    user_query = st.text_input("Ask a question about your uploaded document:")
    
    if user_query:
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
        
        system_prompt = (
            "You are a helpful assistant for technical documentation. "
            "Use the following retrieved context to answer the user's question accurately. "
            "If you do not know the answer based on the context, state that explicitly.\n\n"
            "Context:\n{context}"
        )
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}")
        ])
        
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        
        with st.spinner("Analyzing document context..."):
            response = rag_chain.invoke({"input": user_query})
            st.write("### Answer")
            st.write(response["answer"])
            
            with st.expander("Show Retrieved Document Chunks"):
                for idx, doc in enumerate(response["context"]):
                    st.markdown(f"**Chunk {idx+1}:**")
                    st.text(doc.page_content)
elif not api_key:
    st.info("Please enter your Gemini API key in the sidebar to get started.")