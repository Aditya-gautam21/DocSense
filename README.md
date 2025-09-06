# DocSense

**DocSense** is a lightweight yet powerful Python-based application for document processing and analysis. Built with Streamlit, FastAPI, and LangChain, this tool enables:

- **PDF Comparison**:
  - Document-level cosine similarity comparisons
  - Sentence-level and preprocessed sentence-level similarity
- **ChatBot Interaction**:
  - Conversational access to PDF content using LLMs like LLAMA 3 and Google Gemini

---

## 🚀 Features

- **Multiple Comparison Modes**  
  - Full-document, sentence-level, and preprocessed scans

- **Flexible Embeddings**  
  - Supports Count Vectorizer, TF‑IDF, and `all-MiniLM-L6-v2`

- **Chat Interface**  
  - Load PDFs into ChromaDB and interact via chatbot

- **Modular, Clean Codebase**  
  - Organized files for extraction, preprocessing, embeddings, and LLM integration

---

## 📦 Requirements

- Python 3.8+
- `pip`

---

## ⚙️ Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/Aditya-gautam21/DocSense.git
   cd DocSense
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following:
   ```env
   GOOGLE_API_KEY=your-google-api-key
   DEPLOYED=False
   ```

4. Set up LLAMA 3 and OLLAMA:
   ```bash
   ollama run llama3
   ```

---

## ▶️ Usage Instructions

### Run the App
```bash
streamlit run app.py
```

### In the Web Interface

- **Home Page**:
  - Upload two PDFs
  - Choose comparison mode and embedding
  - Submit to view similarity scores

- **ChatBot Page**:
  - Upload PDFs and preprocess into vector DB
  - Select LLM (LLAMA 3 or Gemini)
  - Interact using natural language queries

---

## 📂 Project Structure

```
DocSense/
├── app.py                # Main Streamlit interface
├── compare.py            # Similarity comparison logic
├── pdf_extractor.py      # PDF text extraction
├── text_preprocessing.py # Text cleanup and preparation
├── chain.py              # LLM chaining logic
├── result.py             # Post-processing chatbot outputs
├── userinput.py          # Streamlit input handlers
├── vectorstore.py        # ChromaDB integration
├── htmlTemplates.py      # UI HTML templates (if any)
├── requirements.txt      # Python dependencies
└── .env                  # API keys and config (not committed)
```

---

## 🌐 Configuration & Deployment

- Set environment variables in `.env`:
  - `GOOGLE_API_KEY`
  - `DEPLOYED` (e.g., `True` for production)
- Use `ollama run llama3` to launch the LLM backend
- Set up persistent vector DB via `vectorstore.py`

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/my-feature`)  
3. Commit your changes (`git commit -m "Add awesome feature"`)  
4. Push and open a Pull Request  

---

## 📜 License

This project is open-source under the **MIT License**. Feel free to use, modify, and distribute! (Check `LICENSE` file for details.)

---

## 🙏 Acknowledgements

- **Streamlit** – UI framework  
- **LangChain** – LLM orchestration  
- **Chroma Vector DB** – for storing embeddings  
- **LLAMA 3 & Google Gemini** – LLMs powering the chatbot

---

## ⭐ About

DocSense streamlines PDF content comparison and conversational querying via powerful embedding techniques and LLMs.
