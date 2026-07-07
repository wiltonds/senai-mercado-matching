"""
matching.py
------------
Motor de busca semântica entre vagas de mercado e cursos SENAI.

Arquitetura (a mesma de um pipeline RAG, aplicada a matching em vez de
geração de texto):

    texto (curso ou vaga) -> vetor -> índice vetorial (FAISS) -> busca por
    similaridade -> top-k mais parecidos

NOTA DE TRANSPARÊNCIA TÉCNICA:
Idealmente, a vetorização usaria embeddings densos de um modelo de linguagem
pré-treinado (ex.: Sentence-BERT multilíngue), que capturam significado além
de palavras exatas. Neste protótipo usamos TF-IDF como vetorização — por
restrição de acesso a modelos de embeddings pré-treinados no ambiente em que
foi construído — mas a arquitetura de indexação e busca (FAISS) é
exatamente a mesma que seria usada em produção. Trocar TF-IDF por
embeddings de um SentenceTransformer é uma mudança de poucas linhas em
`build_vectors()`, sem alterar o restante do pipeline.
"""

import os
from typing import List, Tuple

import faiss
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

from preprocessing import preprocess_to_string

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")


def build_vectors(texts: List[str], vectorizer: TfidfVectorizer = None) -> Tuple[np.ndarray, TfidfVectorizer]:
    """Converte uma lista de textos em vetores densos normalizados (float32),
    prontos para indexação no FAISS com similaridade por produto interno
    (equivalente a similaridade de cosseno, já que normalizamos os vetores).
    """
    processed = [preprocess_to_string(t) for t in texts]

    if vectorizer is None:
        vectorizer = TfidfVectorizer(max_features=2000, ngram_range=(1, 2))
        matrix = vectorizer.fit_transform(processed)
    else:
        matrix = vectorizer.transform(processed)

    dense = matrix.toarray().astype("float32")
    faiss.normalize_L2(dense)  # normaliza para que produto interno = cosseno
    return dense, vectorizer


def build_faiss_index(vectors: np.ndarray) -> faiss.Index:
    """Cria um índice FAISS simples (busca exata por produto interno)."""
    dim = vectors.shape[1]
    index = faiss.IndexFlatIP(dim)  # Inner Product = similaridade de cosseno (vetores normalizados)
    index.add(vectors)
    return index


def search(index: faiss.Index, query_vector: np.ndarray, top_k: int = 3):
    """Busca os top_k vetores mais similares no índice.

    Retorna (scores, indices) — scores em [-1, 1], mais próximo de 1 = mais
    similar (equivalente a similaridade de cosseno).
    """
    scores, indices = index.search(query_vector, top_k)
    return scores[0], indices[0]
