import cv2
import numpy as np
import time
from deepface import DeepFace

emocao = {
    'happy': 'alegre',
    'sad': 'triste',
    'angry': 'raiva',
    'surprise': 'surpreso',
    'neutral': 'neutro',
    'fear': 'medo'
}

# Função para detectar a emoção
def detectarEmocao(frame):
    try:
        resultado = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if isinstance(resultado, dict):
            emocao_dominante = resultado.get('dominant_emotion', None)
        elif isinstance(resultado, list) and len(resultado) > 0:
            emocao_dominante = resultado[0].get('dominant_emotion', None)
        else:
            emocao_dominante = None

        if emocao_dominante:
            return emocao.get(emocao_dominante, 'desconhecida')
        return None
    except Exception as e:
        print(f"Erro ao detectar emoção: {e}")
        return None

# Imagem Binária
def binarizarImagem(frame):
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binario = cv2.threshold(cinza, 127, 255, cv2.THRESH_BINARY)
    return binario

# Imagem Borrada
def aplicarBorramento(frame):
    return cv2.GaussianBlur(frame, (15, 15), 0)

# Configuração da detecção de rosto
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

cores = [
    (0, 0, 255),  # Vermelho
    (0, 255, 255),  # Amarelo
    (0, 255, 0),  # Verde
    (255, 0, 0),  # Azul
    (255, 165, 0),  # Laranja
    (255, 0, 255),  # Roxo
    (255, 255, 255),  # Branco
    (0, 0, 0)  # Preto
]

nomesCores = ['vermelho', 'amarelo', 'verde', 'azul', 'laranja', 'roxo', 'branco', 'preto']
tempoTotal = 40  
tempoCor = tempoTotal / len(cores)
inicio = time.time()

emocaoCor = {cor: {emo: 0 for emo in emocao.values()} for cor in nomesCores}

while True:
    ret, frame = video.read()
    if not ret:
        break

    imagemOriginal = frame.copy()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = faceCascade.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    
    # Atualizar cor de fundo 
    tempoAtual = time.time() - inicio
    indice = int(tempoAtual // tempoCor) % len(cores)
    corAtual = cores[indice]
    nomeCor = nomesCores[indice]
    
    # Exibir a cor no canto da tela
    cv2.rectangle(frame, (frame.shape[1] - 150, 50), (frame.shape[1] - 50, 150), corAtual, -1)
    
    # Detecção de emoção
    emocao_detectada = detectarEmocao(frame)
    if emocao_detectada:
        print(f"Emoção detectada para a cor {nomeCor}: {emocao_detectada}")
        if emocao_detectada in emocaoCor[nomeCor]:
            emocaoCor[nomeCor][emocao_detectada] += 1

    imagem_binarizada = binarizarImagem(frame)
    frame_borrado = aplicarBorramento(frame)
    
    cv2.imshow("Imagem", frame)
    cv2.imshow("Imagem Binarizada", imagem_binarizada)
    cv2.imshow("Imagem Borrada", frame_borrado)

    tempoAtual = time.time() - inicio
    if tempoAtual >= tempoTotal:
        print("\nResumo das emoções detectadas por cor:")
        for cor, contagens in emocaoCor.items():
            print(f"Cor {cor}: {contagens}")
        
        # Determinar a cor favorita com base na emoção mais positiva associada
        corFavorita = max(
            nomesCores,
            key=lambda cor: emocaoCor[cor]['alegre']
        )
        print(f"A cor favorita é: {corFavorita}")
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
