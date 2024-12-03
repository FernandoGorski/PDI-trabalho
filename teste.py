import os
import cv2
from deepface import DeepFace
import time

video_path = r'C:\Users\Hygor\Downloads\Video.mp4'


cap_webcam = cv2.VideoCapture(0)  

if not cap_webcam.isOpened():
    print("Erro ao abrir a webcam.")
    exit()


emocao = {
    'happy': 'alegre',
    'sad': 'triste',
    'angry': 'raiva',
    'surprise': 'surpreso',
    'neutral': 'neutro',
    'fear': 'medo'
}

def analisar_expressao(frame):
    # Analisar a emoção no frame da webcam
    analysis = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    dominant_emotion = analysis[0]['dominant_emotion']
    return dominant_emotion

frame_count = 0
cap_video = None  

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

time.sleep(1.5)

extra_time = 1

last_analysis_time = time.time()  

analysis_interval = 1  

start_time = time.time()

while True:
    ret_webcam, frame_webcam = cap_webcam.read()

    if not ret_webcam:
        break  
    
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time >= video_duration + extra_time:
        print("Duração do vídeo + tempo extra alcançado. Finalizando análise.")
        break
    
    emotion = analisar_expressao(frame_webcam)
    
    analysis_second = int(elapsed_time)
    
    emotion_pt = emocao.get(emotion, emotion)  
    
    print(f"Emoção detectada: {emotion_pt} no segundo {analysis_second}")
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap_webcam.release()
if cap_video:
    cap_video.release()
cv2.destroyAllWindows()
