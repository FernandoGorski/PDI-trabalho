import os
import cv2
from deepface import DeepFace
import time
import numpy as np

# Caminho do vídeo
video_path = r'C:\Users\ferna\Desktop\Processamento Digital de Imagens\PDI-trabalho\Comercial1.mp4'

# Inicializa a captura da webcam
cap_webcam = cv2.VideoCapture(0)

if not cap_webcam.isOpened():
    print("Erro ao abrir a webcam.")
    exit()

# Dicionário de emoções traduzidas
emocao = {
    'happy': 'alegre',
    'sad': 'triste',
    'angry': 'raiva',
    'surprise': 'surpreso',
    'neutral': 'neutro',
    'fear': 'medo'
}

# Abre o arquivo de relatório para escrever as emoções
relatorio_path = "relatorio.txt"
with open(relatorio_path, "w") as f:
    f.write("Relatorio de Emocoes Detectadas\n")
    f.write("====================================\n")

def analisar_expressao(frame):
    # Analisar a emoção no frame da webcam
    analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    dominant_emotion = analysis[0]['dominant_emotion']
    return dominant_emotion

# Abre o vídeo para obter informações de duração
cap_video = cv2.VideoCapture(video_path)
if not cap_video.isOpened():
    print("Erro ao abrir o vídeo.")
    exit()

fps_video = cap_video.get(cv2.CAP_PROP_FPS)
total_frames = int(cap_video.get(cv2.CAP_PROP_FRAME_COUNT))
video_duration = total_frames / fps_video
print(f"Duração do vídeo: {video_duration} segundos")

cap_video.release()

os.startfile(video_path)

time.sleep(1)

extra_time = 0.5
start_time = time.time()

while True:
    ret_webcam, frame_webcam = cap_webcam.read()
    if not ret_webcam:
        break

    # Detecção de rosto usando DeepFace
    try:
        # DeepFace detecta rostos e retorna as coordenadas
        analysis = DeepFace.analyze(frame_webcam, actions=['emotion'], enforce_detection=True)
        face = analysis[0]['region']  # 'region' contém as coordenadas do rosto
        emotion = analysis[0]['dominant_emotion']  # Emoção detectada

        x, y, w, h = face['x'], face['y'], face['w'], face['h']
        
        # Desenhar um quadrado ao redor do rosto detectado
        cv2.rectangle(frame_webcam, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Exibir a emoção detectada no rosto
        cv2.putText(frame_webcam, 
                    f'{emocao.get(emotion, emotion)}',  # Exibe a emoção em português
                    (x, y - 10),  # Posiciona o texto acima do rosto
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    except Exception as e:
        print(f"Erro na detecção de rosto com DeepFace: {e}")
        continue

    # Mostrar as imagens
    cv2.imshow('Webcam', frame_webcam)

    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= video_duration + extra_time:
        print("Finalizando análise.")
        break

    # Mostrar a emoção no console
    emotion_pt = emocao.get(emotion, emotion)
    analysis_second = int(elapsed_time-1)
    print(f"Emoção detectada: {emotion_pt} no segundo {analysis_second}")

    # Salvar a emoção no arquivo de relatório
    with open(relatorio_path, "a") as f:
        f.write(f"Segundo {analysis_second}: {emotion_pt}\n")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
cap_webcam.release()
cv2.destroyAllWindows()

print(f"Relatório de emoções salvo em {relatorio_path}")