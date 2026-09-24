"""Executable semantic-matching demo using synthetic Portuguese text."""
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="SENAI Market Matching | Demo",page_icon="🎓",layout="wide")
st.title("🎓 SENAI Market Matching")
st.caption("Demo executável · vaga → representação textual → similaridade → ranking de cursos")

courses=[
("Automação Industrial e CLP","programação de CLP automação industrial sensores máquinas manutenção sistemas de controle"),
("Análise de Dados e BI","Python SQL indicadores dashboards Power BI análise de dados visualização métricas"),
("Segurança em Máquinas NR-12","segurança máquinas riscos industriais NR-12 prevenção acidentes proteção"),
("Manutenção Industrial","manutenção preventiva motores máquinas diagnóstico falhas manutenção industrial"),
("Gestão de Processos Industriais","processos produtividade qualidade indicadores melhoria contínua gestão"),
]
vacancies={
"Analista de Dados Júnior":"profissional para analisar dados, criar indicadores, dashboards e relatórios usando SQL Python e ferramentas de BI",
"Técnico de Automação":"programação de CLPs, sensores, sistemas automatizados e manutenção de equipamentos industriais",
"Analista de Manutenção":"planejamento de manutenção preventiva, diagnóstico de falhas e acompanhamento de equipamentos",
}
choice=st.selectbox("Vaga demonstrativa",list(vacancies))
query=vacancies[choice]
k=st.slider("Top-k",1,5,3)
texts=[x[1] for x in courses]
vec=TfidfVectorizer(stop_words=["de","da","do","e","em","para","com","a","o"]).fit(texts+[query])
X=vec.transform(texts+[query])
scores=cosine_similarity(X[-1],X[:-1])[0]
ranked=sorted(zip(scores,courses),reverse=True)[:k]
c1,c2,c3=st.columns(3)
c1.metric("Vaga","Demo")
c2.metric("Cursos indexados",len(courses))
c3.metric("Retrieval","TF-IDF + cosine")
st.divider()
st.subheader("Cursos recomendados")
for i,(score,(name,desc)) in enumerate(ranked,1):
    with st.container(border=True):
        a,b=st.columns([7,2])
        a.markdown(f"**{i}. {name}**")
        a.caption(desc)
        b.metric("Similaridade",f"{score:.3f}")
st.caption("DEMO — descrições e cursos são ilustrativos. O repositório também contém a implementação FAISS/TF-IDF.")
