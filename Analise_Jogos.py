import requests
import matplotlib.pyplot as plt

class TabelaJogo:
    def __init__(self, time_a, time_b):
        self.time_a = time_a
        self.time_b = time_b
        self.resultado = None
        self.estatisticas_time_a = {
            "Gols por Jogo": [],
            "Média de Gols": None,
            "Escanteios por Jogo": [],
            "Média de Escanteios": None,
            "Cartões Amarelos por Jogo": [],
            "Média de Cartões Amarelos": None,
            "Vitórias": 0,
            "Derrotas": 0,
            "Empates": 0
        }
        self.estatisticas_time_b = {
            "Gols por Jogo": [],
            "Média de Gols": None,
            "Escanteios por Jogo": [],
            "Média de Escanteios": None,
            "Cartões Amarelos por Jogo": [],
            "Média de Cartões Amarelos": None,
            "Vitórias": 0,
            "Derrotas": 0,
            "Empates": 0
        }

    def adicionar_resultado(self, resultado):
        self.resultado = resultado

    def adicionar_estatisticas_time_a(self, estatisticas):
        self.estatisticas_time_a.update(estatisticas)

    def adicionar_estatisticas_time_b(self, estatisticas):
        self.estatisticas_time_b.update(estatisticas)

    def obter_gols_escanteios_cartoes_por_jogo(self, time):
        gols_por_jogo = []
        escanteios_por_jogo = []
        cartoes_amarelos_por_jogo = []

        for i in range(5):
            gols = int(input(f"Informe quantos gols o {time} fez no jogo {i + 1}: "))
            gols_por_jogo.append(gols)

            cartoes_amarelos = int(input(f"Informe quantos cartões amarelos o {time} teve no jogo {i + 1}: "))
            cartoes_amarelos_por_jogo.append(cartoes_amarelos)

            escanteios = int(input(f"Informe quantos escanteios o {time} teve no jogo {i + 1}: "))
            escanteios_por_jogo.append(escanteios)

        media_gols = sum(gols_por_jogo) / len(gols_por_jogo) if gols_por_jogo else 0
        media_escanteios = sum(escanteios_por_jogo) / len(escanteios_por_jogo) if escanteios_por_jogo else 0
        media_cartoes_amarelos = sum(cartoes_amarelos_por_jogo) / len(cartoes_amarelos_por_jogo) if cartoes_amarelos_por_jogo else 0

        return gols_por_jogo, media_gols, escanteios_por_jogo, media_escanteios, cartoes_amarelos_por_jogo, media_cartoes_amarelos

    def criar_jogo_manualmente(self):
        gols_time_a, media_gols_a, escanteios_time_a, media_escanteios_a, cartoes_amarelos_time_a, media_cartoes_amarelos_a = self.obter_gols_escanteios_cartoes_por_jogo(self.time_a)
        self.adicionar_estatisticas_time_a({
            "Gols por Jogo": gols_time_a,
            "Média de Gols": media_gols_a,
            "Escanteios por Jogo": escanteios_time_a,
            "Média de Escanteios": media_escanteios_a,
            "Cartões Amarelos por Jogo": cartoes_amarelos_time_a,
            "Média de Cartões Amarelos": media_cartoes_amarelos_a
        })

    def criar_jogo_manualmente_time_b(self):
        gols_time_b, media_gols_b, escanteios_time_b, media_escanteios_b, cartoes_amarelos_time_b, media_cartoes_amarelos_b = self.obter_gols_escanteios_cartoes_por_jogo(self.time_b)
        self.adicionar_estatisticas_time_b({
            "Gols por Jogo": gols_time_b,
            "Média de Gols": media_gols_b,
            "Escanteios por Jogo": escanteios_time_b,
            "Média de Escanteios": media_escanteios_b,
            "Cartões Amarelos por Jogo": cartoes_amarelos_time_b,
            "Média de Cartões Amarelos": media_cartoes_amarelos_b
        })

    def exibir_graficos(self):
        # Gráfico de barras para os gols
        plt.bar(range(1, 6), self.estatisticas_time_a['Gols por Jogo'], label=f"{self.time_a} - Média: {self.estatisticas_time_a['Média de Gols']:.2f}")
        plt.bar(range(7, 12), self.estatisticas_time_b['Gols por Jogo'], label=f"{self.time_b} - Média: {self.estatisticas_time_b['Média de Gols']:.2f}")
        plt.xlabel('Jogo')
        plt.ylabel('Gols')
        plt.title('Estatísticas de Gols')
        plt.legend()
        plt.show()

        # Gráfico de barras para os escanteios
        plt.bar(range(1, 6), self.estatisticas_time_a['Escanteios por Jogo'], label=f"{self.time_a} - Média: {self.estatisticas_time_a['Média de Escanteios']:.2f}")
        plt.bar(range(7, 12), self.estatisticas_time_b['Escanteios por Jogo'], label=f"{self.time_b} - Média: {self.estatisticas_time_b['Média de Escanteios']:.2f}")
        plt.xlabel('Jogo')
        plt.ylabel('Escanteios')
        plt.title('Estatísticas de Escanteios')
        plt.legend()
        plt.show()

        # Gráfico de barras para os cartões amarelos
        plt.bar(range(1, 6), self.estatisticas_time_a['Cartões Amarelos por Jogo'], label=f"{self.time_a} - Média: {self.estatisticas_time_a['Média de Cartões Amarelos']:.2f}")
        plt.bar(range(7, 12), self.estatisticas_time_b['Cartões Amarelos por Jogo'], label=f"{self.time_b} - Média: {self.estatisticas_time_b['Média de Cartões Amarelos']:.2f}")
        plt.xlabel('Jogo')
        plt.ylabel('Cartões Amarelos')
        plt.title('Estatísticas de Cartões Amarelos')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    # Solicitar nomes dos times
    time_a = input("Informe o nome do Time A: ").upper()
    time_b = input("Informe o nome do Time B: ").upper()

    # Criar objeto da classe TabelaJogo
    novo_jogo = TabelaJogo(time_a, time_b)

    # Preencher dados para o Time A
    print("\n" + "-" * 40)  # Linha de separação
    print("\nPreenchimento dos dados para o Time A:")
    novo_jogo.criar_jogo_manualmente()

    # Preencher dados para o Time B
    print("\n" + "-" * 40)  # Linha de separação
    print("\nPreenchimento dos dados para o Time B:")
    novo_jogo.criar_jogo_manualmente_time_b()

    # Exibir gráficos
    print("\n" + "-" * 40)  # Linha de separação
    print("\nExibindo Gráficos:")
    novo_jogo.exibir_graficos()
