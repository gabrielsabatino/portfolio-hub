# 🌸 Classificador de Espécies Iris

Modelo de **Machine Learning supervisionado** para classificação de três espécies de flores Iris (*setosa*, *versicolor*, *virginica*) usando o algoritmo K-Nearest Neighbors.

---

## 🎯 Objetivo

Construir um classificador que, a partir das medidas de pétalas e sépalas de uma flor, consiga prever corretamente a sua espécie com **acurácia superior a 95%**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **scikit-learn** — biblioteca de Machine Learning
- **NumPy** — operações numéricas
- **Matplotlib** — visualização da matriz de confusão

---

## 📁 Estrutura do Projeto

```
classificador-iris/
├── classificador.py        # Script principal do modelo
└── README.md               # Este arquivo
```

---

## 📊 Sobre o Dataset

O dataset **Iris** é um clássico do aprendizado de máquina, contendo:

- **150 amostras** de flores
- **4 características** (comprimento e largura de sépalas e pétalas)
- **3 classes** (setosa, versicolor, virginica)
- **50 amostras** por classe

---

## 🚀 Como Executar

### Pré-requisitos

```bash
pip install scikit-learn numpy matplotlib
```

### Execução

```bash
python classificador.py
```

---

## 🧠 Como Funciona

1. **Carregamento dos dados** — usa o dataset Iris embutido no scikit-learn
2. **Divisão treino/teste** — 70% treino, 30% teste (com estratificação)
3. **Treinamento do modelo** — KNN com k=5 vizinhos
4. **Avaliação** — calcula acurácia, precision, recall e f1-score
5. **Visualização** — gera matriz de confusão
6. **Previsão** — demonstra uma predição em amostra de exemplo

---

## 📈 Resultados Esperados

| Métrica | Valor |
|---------|-------|
| **Acurácia** | ~97% |
| **Precision** | ~97% |
| **Recall** | ~97% |
| **F1-Score** | ~97% |

A matriz de confusão é gerada como `matriz_confusao.png`.

---

## 💡 Aprendizados

Este projeto demonstra conceitos fundamentais de Machine Learning:

- ✅ Carregamento de datasets do scikit-learn
- ✅ Divisão estratificada treino/teste
- ✅ Treinamento de modelo supervisionado (KNN)
- ✅ Avaliação de modelos com múltiplas métricas
- ✅ Matriz de confusão para análise de erros
- ✅ Predição em novos dados

---

## 🔄 Próximos Passos

- [ ] Testar outros algoritmos (Random Forest, SVM, Logistic Regression)
- [ ] Aplicar validação cruzada (cross-validation)
- [ ] Otimizar hiperparâmetros com GridSearchCV
- [ ] Criar interface web para predições em tempo real

---

## 👤 Autor

**Gabriel Sabatino**

- GitHub: [@gabrielsabatino](https://github.com/gabrielsabatino)
- LinkedIn: [Seu Perfil](https://linkedin.com/in/gabriel-sabatino-10b9b340b)

---

⬅️ [Voltar ao repositório principal](../../README.md)
