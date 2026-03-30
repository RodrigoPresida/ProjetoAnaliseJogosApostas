# Análise de Jogos — Brasileirão 2025

Análise exploratória comparando o desempenho dos principais clubes do Brasileirão 2025 com base em gols, escanteios e cartões amarelos dos últimos 5 jogos de cada time.

## Demonstração

| Gráfico | Descrição |
|---|---|
| Barras agrupadas | Estatísticas jogo a jogo com linha de média |
| Pizza | Aproveitamento (V/E/D) de cada time |
| Linhas | Evolução das métricas ao longo dos jogos |
| Heatmap | Panorama geral de todos os times |

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)

## Estrutura do Projeto

```
ProjetoAnaliseJogosApostas/
├── dados/
│   └── partidas.csv        # Dados das partidas (gols, escanteios, cartões)
├── Analise_Jogos.ipynb     # Notebook interativo (recomendado)
├── Analise_Jogos.py        # Script standalone
└── README.md
```

## Como Usar

### Notebook (recomendado)

```bash
pip install pandas matplotlib seaborn jupyter
jupyter notebook Analise_Jogos.ipynb
```

Na **célula 5**, altere os times para a comparação desejada:

```python
TIME_A = 'Flamengo'
TIME_B = 'Palmeiras'
```

Times disponíveis: `Flamengo`, `Palmeiras`, `Corinthians`, `São Paulo`, `Grêmio`, `Fortaleza`

### Script via terminal

```bash
python Analise_Jogos.py
```

## Métricas Analisadas

| Métrica | Descrição |
|---|---|
| Gols por jogo | Produção ofensiva nos últimos 5 jogos |
| Escanteios por jogo | Indicador de domínio territorial |
| Cartões amarelos | Estilo de jogo (agressivo vs. técnico) |
| Aproveitamento % | Pontos conquistados / disputados |

## Dados

Os dados em `dados/partidas.csv` cobrem partidas do Brasileirão 2025 (agosto–setembro/2025) e incluem:

- Times mandante e visitante
- Gols, escanteios e cartões amarelos por time
- Data da partida

## Autor

**Rodrigo Cruz dos Santos**
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/rodrigopresidati)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/RodrigoPresida)
