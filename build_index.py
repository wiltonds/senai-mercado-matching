"""
build_index.py
----------------
1. Carrega o catálogo de cursos SENAI (ilustrativo) e as vagas de mercado
   (ilustrativas).
2. Vetoriza as ementas dos cursos e constrói um índice FAISS.
3. Para cada vaga, busca os cursos mais similares semanticamente.
4. Salva os artefatos (vectorizer, índice, dados) para uso no app Streamlit.
5. Imprime um relatório de matching para inspeção rápida.

Uso:
    python src/build_index.py
"""

import json
import os
import sys

import faiss
import joblib
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data"))

from matching import build_faiss_index, build_vectors, search  # noqa: E402
from courses_senai_demo import SENAI_COURSES  # noqa: E402
from vagas_mercado_demo import VAGAS_MERCADO  # noqa: E402

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")


def main():
    os.makedirs(MODELS_DIR, exist_ok=True)

    print("1) Vetorizando ementas dos cursos SENAI...")
    course_texts = [c["ementa"] for c in SENAI_COURSES]
    course_vectors, vectorizer = build_vectors(course_texts)

    print("2) Construindo índice FAISS...")
    index = build_faiss_index(course_vectors)
    print(f"   Índice construído com {index.ntotal} cursos, dimensão {course_vectors.shape[1]}")

    print("3) Buscando os cursos mais similares para cada vaga...\n")
    report = []
    for vaga in VAGAS_MERCADO:
        query_vector, _ = build_vectors([vaga["descricao"]], vectorizer=vectorizer)
        scores, indices = search(index, query_vector, top_k=3)

        matches = []
        print(f"VAGA: {vaga['titulo']}")
        for score, idx in zip(scores, indices):
            curso = SENAI_COURSES[idx]
            print(f"   -> {curso['curso']:50s} (similaridade: {score:.3f})")
            matches.append({"curso": curso["curso"], "codigo": curso["codigo"], "similaridade": float(score)})
        print()

        report.append({"vaga_id": vaga["id"], "vaga_titulo": vaga["titulo"], "matches": matches})

    print("4) Salvando artefatos em /models ...")
    joblib.dump(vectorizer, os.path.join(MODELS_DIR, "tfidf_vectorizer.joblib"))
    faiss.write_index(index, os.path.join(MODELS_DIR, "courses.index"))
    with open(os.path.join(MODELS_DIR, "matching_report.json"), "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("Concluído. Artefatos salvos em /models.")


if __name__ == "__main__":
    main()
