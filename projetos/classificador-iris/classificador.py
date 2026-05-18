"""
============================================================
CLASSIFICADOR DE ESPÉCIES DE FLORES IRIS
============================================================
Projeto: Classificador Iris
Autor: Gabriel Sabatino
Data: 2026
Descrição: Modelo de Machine Learning supervisionado para
           classificar três espécies de flores Iris (setosa,
           versicolor, virginica) com base em medidas das
           pétalas e sépalas. Usa o algoritmo K-Nearest
           Neighbors (KNN) do scikit-learn.
============================================================
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------------
# 1. CARREGAMENTO DOS DADOS
# ------------------------------------------------------------
print("=" * 60)
print("CLASSIFICADOR IRIS - PORTFOLIOHUB")
print("=" * 60)

iris = load_iris()
X = iris.data
y = iris.target

print(f"\n✓ Dataset carregado")
print(f"  Total de amostras: {X.shape[0]}")
print(f"  Características: {X.shape[1]} ({', '.join(iris.feature_names)})")
print(f"  Classes: {len(iris.target_names)} ({', '.join(iris.target_names)})")

# ------------------------------------------------------------
# 2. DIVISÃO TREINO / TESTE
# ------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

print(f"\n✓ Divisão treino/teste:")
print(f"  Treino: {X_train.shape[0]} amostras")
print(f"  Teste:  {X_test.shape[0]} amostras")

# ------------------------------------------------------------
# 3. TREINAMENTO DO MODELO
# ------------------------------------------------------------
print("\n📚 Treinando modelo KNN (k=5)...")
modelo = KNeighborsClassifier(n_neighbors=5)
modelo.fit(X_train, y_train)
print("✓ Modelo treinado com sucesso!")

# ------------------------------------------------------------
# 4. AVALIAÇÃO
# ------------------------------------------------------------
y_pred = modelo.predict(X_test)
acuracia = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("RESULTADOS")
print("=" * 60)
print(f"\n🎯 Acurácia: {acuracia * 100:.2f}%")
print("\n📋 Relatório de Classificação:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# ------------------------------------------------------------
# 5. MATRIZ DE CONFUSÃO
# ------------------------------------------------------------
cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(8, 6))
im = ax.imshow(cm, cmap="Blues")

ax.set_xticks(np.arange(len(iris.target_names)))
ax.set_yticks(np.arange(len(iris.target_names)))
ax.set_xticklabels(iris.target_names)
ax.set_yticklabels(iris.target_names)

# Anotar os valores
for i in range(len(iris.target_names)):
    for j in range(len(iris.target_names)):
        ax.text(j, i, cm[i, j], ha="center", va="center",
                color="white" if cm[i, j] > cm.max() / 2 else "black",
                fontsize=14, fontweight="bold")

ax.set_xlabel("Predito", fontsize=12)
ax.set_ylabel("Real", fontsize=12)
ax.set_title("Matriz de Confusão - Classificador Iris", fontsize=14, fontweight="bold")
plt.colorbar(im)
plt.tight_layout()
plt.savefig("matriz_confusao.png", dpi=100, bbox_inches="tight")
print("\n✓ Matriz de confusão salva: matriz_confusao.png")

# ------------------------------------------------------------
# 6. PREVISÃO DE EXEMPLO
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("EXEMPLO DE PREVISÃO")
print("=" * 60)

amostra_exemplo = np.array([[5.1, 3.5, 1.4, 0.2]])
previsao = modelo.predict(amostra_exemplo)[0]
print(f"\nAmostra de entrada: {amostra_exemplo[0]}")
print(f"  (sépala: {amostra_exemplo[0][0]}cm x {amostra_exemplo[0][1]}cm)")
print(f"  (pétala: {amostra_exemplo[0][2]}cm x {amostra_exemplo[0][3]}cm)")
print(f"\n🌸 Espécie prevista: {iris.target_names[previsao].upper()}")

print("\n✅ Classificação concluída com sucesso!")
