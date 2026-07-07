"""
streamlit_app.py
-----------------
Interface web: busca semântica entre vagas de mercado e cursos SENAI,
usando FAISS como banco vetorial.

Executar localmente:
    streamlit run app/streamlit_app.py
"""

import os
import sys

import faiss
import joblib
import streamlit as st

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "src"))
sys.path.insert(0, os.path.join(BASE_DIR, "data"))

from matching import build_vectors, search  # noqa: E402
from courses_senai_demo import SENAI_COURSES  # noqa: E402
from vagas_mercado_demo import VAGAS_MERCADO  # noqa: E402

MODELS_DIR = os.path.join(BASE_DIR, "models")

st.set_page_config(page_title="Matching Curso x Mercado — SENAI", page_icon="🎓", layout="centered")

st.title("🎓 Busca Semântica: Cursos SENAI × Vagas de Mercado")
st.caption("Prova de conceito: banco vetorial (FAISS) aplicado à inteligência de mercado.")

with st.expander("ℹ️ Sobre este projeto e seus dados (leia antes de testar)"):
    st.markdown("""
    **O que este protótipo faz:** recebe a descrição de uma vaga de mercado e busca,
    por similaridade semântica, os cursos SENAI cujas ementas mais se aproximam —
    a mesma lógica de um pipeline de **busca vetorial / RAG**, aplicada a matching
    em vez de geração de texto.

    **Transparência sobre os dados:** as ementas de curso e as descrições de vaga
    usadas aqui são **exemplos ilustrativos**, escritos para validar a arquitetura —
    não são o catálogo oficial da SENAI-AL nem vagas reais coletadas do CAGED ou de
    portais de emprego. As categorias (TI, Segurança do Trabalho, Automação
    Industrial etc.) refletem áreas reais de atuação, mas o texto específico é de
    demonstração.

    **Transparência sobre a vetorização:** idealmente, este tipo de busca usaria
    *embeddings* densos de um modelo de linguagem pré-treinado (ex.: Sentence-BERT
    multilíngue), que captam sinônimos e significado além da palavra exata. Este
    protótipo usa **TF-IDF** como vetorização (por restrição de acesso a modelos de
    embeddings no ambiente em que foi construído), indexado com **FAISS** — a
    infraestrutura de busca vetorial é real e idêntica à de produção; só a forma de
    gerar o vetor mudaria.
    """)

if not os.path.exists(os.path.join(MODELS_DIR, "tfidf_vectorizer.joblib")):
    st.error("Índice não encontrado em /models. Rode `python src/build_index.py` primeiro.")
    st.stop()

vectorizer = joblib.load(os.path.join(MODELS_DIR, "tfidf_vectorizer.joblib"))
index = faiss.read_index(os.path.join(MODELS_DIR, "courses.index"))

st.subheader("1. Escolha uma vaga de exemplo ou digite a sua")
vaga_options = ["— digitar minha própria descrição —"] + [v["titulo"] for v in VAGAS_MERCADO]
choice = st.selectbox("Vaga:", vaga_options)

if choice == vaga_options[0]:
    descricao = st.text_area("Descrição da vaga:", height=100,
                              placeholder="Ex.: Buscamos profissional para programar CLPs e manter sistemas automatizados de produção...")
else:
    vaga_obj = next(v for v in VAGAS_MERCADO if v["titulo"] == choice)
    descricao = vaga_obj["descricao"]
    st.text_area("Descrição da vaga:", value=descricao, height=100, disabled=True)

top_k = st.slider("Quantos cursos mostrar (top-k):", min_value=1, max_value=5, value=3)

if st.button("Buscar cursos correspondentes", type="primary"):
    if not descricao.strip():
        st.warning("Digite ou selecione uma descrição de vaga primeiro.")
    else:
        query_vector, _ = build_vectors([descricao], vectorizer=vectorizer)
        scores, indices = search(index, query_vector, top_k=top_k)

        st.subheader("2. Cursos mais similares (busca vetorial)")
        for rank, (score, idx) in enumerate(zip(scores, indices), start=1):
            curso = SENAI_COURSES[idx]
            st.markdown(f"**{rank}. {curso['curso']}** ({curso['codigo']})")
            st.progress(max(float(score), 0.0))
            st.caption(f"Similaridade (cosseno via TF-IDF): {score:.3f}")
            with st.expander("Ver ementa"):
                st.write(curso["ementa"])
            st.divider()

st.caption(
    "Protótipo de inteligência de mercado — construído como preparação prática para a "
    "bolsa de Inovação ICT ITAÚ / Inova Talentos. Próximo passo planejado: substituir "
    "TF-IDF por embeddings de Sentence-BERT multilíngue quando houver acesso ao modelo, "
    "mantendo a mesma infraestrutura de índice FAISS."
)
