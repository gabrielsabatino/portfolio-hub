"""
============================================================
ANÁLISE EXPLORATÓRIA DE DADOS DE VENDAS
============================================================
Projeto: Análise de Vendas
Autor: Gabriel Sabatino
Data: 2026
Descrição: Script de análise exploratória usando Pandas,
           NumPy e Matplotlib para identificar padrões
           em dados de vendas.
============================================================
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. CARREGAMENTO DOS DADOS
# ------------------------------------------------------------
print("=" * 60)
print("ANÁLISE DE VENDAS - PORTFOLIOHUB")
print("=" * 60)

# Carregar o dataset
df = pd.read_csv("dados/vendas.csv")
print(f"\n✓ Dados carregados: {df.shape[0]} linhas, {df.shape[1]} colunas")
print("\nPrimeiras linhas:")
print(df.head())

# ------------------------------------------------------------
# 2. ANÁLISE EXPLORATÓRIA
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("ESTATÍSTICAS DESCRITIVAS")
print("=" * 60)
print(df.describe())

# Vendas totais por categoria
print("\n📊 VENDAS POR CATEGORIA:")
vendas_categoria = df.groupby("categoria")["valor"].sum().sort_values(ascending=False)
print(vendas_categoria)

# Top 5 produtos mais vendidos
print("\n🏆 TOP 5 PRODUTOS:")
top_produtos = df.groupby("produto")["quantidade"].sum().nlargest(5)
print(top_produtos)

# ------------------------------------------------------------
# 3. VISUALIZAÇÕES
# ------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Gráfico 1: Vendas por categoria
vendas_categoria.plot(kind="bar", ax=axes[0], color="#6366f1")
axes[0].set_title("Vendas Totais por Categoria", fontsize=14, fontweight="bold")
axes[0].set_xlabel("Categoria")
axes[0].set_ylabel("Valor Total (R$)")
axes[0].tick_params(axis="x", rotation=45)

# Gráfico 2: Top produtos
top_produtos.plot(kind="barh", ax=axes[1], color="#ec4899")
axes[1].set_title("Top 5 Produtos por Quantidade", fontsize=14, fontweight="bold")
axes[1].set_xlabel("Quantidade Vendida")

plt.tight_layout()
plt.savefig("grafico_vendas.png", dpi=100, bbox_inches="tight")
print("\n✓ Gráfico salvo: grafico_vendas.png")

# ------------------------------------------------------------
# 4. INSIGHTS FINAIS
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("INSIGHTS PRINCIPAIS")
print("=" * 60)

categoria_top = vendas_categoria.index[0]
produto_top = top_produtos.index[0]
ticket_medio = df["valor"].mean()

print(f"💡 Categoria mais lucrativa: {categoria_top}")
print(f"💡 Produto mais vendido: {produto_top}")
print(f"💡 Ticket médio: R$ {ticket_medio:.2f}")
print(f"💡 Total de vendas analisadas: {len(df)}")

print("\n✅ Análise concluída com sucesso!")
