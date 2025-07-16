from langchain_text_splitters import CharacterTextSplitter

class Chunks:
    def __init__(self):
        self.text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    
    def get_text_chunks(self,text):
        return self.text_splitter.split_text(text)