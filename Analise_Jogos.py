import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import os

sns.set_theme(style="darkgrid", palette="muted")

ARQUIVO_DADOS = os.path.join(os.path.dirname(__file__), "dados", "partidas.csv")
TIMES_DISPONIVEIS = ["Flamengo", "Palmeiras", "Corinthians", "São Paulo", "Grêmio", "Fortaleza"]

COR_A = "#1f77b4"
COR_B = "#ff7f0e"


def carregar_dados():
    return pd.read_csv(ARQUIVO_DADOS, parse_dates=["data"])


def listar_times():
    print("\nTimes disponíveis:")
    for i, time in enumerate(TIMES_DISPONIVEIS, 1):
        print(f"  {i}. {time}")


def selecionar_time(label):
    listar_times()
    while True:
        escolha = input(f"\nEscolha o {label} (número ou nome): ").strip()
        if escolha.isdigit():
            idx = int(escolha) - 1
            if 0 <= idx < len(TIMES_DISPONIVEIS):
                return TIMES_DISPONIVEIS[idx]
        else:
            for time in TIMES_DISPONIVEIS:
                if escolha.lower() == time.lower():
                    return time
        print("  Opção inválida. Tente novamente.")


def calcular_estatisticas(df, time):
    partidas = df[(df["time_mandante"] == time) | (df["time_visitante"] == time)].copy()
    partidas = partidas.sort_values("data").tail(5)

    gols, escanteios, cartoes, resultados = [], [], [], []

    for _, row in partidas.iterrows():
        eh_mandante = row["time_mandante"] == time
        gols.append(int(row["gols_mandante"] if eh_mandante else row["gols_visitante"]))
        escanteios.append(int(row["escanteios_mandante"] if eh_mandante else row["escanteios_visitante"]))
        cartoes.append(int(row["cartoes_amarelos_mandante"] if eh_mandante else row["cartoes_amarelos_visitante"]))

        gf = row["gols_mandante"] if eh_mandante else row["gols_visitante"]
        gc = row["gols_visitante"] if eh_mandante else row["gols_mandante"]
        resultados.append("V" if gf > gc else ("D" if gf < gc else "E"))

    return {
        "Gols por Jogo": gols,
        "Média de Gols": round(sum(gols) / len(gols), 2),
        "Escanteios por Jogo": escanteios,
        "Média de Escanteios": round(sum(escanteios) / len(escanteios), 2),
        "Cartões Amarelos por Jogo": cartoes,
        "Média de Cartões Amarelos": round(sum(cartoes) / len(cartoes), 2),
        "Vitórias": resultados.count("V"),
        "Derrotas": resultados.count("D"),
        "Empates": resultados.count("E"),
        "Resultados": resultados,
    }


def exibir_resumo(sa, sb, time_a, time_b):
    print(f"\n{'═' * 52}")
    print(f"  RESUMO — {time_a} vs {time_b} (últimos 5 jogos)")
    print(f"{'═' * 52}")
    print(f"  {'Métrica':<28} {time_a:>10} {time_b:>10}")
    print(f"  {'─' * 48}")
    for label, chave in [
        ("Média de Gols", "Média de Gols"),
        ("Média de Escanteios", "Média de Escanteios"),
        ("Média de Cartões Amarelos", "Média de Cartões Amarelos"),
        ("Vitórias", "Vitórias"), ("Empates", "Empates"), ("Derrotas", "Derrotas"),
    ]:
        print(f"  {label:<28} {str(sa[chave]):>10} {str(sb[chave]):>10}")
    print(f"{'═' * 52}\n")


# ── Gráfico 1: Barras agrupadas por métrica ───────────────────────────────────
def grafico_barras_comparativo(sa, sb, time_a, time_b):
    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.suptitle(f"Estatísticas — {time_a} vs {time_b} (últimos 5 jogos)",
                 fontsize=14, fontweight="bold")

    pares = [
        ("Gols por Jogo", "Média de Gols", "Gols"),
        ("Escanteios por Jogo", "Média de Escanteios", "Escanteios"),
        ("Cartões Amarelos por Jogo", "Média de Cartões Amarelos", "Cartões Amarelos"),
    ]

    for ax, (chave, media_chave, ylabel) in zip(axes, pares):
        x = range(1, 6)
        ax.bar([j - 0.2 for j in x], sa[chave], width=0.4, color=COR_A,
               label=f"{time_a} (μ={sa[media_chave]})")
        ax.bar([j + 0.2 for j in x], sb[chave], width=0.4, color=COR_B,
               label=f"{time_b} (μ={sb[media_chave]})")
        ax.axhline(sa[media_chave], color=COR_A, linestyle="--", linewidth=1, alpha=0.7)
        ax.axhline(sb[media_chave], color=COR_B, linestyle="--", linewidth=1, alpha=0.7)
        ax.set_title(ylabel, fontsize=11)
        ax.set_xlabel("Jogo")
        ax.set_xticks(list(x))
        ax.set_xticklabels([f"J{j}" for j in x])
        ax.legend(fontsize=8)

    plt.tight_layout()
    plt.show()


# ── Gráfico 2: Pizza de aproveitamento ────────────────────────────────────────
def grafico_aproveitamento(sa, sb, time_a, time_b):
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    fig.suptitle("Aproveitamento (últimos 5 jogos)", fontsize=14, fontweight="bold")

    for ax, stats, time in [(axes[0], sa, time_a), (axes[1], sb, time_b)]:
        valores = [stats["Vitórias"], stats["Empates"], stats["Derrotas"]]
        cores = ["#2ecc71", "#f39c12", "#e74c3c"]
        labels = ["Vitórias", "Empates", "Derrotas"]
        explode = [0.05, 0, 0]
        wedges, texts, autotexts = ax.pie(
            valores, labels=labels, colors=cores, autopct="%1.0f%%",
            startangle=90, explode=explode
        )
        for t in autotexts:
            t.set_fontsize(11)
        ax.set_title(time, fontsize=12, fontweight="bold")

    plt.tight_layout()
    plt.show()


# ── Gráfico 3: Evolução por jogo (linha) ──────────────────────────────────────
def grafico_evolucao(sa, sb, time_a, time_b):
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    fig.suptitle(f"Evolução por Jogo — {time_a} vs {time_b}", fontsize=14, fontweight="bold")

    pares = [
        ("Gols por Jogo", "Gols"),
        ("Escanteios por Jogo", "Escanteios"),
        ("Cartões Amarelos por Jogo", "Cartões Amarelos"),
    ]
    x = range(1, 6)

    for ax, (chave, ylabel) in zip(axes, pares):
        ax.plot(x, sa[chave], marker="o", color=COR_A, label=time_a, linewidth=2)
        ax.plot(x, sb[chave], marker="s", color=COR_B, label=time_b, linewidth=2)
        ax.fill_between(x, sa[chave], sb[chave], alpha=0.1, color="gray")
        ax.set_title(ylabel, fontsize=11)
        ax.set_xlabel("Jogo")
        ax.set_xticks(list(x))
        ax.set_xticklabels([f"J{j}" for j in x])
        ax.legend(fontsize=9)

    plt.tight_layout()
    plt.show()


# ── Gráfico 4: Heatmap de desempenho geral de todos os times ──────────────────
def grafico_heatmap_geral(df):
    registros = []
    for time in TIMES_DISPONIVEIS:
        stats = calcular_estatisticas(df, time)
        registros.append({
            "Time": time,
            "Média Gols": stats["Média de Gols"],
            "Média Escanteios": stats["Média de Escanteios"],
            "Média Cartões": stats["Média de Cartões Amarelos"],
            "Aproveitamento": round((stats["Vitórias"] * 3 + stats["Empates"]) / 15 * 100, 1),
        })

    tabela = pd.DataFrame(registros).set_index("Time")

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.heatmap(tabela, annot=True, fmt=".1f", cmap="YlOrRd", linewidths=0.5,
                ax=ax, cbar_kws={"label": "Valor"})
    ax.set_title("Desempenho Geral — Todos os Times (últimos 5 jogos)",
                 fontsize=13, fontweight="bold")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    print("=" * 52)
    print("  ANÁLISE DE JOGOS — BRASILEIRÃO 2025")
    print("=" * 52)

    df = carregar_dados()
    time_a = selecionar_time("Time A")
    time_b = selecionar_time("Time B")

    print(f"\nCalculando estatísticas...")
    sa = calcular_estatisticas(df, time_a)
    sb = calcular_estatisticas(df, time_b)

    exibir_resumo(sa, sb, time_a, time_b)

    print("Exibindo gráficos...\n")
    grafico_barras_comparativo(sa, sb, time_a, time_b)
    grafico_aproveitamento(sa, sb, time_a, time_b)
    grafico_evolucao(sa, sb, time_a, time_b)
    grafico_heatmap_geral(df)
