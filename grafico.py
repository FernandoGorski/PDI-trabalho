import matplotlib.pyplot as plt
from collections import defaultdict

# Caminho do relatório
relatorio_path = "relatorio.txt"

# Dicionário para armazenar as emoções por segundo
emocao_por_segundo = defaultdict(list)

# Emoções possíveis (de acordo com os dados do relatório)
emocao_possiveis = ['alegre', 'triste', 'raiva', 'surpreso', 'neutro', 'medo']

# Ler o arquivo de relatório e contar as emoções por segundo
with open(relatorio_path, "r") as f:
    lines = f.readlines()[3:]  # Ignorar as primeiras linhas de título
    for line in lines:
        segundo, emocao = line.split(": ")
        emocao = emocao.strip()
        segundo = int(segundo.split()[1])  # Extrair o número do segundo
        
        # Adiciona a emoção à lista de emoções do segundo
        emocao_por_segundo[segundo].append(emocao)

# Preparando dados para o gráfico
segundos = sorted(emocao_por_segundo.keys())

# Determinar a emoção dominante para cada segundo
emo_dominante_por_segundo = []
for sec in segundos:
    # Encontrar a emoção mais frequente no segundo (em caso de empate, escolher a primeira)
    emocao_dominante = max(set(emocao_por_segundo[sec]), key=emocao_por_segundo[sec].count)
    emo_dominante_por_segundo.append(emocao_dominante)

# Criando o gráfico com fundo preto
fig, ax = plt.subplots(figsize=(10, 6))

# Definindo a cor de fundo do gráfico
fig.patch.set_facecolor('black')  # Cor de fundo da figura (gráfico)
ax.set_facecolor('black')  # Cor de fundo do eixo

# Conectar os pontos com uma linha tracejada branca (hipotenusa)
ax.plot(segundos, [emocao_possiveis.index(emo) for emo in emo_dominante_por_segundo],
        linestyle='--', color='white', linewidth=3)  # Linha tracejada branca grossa

# Alterando a cor dos rótulos
ax.tick_params(axis='x', colors='white')  # Cor dos rótulos do eixo X
ax.tick_params(axis='y', colors='white')  # Cor dos rótulos do eixo Y
plt.xlabel('Segundo', color='white')  # Cor do rótulo do eixo X
plt.ylabel('Emoções', color='white')  # Cor do rótulo do eixo Y

# Alterando a cor do título
plt.title('Emoção Dominante por Segundo', color='white')

# Definindo as emoções no eixo Y
plt.yticks(range(len(emocao_possiveis)), emocao_possiveis, color='white')  # Cor dos rótulos do eixo Y

plt.xticks(segundos, rotation=45)
plt.grid(True, color='gray')  # Cor da grade

# Exibir o gráfico
plt.tight_layout()
plt.show()
