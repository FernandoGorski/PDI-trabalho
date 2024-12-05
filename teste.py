import os
import cv2
from deepface import DeepFace
import time
import numpy as np

video_paths = [
    r'C:\Users\ferna\Desktop\Processamento Digital de Imagens\PDI-trabalho\Comercial1.mp4',
    r'C:\Users\ferna\Desktop\Processamento Digital de Imagens\PDI-trabalho\Comercial2.mp4',
    r'C:\Users\ferna\Desktop\Processamento Digital de Imagens\PDI-trabalho\Comercial3.mp4'
]

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

relatorio_path = "relatorio.txt"
with open(relatorio_path, "w") as f:
    f.write("Relatório de Emoções Detectadas\n")
    f.write("====================================\n")


for video_path in video_paths:
    cap_video = cv2.VideoCapture(video_path)
    if not cap_video.isOpened():
        print(f"Erro ao abrir o vídeo: {video_path}")
        continue

    fps_video = cap_video.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap_video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_duration = total_frames / fps_video
    print(f"Duração do vídeo {video_path}: {video_duration} segundos")
    
    cap_video.release()
    os.startfile(video_path)
    time.sleep(1)  

    extra_time = 0.5
    start_time = time.time()

    while True:
        ret_webcam, frame_webcam = cap_webcam.read()
        if not ret_webcam:
            print("Erro ao acessar a webcam durante o processamento.")
            break

        try:
            # Analisar emoção com DeepFace
            analysis = DeepFace.analyze(frame_webcam, actions=['emotion'], enforce_detection=True)
            face = analysis[0]['region']
            emotion = analysis[0]['dominant_emotion']

            x, y, w, h = face['x'], face['y'], face['w'], face['h']
            
            # Desenhar um quadrado ao redor do rosto
            cv2.rectangle(frame_webcam, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # Exibir a emoção detectada
            cv2.putText(frame_webcam, 
                        f'{emocao.get(emotion, emotion)}', 
                        (x, y - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        except Exception as e:
            print(f"Erro na detecção de rosto com DeepFace: {e}")
            continue

        # Mostrar a imagem da webcam
        cv2.imshow('Webcam', frame_webcam)

        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= video_duration + extra_time:
            print(f"Análise do vídeo {video_path} concluída.")
            break

        # Mostrar e salvar a emoção detectada
        emotion_pt = emocao.get(emotion, emotion)
        analysis_second = int(elapsed_time-1)
        print(f"Emoção detectada: {emotion_pt} no segundo {analysis_second}")

        with open(relatorio_path, "a") as f:
            f.write(f"{video_path} - Segundo {analysis_second}: {emotion_pt}\n")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Processo interrompido pelo usuário.")
            break

    print(f"Concluído o processamento de: {video_path}")
    time.sleep(2)

# Libera os recursos
cap_webcam.release()
cv2.destroyAllWindows()

print(f"Relatório de emoções salvo em {relatorio_path}")
