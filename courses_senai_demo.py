"""
courses_senai_demo.py
----------------------
Catálogo ILUSTRATIVO de cursos SENAI, com ementas de exemplo.

IMPORTANTE (transparência metodológica):
Estas ementas são exemplos ILUSTRATIVOS escritos para fins de demonstração
da arquitetura de busca semântica — não são as ementas oficiais e completas
do catálogo real da SENAI-AL. As categorias de curso (Segurança do Trabalho,
Automação Industrial, TI, Logística, etc.) refletem áreas reais de atuação
do Sistema S, mas o texto específico de cada ementa foi escrito para este
protótipo. Substitua pelo conteúdo real das ementas institucionais antes de
qualquer uso em produção.
"""

SENAI_COURSES = [
    {
        "codigo": "TI-001",
        "curso": "Técnico em Desenvolvimento de Sistemas",
        "ementa": "Formação em lógica de programação, desenvolvimento web front-end e "
                  "back-end, banco de dados relacionais, versionamento de código com Git "
                  "e metodologias ágeis para construção de aplicações de software.",
    },
    {
        "codigo": "TI-002",
        "curso": "Suporte e Infraestrutura de Redes",
        "ementa": "Instalação, configuração e manutenção de redes de computadores, "
                  "servidores, cabeamento estruturado, protocolos de rede e suporte "
                  "técnico a usuários e sistemas operacionais.",
    },
    {
        "codigo": "TI-003",
        "curso": "Análise de Dados e Automação de Processos",
        "ementa": "Coleta, tratamento e análise de dados com planilhas e ferramentas de "
                  "BI, automação de rotinas repetitivas, introdução a Python para análise "
                  "de dados e construção de dashboards para tomada de decisão.",
    },
    {
        "codigo": "SST-001",
        "curso": "Técnico em Segurança do Trabalho",
        "ementa": "Identificação e prevenção de riscos ocupacionais, normas "
                  "regulamentadoras (NRs), elaboração de laudos técnicos, uso de "
                  "equipamentos de proteção individual e coletiva, e gestão de saúde e "
                  "segurança ocupacional em ambientes industriais.",
    },
    {
        "codigo": "SST-002",
        "curso": "Gestão de Riscos Ocupacionais em Pequenas Empresas",
        "ementa": "Diagnóstico simplificado de riscos para micro e pequenas empresas, "
                  "adequação a normas regulamentadoras com baixo custo, elaboração de "
                  "planos de ação preventivos e acompanhamento de conformidade.",
    },
    {
        "codigo": "AUT-001",
        "curso": "Técnico em Automação Industrial",
        "ementa": "Programação de controladores lógicos programáveis (CLPs), pneumática "
                  "e hidráulica industrial, sensores e atuadores, manutenção de sistemas "
                  "automatizados de linha de produção.",
    },
    {
        "codigo": "AUT-002",
        "curso": "Manutenção de Sistemas Eletroeletrônicos",
        "ementa": "Diagnóstico e reparo de circuitos eletrônicos, instrumentação "
                  "industrial, leitura de esquemas elétricos e manutenção preventiva e "
                  "corretiva de equipamentos industriais.",
    },
    {
        "codigo": "LOG-001",
        "curso": "Técnico em Logística",
        "ementa": "Gestão de estoques, cadeia de suprimentos, roteirização de "
                  "transporte, armazenagem e distribuição, e uso de sistemas de gestão "
                  "logística (WMS/TMS).",
    },
    {
        "codigo": "MEC-001",
        "curso": "Técnico em Eletromecânica",
        "ementa": "Manutenção mecânica e elétrica de máquinas industriais, leitura de "
                  "desenho técnico, alinhamento e balanceamento de equipamentos "
                  "rotativos, e boas práticas de manutenção preditiva.",
    },
    {
        "codigo": "GES-001",
        "curso": "Técnico em Administração e Gestão Empresarial",
        "ementa": "Fundamentos de gestão de pessoas, processos administrativos, "
                  "atendimento ao cliente, noções de finanças empresariais e rotinas de "
                  "escritório para pequenas e médias empresas.",
    },
    {
        "codigo": "ALI-001",
        "curso": "Técnico em Alimentos",
        "ementa": "Boas práticas de fabricação, controle de qualidade e segurança "
                  "alimentar, processamento e conservação de alimentos, e normas "
                  "sanitárias para indústria alimentícia.",
    },
    {
        "codigo": "CIV-001",
        "curso": "Técnico em Edificações",
        "ementa": "Leitura e interpretação de projetos arquitetônicos, técnicas "
                  "construtivas, controle de qualidade em obras, orçamento e "
                  "planejamento de execução de edificações.",
    },
]
