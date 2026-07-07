# 🎓 Busca Semântica: Cursos SENAI × Vagas de Mercado

Prova de conceito de um **motor de matching semântico** entre a demanda do
mercado de trabalho (vagas) e a oferta de cursos técnicos (SENAI), usando
banco vetorial (**FAISS**) — a mesma infraestrutura usada em pipelines de
RAG, aplicada aqui a um problema real de inteligência de mercado.

Projeto desenvolvido como extensão prática do trabalho de Inteligência de
Mercado na FIEA/SENAI-AL, e como preparação técnica para a bolsa de Inovação
**ICT ITAÚ / Inova Talentos**.

---

## O problema real que este projeto resolve

A análise de CAGED cruzada com o portfólio de cursos identifica gaps por
**categoria oficial de ocupação (CBO)** — uma classificação rígida. Descrições
de vaga em texto livre, porém, usam palavras diferentes para pedir
competências parecidas às ensinadas em um curso já existente, e a
classificação oficial nem sempre captura essa correspondência.

Este protótipo testa uma abordagem alternativa: representar a **ementa de
cada curso** e a **descrição de cada vaga** como vetores, e buscar
correspondências por similaridade — encontrando conexões que a categorização
oficial poderia não capturar.

---

## ⚠️ Transparência sobre os dados e a metodologia

**Dados:** as ementas de curso (`data/courses_senai_demo.py`) e as descrições
de vaga (`data/vagas_mercado_demo.py`) são **exemplos ilustrativos**, escritos
para validar a arquitetura — não são o catálogo oficial da SENAI-AL nem vagas
reais coletadas de CAGED/Novo CAGED ou portais de emprego. As categorias
refletem áreas reais de atuação do Sistema S (TI, Segurança do Trabalho,
Automação Industrial etc.), mas o texto específico de cada ementa/vaga é de
demonstração.

**Vetorização:** o ideal seria usar *embeddings* densos de um modelo de
linguagem pré-treinado (ex.: Sentence-BERT multilíngue), que captam sinônimos
e significado além da palavra exata. Este protótipo usa **TF-IDF**, por
restrição de acesso a modelos de embeddings pré-treinados no ambiente em que
foi construído (sem acesso ao Hugging Face Hub). A infraestrutura de busca
vetorial (**FAISS**) é real e idêntica à de produção — trocar TF-IDF por
embeddings de um `SentenceTransformer` é uma mudança de poucas linhas em
`src/matching.py::build_vectors()`, sem alterar o restante do pipeline.

---

## Resultado observado (honesto, incluindo os erros)

Rodando `python src/build_index.py` com os dados de exemplo, o TF-IDF acertou
o curso correspondente como primeiro colocado em 9 de 10 vagas de teste. O
único erro relevante:

> **Vaga "Analista de Dados Júnior"** → o modelo colocou em 1º lugar
> "Administração e Gestão Empresarial", e só em 2º "Análise de Dados e
> Automação de Processos" — porque a vaga usa a palavra "indicadores" e a
> ementa usa "dashboards"/"BI", termos que o TF-IDF não reconhece como
> sinônimos.

Esse erro é o argumento mais concreto para embeddings: um modelo como
Sentence-BERT captaria que "indicadores", "dashboards" e "BI" ocupam o mesmo
espaço semântico, mesmo sem repetir a palavra exata — o TF-IDF não consegue.

---

## Arquitetura

```
descrição da vaga (texto)
        │
        ▼
  pré-processamento (limpeza, tokenização, stopwords)
        │
        ▼
  vetorização (TF-IDF — ou embeddings, no upgrade futuro)
        │
        ▼
  busca no índice FAISS (similaridade de cosseno)
        │
        ▼
  top-k cursos mais similares, com score de similaridade
```

## Estrutura do repositório

```
senai-mercado-matching/
├── app/
│   └── streamlit_app.py        # Interface web de busca
├── src/
│   ├── preprocessing.py        # Limpeza, tokenização, stopwords (PT)
│   ├── matching.py             # Vetorização (TF-IDF) + índice FAISS + busca
│   └── build_index.py          # Constrói o índice e roda o matching de teste
├── data/
│   ├── courses_senai_demo.py   # Ementas ilustrativas de cursos
│   └── vagas_mercado_demo.py   # Descrições ilustrativas de vagas
├── models/                     # Índice FAISS + vectorizer (gerados)
├── requirements.txt
└── README.md
```

## Como rodar localmente

```bash
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python src/build_index.py         # constrói o índice e imprime o matching de teste
streamlit run app/streamlit_app.py
```

## Deploy no Streamlit Community Cloud

Mesmo processo do projeto de sentiment analysis: suba o repositório pro
GitHub, conecte em [share.streamlit.io](https://share.streamlit.io), aponte
para `app/streamlit_app.py`. Como o índice é pequeno (12 cursos), pode
rodar `build_index.py` no próprio boot do app, ou commitar `/models`
diretamente.

## Roadmap

- [ ] Substituir dados ilustrativos pelas ementas reais do catálogo SENAI-AL
      e por descrições reais de vagas (fonte a definir: portal de emprego
      regional, parceiros, ou coleta manual)
- [ ] Trocar TF-IDF por embeddings de Sentence-BERT multilíngue
- [ ] Avaliar a qualidade da busca com métricas de recall@k / MRR, usando um
      conjunto de pares vaga-curso validados manualmente como gabarito
- [ ] Expandir para um assistente conversacional (RAG completo): em vez de só
      listar cursos similares, gerar uma recomendação textual explicando por
      que aquele curso atende à vaga

## Autor

Wilton Costa — Analista de Inteligência de Mercado (FIEA/SENAI-AL) | Mestrando
em Management com ênfase em Data Science (Faulkner University).
