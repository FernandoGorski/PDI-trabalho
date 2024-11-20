import cv2
import numpy as np
from deepface import DeepFace
import time

emocao = {
    'happy': 'alegre',
    'sad': 'triste',
    'angry': 'raiva',
    'surprise': 'surpreso',
    'neutral': 'neutro',
    'fear': 'medo'
}

def detectarEmocao(frame):
    try:
        resultado = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emocao = resultado[0]['dominant_emotion']
        return emocao.get(emocao, 'desconhecida')
    except Exception as e:
        print(f"Erro ao detectar emoção: {e}")
        return None

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video = cv2.VideoCapture(0)

cores = [(0, 0, 255), (0, 255, 255), (0, 255, 0)]
nomesCores = ['vermelho', 'amarelo', 'verde']
tempoTotal = 20  
tempoCor = tempoTotal / len(cores)
inicio = time.time()

emocaoCor = {
    'vermelho': {'alegre': 0, 'triste': 0, 'raiva': 0, 'surpreso': 0, 'neutro': 0, 'medo': 0},
    'amarelo': {'alegre': 0, 'triste': 0, 'raiva': 0, 'surpreso': 0, 'neutro': 0, 'medo': 0},
    'verde': {'alegre': 0, 'triste': 0, 'raiva': 0, 'surpreso': 0, 'neutro': 0, 'medo': 0}
}

while True:
    ret, frame = video.read()
    if not ret:
        break

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rostos = faceCascade.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    
    tempoAtual = time.time() - inicio

    indice = int(tempoAtual // tempoCor) % len(cores)
    corAtual = cores[indice]
    nomeCor = nomesCores[indice]
    cv2.rectangle(frame, (frame.shape[1] - 150, 50), (frame.shape[1] - 50, 150), corAtual, -1)
    

    emocao = detectarEmocao(frame)
    if emocao:
        print(f"Emoção detectada para a cor {nomeCor}: {emocao}")
        if emocao in emocaoCor[nomeCor]:
            emocaoCor[nomeCor][emocao] += 1

    cv2.imshow("Video com Quadrado Colorido", frame)

    if tempoAtual >= tempoTotal:
        print("\nResumo das emoções detectadas por cor:")
        for cor, contagens in emocaoCor.items():
            print(f"Cor {cor}: {contagens}")
        
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
