import pandas as pd
import matplotlib.pyplot as plt
import os


ARQUIVO_DADOS = os.path.join(os.path.dirname(__file__), "dados", "partidas.csv")
TIMES_DISPONIVEIS = ["Flamengo", "Palmeiras", "Corinthians", "São Paulo", "Grêmio", "Athletico"]


def carregar_dados():
    df = pd.read_csv(ARQUIVO_DADOS, parse_dates=["data"])
    return df


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
    """Retorna estatísticas dos últimos 5 jogos do time."""
    partidas = df[(df["time_mandante"] == time) | (df["time_visitante"] == time)].copy()
    partidas = partidas.sort_values("data").tail(5)

    gols, escanteios, cartoes, resultados = [], [], [], []

    for _, row in partidas.iterrows():
        eh_mandante = row["time_mandante"] == time
        gols.append(row["gols_mandante"] if eh_mandante else row["gols_visitante"])
        escanteios.append(row["escanteios_mandante"] if eh_mandante else row["escanteios_visitante"])
        cartoes.append(row["cartoes_amarelos_mandante"] if eh_mandante else row["cartoes_amarelos_visitante"])

        gols_favor = row["gols_mandante"] if eh_mandante else row["gols_visitante"]
        gols_contra = row["gols_visitante"] if eh_mandante else row["gols_mandante"]
        if gols_favor > gols_contra:
            resultados.append("V")
        elif gols_favor < gols_contra:
            resultados.append("D")
        else:
            resultados.append("E")

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
        "Jogos": len(partidas),
    }


def exibir_resumo(stats_a, stats_b, time_a, time_b):
    print(f"\n{'═' * 50}")
    print(f"  RESUMO — {time_a} vs {time_b} (últimos 5 jogos)")
    print(f"{'═' * 50}")
    print(f"{'Métrica':<28} {time_a:>10} {time_b:>10}")
    print(f"{'─' * 50}")
    metricas = [
        ("Média de Gols", "Média de Gols"),
        ("Média de Escanteios", "Média de Escanteios"),
        ("Média de Cartões Amarelos", "Média de Cartões Amarelos"),
        ("Vitórias", "Vitórias"),
        ("Empates", "Empates"),
        ("Derrotas", "Derrotas"),
    ]
    for label, chave in metricas:
        print(f"  {label:<26} {str(stats_a[chave]):>10} {str(stats_b[chave]):>10}")
    print(f"{'═' * 50}\n")


def _grafico_barras(stats_a, stats_b, time_a, time_b, chave, media_chave, ylabel, titulo):
    jogos = range(1, len(stats_a[chave]) + 1)
    x = list(jogos)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar([j - 0.2 for j in x], stats_a[chave], width=0.4,
           label=f"{time_a} (média: {stats_a[media_chave]})", color="#1f77b4")
    ax.bar([j + 0.2 for j in x], stats_b[chave], width=0.4,
           label=f"{time_b} (média: {stats_b[media_chave]})", color="#ff7f0e")

    ax.axhline(stats_a[media_chave], color="#1f77b4", linestyle="--", linewidth=1, alpha=0.6)
    ax.axhline(stats_b[media_chave], color="#ff7f0e", linestyle="--", linewidth=1, alpha=0.6)

    ax.set_xlabel("Jogo")
    ax.set_ylabel(ylabel)
    ax.set_title(titulo, fontsize=13, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([f"J{j}" for j in x])
    ax.legend()
    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.show()


def exibir_graficos(stats_a, stats_b, time_a, time_b):
    _grafico_barras(stats_a, stats_b, time_a, time_b,
                    "Gols por Jogo", "Média de Gols",
                    "Gols", f"Gols — {time_a} vs {time_b}")
    _grafico_barras(stats_a, stats_b, time_a, time_b,
                    "Escanteios por Jogo", "Média de Escanteios",
                    "Escanteios", f"Escanteios — {time_a} vs {time_b}")
    _grafico_barras(stats_a, stats_b, time_a, time_b,
                    "Cartões Amarelos por Jogo", "Média de Cartões Amarelos",
                    "Cartões Amarelos", f"Cartões Amarelos — {time_a} vs {time_b}")


if __name__ == "__main__":
    print("=" * 50)
    print("  ANÁLISE DE JOGOS — BRASILEIRÃO 2023")
    print("=" * 50)

    df = carregar_dados()
    time_a = selecionar_time("Time A")
    time_b = selecionar_time("Time B")

    print(f"\nCalculando estatísticas dos últimos 5 jogos...")
    stats_a = calcular_estatisticas(df, time_a)
    stats_b = calcular_estatisticas(df, time_b)

    exibir_resumo(stats_a, stats_b, time_a, time_b)
    exibir_graficos(stats_a, stats_b, time_a, time_b)
