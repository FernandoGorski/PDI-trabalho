import matplotlib.pyplot as plt
from collections import defaultdict

# Caminho do relatório
relatorio_path = "relatorio.txt"

# Dicionário para armazenar as emoções por segundo
emocao_por_secundo = defaultdict(list)

# Emoções possíveis
emocao_possiveis = ['triste', 'alegre', 'surpreso', 'raiva', 'neutro', 'medo']

# Ler o arquivo de relatório e organizar os dados
with open(relatorio_path, "r") as f:
    lines = f.readlines()[3:]  # Ignorar as primeiras linhas de título
    for line in lines:
        segundo, emocao = line.split(": ")
        emocao = emocao.strip()
        segundo = int(segundo.split()[1])  # Extrair o número do segundo
        emocao_por_secundo[segundo].append(emocao)

# Identificar intervalos contínuos para cada emoção
intervalos_emocoes = defaultdict(list)

for emocao in emocao_possiveis:
    inicio = None
    for segundo in sorted(emocao_por_secundo.keys()):
        if emocao in emocao_por_secundo[segundo]:
            if inicio is None:
                inicio = segundo
        else:
            if inicio is not None:
                intervalos_emocoes[emocao].append((inicio, segundo - 1))
                inicio = None
    if inicio is not None:  # Caso a emoção vá até o último segundo
        intervalos_emocoes[emocao].append((inicio, max(emocao_por_secundo.keys())))

# Criar o gráfico de barras horizontais segmentadas
fig, ax = plt.subplots(figsize=(12, 8))
y_positions = range(len(emocao_possiveis))  # Posições no eixo Y para as emoções
cores = ['blue', 'green', 'red', 'purple', 'gray', 'cyan']  # Cores para cada emoção

# Adicionar as linhas horizontais contínuas primeiro (por baixo das barras)
for y in y_positions:
    ax.axhline(y=y, color='lightgray', linewidth=0.5, zorder=1)  # `zorder=1` para ficar atrás

# Plotar as barras segmentadas por cima das linhas
for i, emocao in enumerate(emocao_possiveis):
    for inicio, fim in intervalos_emocoes[emocao]:
        ax.barh(y=i, width=fim - inicio + 1, left=inicio, color=cores[i], edgecolor="black", height=0.4, zorder=2)

# Ajustar os rótulos e títulos
plt.yticks(y_positions, emocao_possiveis, color='black')
plt.xlabel('Segundos', color='black')
plt.ylabel('Emoções', color='black')
plt.title('Duração de Emoções Segmentadas', color='black')

# Melhorar o layout
plt.tight_layout()

# Exibir o gráfico
plt.show()
