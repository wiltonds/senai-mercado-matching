"""
preprocessing.py
-----------------
Pré-processamento de texto em português para o pipeline de matching
curso <-> vaga. Mesma lógica do projeto de sentiment analysis (Camada 1),
adaptada para stopwords em português.
"""

import re
from typing import List

# Lista compacta de stopwords em português (evita dependência de download
# de corpora externos — mesma decisão de design do projeto de sentimento).
STOPWORDS_PT = {
    "a", "o", "as", "os", "um", "uma", "uns", "umas", "de", "do", "da", "dos", "das",
    "em", "no", "na", "nos", "nas", "por", "para", "com", "sem", "sob", "sobre",
    "e", "ou", "que", "se", "ao", "aos", "à", "às", "é", "são", "foi", "ser",
    "como", "mais", "mas", "também", "já", "muito", "bem", "não", "sim",
}

_TOKEN_RE = re.compile(r"[a-zA-ZÀ-ÿ]+")


def clean_text(text: str) -> str:
    return text.lower()


def tokenize(text: str) -> List[str]:
    return _TOKEN_RE.findall(text)


def remove_stopwords(tokens: List[str]) -> List[str]:
    return [t for t in tokens if t not in STOPWORDS_PT and len(t) > 2]


def preprocess(text: str) -> List[str]:
    cleaned = clean_text(text)
    tokens = tokenize(cleaned)
    tokens = remove_stopwords(tokens)
    return tokens


def preprocess_to_string(text: str) -> str:
    return " ".join(preprocess(text))
