import cv2
import numpy as np
import pyautogui
from ultralytics import YOLO
import time
from datetime import datetime
from pathlib import Path

# 1. Cargar el detector de objetos
model = YOLO("modelos/yolov8n.pt")
VEHICULOS_ID =  [2, 3, 5, 7] # Autos, camiones, motocicletas

# Variables de control para la grabación
grabando = False
frames_totales_grabar = 0
video_writer = None
duracion_segundos = 30
fps_estimados = 2  # Analizamos la pantalla 2 veces por segundo (cada 500ms)

print("====================================================")
print("  GRABACIÓN AUTOMÁTICA DE TOMA COMPLETA ACTIVADA    ")
print("====================================================")

# Coordenadas del cajón (para el análisis de la IA)
ancho_pantalla, alto_pantalla = pyautogui.size()
x_min = int(ancho_pantalla * 0.548)
x_max = int(ancho_pantalla * 0.690)
y_min = int(alto_pantalla * 0.322)  
y_max = int(alto_pantalla * 0.380)

estado_anterior = "LIBRE"

while True:
    # 2. Capturar la pantalla completa en vivo
    captura = pyautogui.screenshot()
    frame = np.array(captura)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    # 3. Extraer el fragmento del cajón solo para que la IA lo analice
    cajon_recortado = frame[y_min:y_max, x_min:x_max]

    if cajon_recortado.size == 0:
        continue

    # Analizar el cajón pequeño
    results = model(cajon_recortado, stream=True, verbose=False, conf=0.25)
    
    cajon_ocupado = False
    for r in results:
        for box in r.boxes:
            if int(box.cls) in VEHICULOS_ID:
                cajon_ocupado = True

    estado_actual = "OCUPADO" if cajon_ocupado else "LIBRE"

    # CORREGIDO: Se cambió 'not grabbing' por 'not grabando'
    if estado_actual == "OCUPADO" and estado_anterior == "LIBRE" and not grabando:
        print(f"\n[ALERTA] {datetime.now().strftime('%H:%M:%S')} - ¡Vehículo detectado!")
        print("--> Iniciando grabación de 30 segundos de la TOMA COMPLETA...")
        
        # Generar nombre del archivo de video
        fecha_hora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_video = f"llegada_completa_{fecha_hora}.mp4"
        
        # Configurar el grabador (ahora usa el ancho y alto de toda tu pantalla)
        cuatrocc = cv2.VideoWriter_fourcc(*'mp4v')
        video_writer = cv2.VideoWriter(nombre_video, cuatrocc, fps_estimados, (ancho_pantalla, alto_pantalla))
        
        grabando = True
        frames_totales_grabar = duracion_segundos * fps_estimados

    # Si está activado, graba el 'frame' completo (toda tu pantalla)
    if grabando:
        video_writer.write(frame)
        frames_totales_grabar -= 1
        segundos_restantes = int(frames_totales_grabar / fps_estimados)
        print(f"[GRABANDO] Capturando pantalla completa... Quedan {segundos_restantes} segundos.")
        
        # Detener la grabación al cumplir los 30 segundos
        if frames_totales_grabar <= 0:
            video_writer.release()
            grabando = False
            print(f"[OK] ¡Video guardado con éxito!: {nombre_video}\n")

    estado_anterior = estado_actual

    # Interfaz gráfica de tu pequeña ventana flotante de control
    color_banner = (0, 0, 255) if cajon_ocupado else (0, 255, 0)
    banner = np.zeros((45, cajon_recortado.shape[1], 3), dtype=np.uint8)
    banner[:] = color_banner
    
    texto_pantalla = f"{estado_actual} (REC)" if grabando else estado_actual
    cv2.putText(banner, texto_pantalla, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    interfaz_final = np.vstack((banner, cajon_recortado))
    interfaz_grande = cv2.resize(interfaz_final, (350, 250))

    cv2.imshow("Monitor: Cajon Gris", interfaz_grande)

    # OPTIMIZADO: cv2.waitKey maneja el tiempo de espera de forma nativa y fluida
    # 500 milisegundos equivalen al sleep(0.5) que tenías antes
    if cv2.waitKey(500) & 0xFF == ord('q'):
        if video_writer is not None:
            video_writer.release()
        break

cv2.destroyAllWindows()
