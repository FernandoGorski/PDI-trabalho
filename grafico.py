import matplotlib.pyplot as plt
from collections import defaultdict

# Caminho do relatório
relatorio_path = "relatorio.txt"

# Dicionário para armazenar as emoções por segundo
emocao_por_secundo = defaultdict(list)

# Emoções possíveis (de acordo com os dados do relatório)
emocao_possiveis = ['alegre', 'triste', 'raiva', 'surpreso', 'neutro', 'medo']

# Ler o arquivo de relatório e contar as emoções por segundo
with open(relatorio_path, "r") as f:
    lines = f.readlines()[3:]  # Ignorar as primeiras linhas de título
    for line in lines:
        segundo, emocao = line.split(": ")
        emocao = emocao.strip()
        segundo = int(segundo.split()[1])  # Extrair o número do segundo
        
        # Adicionar a emoção à lista de emoções do segundo
        emocao_por_secundo[segundo].append(emocao)

# Preparar os dados para o gráfico
segundos = sorted(emocao_por_secundo.keys())
segundos_completos = list(range(min(segundos), max(segundos) + 1))  # Preencher de segundo em segundo

# Determinar a emoção dominante para cada segundo
emo_dominante_por_secundo = []
for sec in segundos_completos:
    if sec in emocao_por_secundo:
        # Encontrar a emoção mais frequente no segundo
        emocao_dominante = max(set(emocao_por_secundo[sec]), key=emocao_por_secundo[sec].count)
    else:
        # Preencher segundos ausentes com 'neutro'
        emocao_dominante = 'neutro'
    emo_dominante_por_secundo.append(emocao_dominante)

# Criando o gráfico com os eixos invertidos
fig, ax = plt.subplots(figsize=(12, 8))

# Adicionar a linha conectando os valores
ax.plot(
    segundos_completos,
    [emocao_possiveis.index(emo) for emo in emo_dominante_por_secundo],
    color='green',
    linestyle='-',
    linewidth=2,
    marker='o',
    markersize=6,
    markerfacecolor='green'
)

# Ajustando os rótulos e os eixos
ax.set_facecolor('white')
fig.patch.set_facecolor('white')
plt.ylabel('Emoções', color='black')  # Emoções no eixo Y
plt.xlabel('Segundos', color='black')  # Segundos no eixo X
plt.title('Emoção Dominante por Segundo', color='black')

# Definir as emoções como rótulos do eixo Y
plt.yticks(range(len(emocao_possiveis)), emocao_possiveis, color='black')
plt.xticks(segundos_completos, rotation=45, color='black')  # Exibir todos os segundos

# Adicionar uma matriz bem sutil no fundo
ax.grid(True, which='both', axis='both', color='gray', linestyle='-', linewidth=0.5, alpha=0.2)

# Melhorar o layout
plt.tight_layout()

# Exibir o gráfico
plt.show()
