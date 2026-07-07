"""
vagas_mercado_demo.py
-----------------------
Descrições de vagas ILUSTRATIVAS, escritas para demonstrar a busca semântica
entre "o que o mercado pede" e "o que a SENAI oferece". Temática alinhada aos
gaps identificados na sua análise de CAGED (TI como maior gap, Segurança do
Trabalho como oportunidade de expansão geográfica).

IMPORTANTE: são exemplos ilustrativos, não vagas reais coletadas do CAGED,
Novo CAGED ou de portais de emprego. Servem para validar a arquitetura de
matching — substitua por descrições reais de vagas quando disponíveis
(ex.: campo de "descrição da ocupação" de fontes de vagas, se existir, ou
descrições de vagas coletadas de portais de emprego regionais).
"""

VAGAS_MERCADO = [
    {
        "id": "V001",
        "titulo": "Desenvolvedor(a) Full Stack Júnior",
        "descricao": "Buscamos profissional para desenvolver e manter aplicações web, "
                      "trabalhando com banco de dados, controle de versão e "
                      "metodologias ágeis de desenvolvimento de software.",
    },
    {
        "id": "V002",
        "titulo": "Analista de Suporte de TI",
        "descricao": "Responsável por atendimento a usuários, manutenção de redes "
                      "locais, configuração de servidores e resolução de problemas de "
                      "infraestrutura de tecnologia da informação.",
    },
    {
        "id": "V003",
        "titulo": "Analista de Dados Júnior",
        "descricao": "Vaga para profissional que irá tratar e analisar dados "
                      "empresariais, construir relatórios e painéis de indicadores, e "
                      "automatizar processos manuais repetitivos.",
    },
    {
        "id": "V004",
        "titulo": "Técnico de Segurança do Trabalho",
        "descricao": "Profissional responsável por identificar riscos ocupacionais, "
                      "garantir conformidade com normas regulamentadoras e conduzir "
                      "treinamentos de uso de equipamentos de proteção.",
    },
    {
        "id": "V005",
        "titulo": "Consultor de Adequação Normativa para Pequenas Empresas",
        "descricao": "Atuação em diagnóstico de conformidade regulatória para micro e "
                      "pequenas empresas, com foco em baixo custo de implementação e "
                      "planos de ação simplificados.",
    },
    {
        "id": "V006",
        "titulo": "Técnico de Automação e Instrumentação",
        "descricao": "Vaga para atuação na programação e manutenção de controladores "
                      "lógicos programáveis, sensores industriais e sistemas "
                      "automatizados de produção.",
    },
    {
        "id": "V007",
        "titulo": "Técnico de Manutenção Industrial",
        "descricao": "Responsável pelo diagnóstico e reparo de equipamentos "
                      "eletroeletrônicos e mecânicos, leitura de esquemas técnicos e "
                      "manutenção preventiva de linhas de produção.",
    },
    {
        "id": "V008",
        "titulo": "Auxiliar de Logística e Estoque",
        "descricao": "Vaga para apoio em gestão de estoques, conferência de "
                      "mercadorias, roteirização de entregas e uso de sistemas de "
                      "controle logístico.",
    },
    {
        "id": "V009",
        "titulo": "Assistente Administrativo",
        "descricao": "Rotinas administrativas, atendimento ao cliente, apoio em "
                      "processos financeiros simples e organização de documentos para "
                      "escritório de médio porte.",
    },
    {
        "id": "V010",
        "titulo": "Técnico em Controle de Qualidade Alimentar",
        "descricao": "Atuação em controle de qualidade e segurança alimentar em "
                      "indústria de alimentos, seguindo boas práticas de fabricação e "
                      "normas sanitárias vigentes.",
    },
]
