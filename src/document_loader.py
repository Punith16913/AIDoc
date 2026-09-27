from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def process_document(file_path: str):
    """Loads a PDF or TXT document and splits it into searchable chunks."""
    if file_path.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)
        
    docs = loader.load()
    
    # Split text into overlapping chunks for RAG retrieval
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=150
    )
    return text_splitter.split_documents(docs)