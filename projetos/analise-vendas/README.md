# 📊 Análise Exploratória de Vendas

Projeto de análise de dados de vendas usando Python, Pandas e Matplotlib.

---

## 🎯 Objetivo

Realizar uma análise exploratória de dados (EDA) em um conjunto de vendas para:

- Identificar a categoria mais lucrativa
- Descobrir os produtos mais vendidos
- Calcular o ticket médio
- Visualizar tendências através de gráficos

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Pandas** — manipulação e análise de dados
- **NumPy** — operações numéricas
- **Matplotlib** — visualização de dados

---

## 📁 Estrutura do Projeto

```
analise-vendas/
├── dados/
│   └── vendas.csv          # Dataset com dados de vendas
├── analise_vendas.py       # Script principal de análise
└── README.md               # Este arquivo
```

---

## 🚀 Como Executar

### Pré-requisitos

Instale as dependências:

```bash
pip install pandas numpy matplotlib
```

### Execução

Na pasta do projeto, rode:

```bash
python analise_vendas.py
```

O script vai:
1. Carregar o dataset `dados/vendas.csv`
2. Mostrar estatísticas descritivas
3. Gerar um gráfico (`grafico_vendas.png`)
4. Exibir os principais insights no terminal

---

## 📈 Resultados Esperados

Ao executar, você verá no terminal:

- **Estatísticas descritivas** do dataset
- **Vendas totais por categoria**
- **Top 5 produtos mais vendidos**
- **Insights principais** (categoria mais lucrativa, ticket médio, etc.)

E será gerado um arquivo PNG com dois gráficos:
- Gráfico de barras das vendas por categoria
- Gráfico de barras horizontais dos top 5 produtos

---

## 💡 Aprendizados

Este projeto demonstra:

- ✅ Leitura de arquivos CSV com Pandas
- ✅ Agrupamento e agregação de dados (`groupby`)
- ✅ Estatísticas descritivas (`describe`)
- ✅ Visualização de dados com Matplotlib
- ✅ Geração de insights a partir de dados brutos

---

## 🔄 Próximos Passos

- [ ] Adicionar análise temporal (vendas por mês)
- [ ] Criar dashboard interativo com Plotly
- [ ] Implementar previsão de vendas com Machine Learning
- [ ] Adicionar testes unitários

---

## 👤 Autor

**Gabriel Sabatino**

- GitHub: [@gabrielsabatino](https://github.com/gabrielsabatino)
- LinkedIn: [Seu Perfil](https://linkedin.com/in/gabriel-sabatino-10b9b340b)

---

⬅️ [Voltar ao repositório principal](../../README.md)
