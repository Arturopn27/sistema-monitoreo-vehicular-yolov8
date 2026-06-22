# sistema-monitoreo-vehicular-yolov8
Sistema de monitoreo vehicular con visión artificial utilizando Python, OpenCV y YOLOv8.
# Sistema de Monitoreo Vehicular con YOLOv8

Proyecto desarrollado en Python para detectar vehículos que obstruyen una zona específica de estacionamiento mediante visión artificial. El sistema analiza una región de la pantalla en tiempo real y, cuando detecta un vehículo, inicia automáticamente una grabación de evidencia durante 30 segundos.

## Objetivo del proyecto

El objetivo principal de este proyecto es automatizar la detección de vehículos que bloquean la salida de un estacionamiento, generando evidencia en video de manera automática.

Este proyecto fue desarrollado como una solución personal ante una necesidad real: identificar cuándo un vehículo obstruía la salida del estacionamiento.

## Tecnologías utilizadas

* Python
* OpenCV
* YOLOv8
* Ultralytics
* NumPy
* PyAutoGUI
* Git y GitHub

## Funcionalidades principales

* Captura de pantalla en tiempo real.
* Análisis de una zona específica del estacionamiento.
* Detección de vehículos usando YOLOv8.
* Grabación automática de evidencia cuando se detecta una obstrucción.
* Generación de videos con fecha y hora.
* Interfaz visual sencilla para mostrar el estado del espacio monitoreado.
* Organización del proyecto con estructura profesional.

## Estructura del proyecto

```text
sistema-monitoreo-vehicular-yolov8/
│
├── capturas/
├── modelos/
│   └── yolov8n.pt
│
├── src/
│   └── main.py
│
├── videos/
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/Arturopn27/sistema-monitoreo-vehicular-yolov8.git
```

2. Entrar a la carpeta del proyecto:

```bash
cd sistema-monitoreo-vehicular-yolov8
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

En Windows, si el comando `python` no está disponible, se puede usar:

```bash
py -m pip install -r requirements.txt
```

## Uso

Ejecutar el programa desde la raíz del proyecto:

```bash
py src/main.py
```

Para cerrar la ventana de monitoreo, presionar la tecla:

```text
q
```

## Funcionamiento general

El sistema captura la pantalla completa y recorta una zona específica donde se desea detectar la presencia de vehículos. Esa región es procesada por YOLOv8 para identificar objetos como autos, motocicletas, camiones o autobuses.

Cuando el sistema detecta que el espacio pasa de estar libre a ocupado, inicia automáticamente una grabación de 30 segundos de la pantalla completa. El archivo se guarda en la carpeta `videos/` con un nombre basado en la fecha y hora de detección.

## Clases detectadas

El modelo YOLOv8 utiliza las siguientes clases del dataset COCO:

* Auto
* Motocicleta
* Autobús
* Camión

## Ejemplo de salida

Cuando se detecta un vehículo, el sistema muestra mensajes como:

```text
[ALERTA] 14:32:10 - ¡Vehículo detectado!
--> Iniciando grabación de 30 segundos de la TOMA COMPLETA...
[GRABANDO] Capturando pantalla completa... Quedan 29 segundos.
[OK] ¡Video guardado con éxito!
```

## Consideraciones

Este proyecto fue creado con fines personales, educativos y de aprendizaje.
El sistema utiliza captura de pantalla, por lo que debe emplearse de forma responsable y respetando la privacidad de las personas.

## Aprendizajes obtenidos

Durante el desarrollo de este proyecto se aplicaron conocimientos de:

* Visión artificial.
* Detección de objetos.
* Automatización con Python.
* Procesamiento de imágenes con OpenCV.
* Manejo de rutas y estructura de proyectos.
* Uso de Git y GitHub para control de versiones.
* Documentación técnica de proyectos.

## Autor

**Arturo Pacheco**

Proyecto desarrollado como práctica personal de visión artificial aplicada a un problema real de monitoreo vehicular.
