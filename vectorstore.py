import os
from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone as PineconeClient, ServerlessSpec
from langchain_pinecone import Pinecone


class Vectorstore:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(model_name="hkunlp/instructor-large")
        self.index_name = "pdf-chat-index"

        # Initialize Pinecone client
        self.pc = PineconeClient(api_key=os.getenv("PINECONE_API_KEY"))

        # Create index if it doesn't exist
        if self.index_name not in self.pc.list_indexes().names():
            self.pc.create_index(
                name=self.index_name,
                dimension=768,  # Depends on your embedding model
                metric="cosine",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1"
                )
            )

    def fetch_vectorstores(self, chunks):
        # Use LangChain's Pinecone wrapper to store the data
        vectorstore = Pinecone.from_texts(
            texts=chunks,
            embedding=self.embeddings,
            index_name=self.index_name,
            namespace="pdf-chat"
        )
        return vectorstore
