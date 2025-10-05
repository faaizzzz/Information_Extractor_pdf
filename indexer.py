#!/usr/bin/env python3
"""
Indexer for multi-PDF QA system using TF-IDF.
Includes auto PDF detection and short-answer extraction.
"""

import os
import re
import numpy as np
import pdfplumber
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


PDF_FOLDER = "pdfs"

# ------------------ Text Extraction ------------------

def extract_text_from_pdf(pdf_path):
    """Extract and join text from all pages of a PDF."""
    texts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                texts.append(text)
    return "\n".join(texts)

def clean_text(text):
    """Clean boilerplate, symbols, and excess whitespace."""
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'Version\s*\d+(\.\d+)?|Update|Note to Readers.*', '', text, flags=re.I)
    return text.strip()

def smart_chunk_text(text, chunk_size=300, overlap=50):
    """Split text into overlapping chunks for better retrieval."""
    words = text.split()
    chunks, i = [], 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunk = re.sub(r'(\d+\)|\d+\.)', '•', chunk)
        chunks.append(chunk.strip())
        i += chunk_size - overlap
    return chunks

# ------------------ Indexing ------------------

def index_pdfs(folder=PDF_FOLDER):
    """Index all PDFs in the folder and return vector store."""
    chunks, meta = [], []
    for fname in os.listdir(folder):
        if not fname.lower().endswith(".pdf"):
            continue
        path = os.path.join(folder, fname)
        text = clean_text(extract_text_from_pdf(path))
        doc_chunks = smart_chunk_text(text)
        chunks.extend(doc_chunks)
        meta.extend([{"source": fname}] * len(doc_chunks))

    vectorizer = TfidfVectorizer(stop_words="english", max_features=60000)
    X = vectorizer.fit_transform(chunks)
    print(f"✅ Indexed {len(chunks)} text chunks from {len(set(m['source'] for m in meta))} PDFs.")
    return {"vectorizer": vectorizer, "X": X, "chunks": chunks, "meta": meta}

def save_index(index, path="index.pkl"):
    joblib.dump(index, path)

def load_index(path="index.pkl"):
    return joblib.load(path)

# ------------------ Query & Answer ------------------

def auto_detect_doc(query):
    """Heuristic-based PDF detection by keywords."""
    q = query.lower()
    if any(w in q for w in ["cybersecurity", "nist", "risk", "framework"]):
        return "NIST.CSWP.04162018.pdf"
    elif any(w in q for w in ["transformer", "attention", "encoding"]):
        return "1706.03762v7.pdf"
    elif any(w in q for w in ["bert", "nlp", "language model"]):
        return "1810.04805v2.pdf"
    return None

def summarize_text(text):
    """Summarize long text into concise bullets."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    bullets = [f"• {s.strip()}" for s in sentences if len(s.strip()) > 25]
    summary = "\n".join(bullets[:5])
    return summary.strip() if summary else text.strip()

def answer_query(index, query, top_k=2):
    """Return short, readable answers."""
    vec = index["vectorizer"].transform([query])
    sims = cosine_similarity(vec, index["X"]).flatten()
    idx = np.argsort(-sims)[:top_k]
    results = [(float(sims[i]), summarize_text(index["chunks"][i]), index["meta"][i]) for i in idx]
    return results
