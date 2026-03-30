import matplotlib.pyplot as plt


class TabelaJogo:
    def __init__(self, time_a, time_b):
        self.time_a = time_a
        self.time_b = time_b
        self.estatisticas_time_a = self._estatisticas_vazias()
        self.estatisticas_time_b = self._estatisticas_vazias()

    def _estatisticas_vazias(self):
        return {
            "Gols por Jogo": [],
            "Média de Gols": None,
            "Escanteios por Jogo": [],
            "Média de Escanteios": None,
            "Cartões Amarelos por Jogo": [],
            "Média de Cartões Amarelos": None,
            "Vitórias": 0,
            "Derrotas": 0,
            "Empates": 0,
        }

    def _coletar_dados_time(self, time):
        gols, escanteios, cartoes = [], [], []

        for i in range(1, 6):
            gols.append(int(input(f"Gols do {time} no jogo {i}: ")))
            cartoes.append(int(input(f"Cartões amarelos do {time} no jogo {i}: ")))
            escanteios.append(int(input(f"Escanteios do {time} no jogo {i}: ")))

        return {
            "Gols por Jogo": gols,
            "Média de Gols": sum(gols) / len(gols),
            "Escanteios por Jogo": escanteios,
            "Média de Escanteios": sum(escanteios) / len(escanteios),
            "Cartões Amarelos por Jogo": cartoes,
            "Média de Cartões Amarelos": sum(cartoes) / len(cartoes),
        }

    def coletar_dados(self):
        print(f"\n{'─' * 40}")
        print(f"Dados para: {self.time_a}")
        self.estatisticas_time_a.update(self._coletar_dados_time(self.time_a))

        print(f"\n{'─' * 40}")
        print(f"Dados para: {self.time_b}")
        self.estatisticas_time_b.update(self._coletar_dados_time(self.time_b))

    def _grafico_barras(self, chave, ylabel, titulo):
        jogos = range(1, 6)
        plt.figure(figsize=(8, 5))
        plt.bar(
            [j - 0.2 for j in jogos],
            self.estatisticas_time_a[chave],
            width=0.4,
            label=f"{self.time_a} (média: {self.estatisticas_time_a[f'Média de {chave.split()[0]}']:.2f})",
        )
        plt.bar(
            [j + 0.2 for j in jogos],
            self.estatisticas_time_b[chave],
            width=0.4,
            label=f"{self.time_b} (média: {self.estatisticas_time_b[f'Média de {chave.split()[0]}']:.2f})",
        )
        plt.xlabel("Jogo")
        plt.ylabel(ylabel)
        plt.title(titulo)
        plt.xticks(jogos, [f"J{j}" for j in jogos])
        plt.legend()
        plt.tight_layout()
        plt.show()

    def exibir_graficos(self):
        self._grafico_barras("Gols por Jogo", "Gols", f"Gols — {self.time_a} vs {self.time_b}")
        self._grafico_barras("Escanteios por Jogo", "Escanteios", f"Escanteios — {self.time_a} vs {self.time_b}")
        self._grafico_barras("Cartões Amarelos por Jogo", "Cartões Amarelos", f"Cartões Amarelos — {self.time_a} vs {self.time_b}")


if __name__ == "__main__":
    time_a = input("Nome do Time A: ").upper()
    time_b = input("Nome do Time B: ").upper()

    jogo = TabelaJogo(time_a, time_b)
    jogo.coletar_dados()

    print(f"\n{'─' * 40}")
    print("Exibindo gráficos...")
    jogo.exibir_graficos()
