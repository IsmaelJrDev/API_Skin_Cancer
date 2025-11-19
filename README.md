# 🩺 API Skin Cancer Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange)
![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-06B6D4)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248)

Un sistema de **apoyo al diagnóstico dermatológico** basado en Inteligencia Artificial. Esta aplicación web permite a los usuarios subir imágenes dermatoscópicas y recibir una predicción sobre la naturaleza de la lesión (benigna o maligna) utilizando modelos de **Deep Learning (ResNet50 y AlexNet)** entrenados con el dataset HAM10000.

La aplicación registra automáticamente el historial de diagnósticos en **MongoDB Atlas** y cuenta con una interfaz moderna construida con **TailwindCSS**.

---

## 🚀 Características Principales

* **Multi-Modelo:** El usuario puede elegir entre dos arquitecturas neuronales:
    * **ResNet50** (Transfer Learning): Alta precisión.
    * **AlexNet** (Custom Architecture): Modelo clásico entrenado desde cero.
* **Análisis en Tiempo Real:** Procesamiento de imágenes y predicción en segundos.
* **Historial en la Nube:** Cada diagnóstico se guarda en MongoDB Atlas con metadatos (fecha, confianza, tipo de lesión).
* **Interfaz Responsive:** Frontend profesional diseñado con TailwindCSS.
* **Detección de Riesgo:** Sistema de alertas automático si la lesión es clasificada como Melanoma o Carcinoma.

---

## 🛠️ Stack Tecnológico

* **Backend:** Django (Python)
* **IA / ML:** TensorFlow, Keras, OpenCV, NumPy
* **Base de Datos:** MongoDB Atlas (para logs e historial)
* **Frontend:** HTML5, TailwindCSS (vía CDN)
* **Despliegue / Exposición:** Ngrok (para acceso remoto seguro)

---

## 📂 Estructura del Proyecto

```bash
API_Skin_Cancer/
├── core/                 # Configuración principal de Django (settings, urls)
├── diagnosis/            # Aplicación lógica (vistas, modelos, templates)
│   ├── templates/        # Interfaz de usuario (index.html)
│   └── views.py          # Lógica de inferencia y conexión a Mongo
├── media/                # Almacenamiento temporal de imágenes subidas
├── modelos_entrenados/   # CARPETA CRÍTICA: Aquí deben ir los archivos .keras
│   ├── modelo_final_skin_cancer_alexnet.keras
│   └── modelo_final_skin_cancer_resnet.keras
├── manage.py
└── requirements.txt
⚙️ Instalación y ConfiguraciónSigue estos pasos para ejecutar el proyecto en tu entorno local (Linux/Mac/Windows).1. Clonar el repositorioBashgit clone [https://github.com/IsmaelJrDev/API_Skin_Cancer.git](https://github.com/IsmaelJrDev/API_Skin_Cancer.git)
cd API_Skin_Cancer
2. Crear entorno virtualBash# Linux / Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
3. Instalar dependenciasBashpip install -r requirements.txt
(Asegúrate de tener instaladas las librerías: django, tensorflow, opencv-python-headless, pymongo, dnspython, pillow, numpy)4. Colocar los Modelos EntrenadosDebido al límite de tamaño de GitHub, los modelos entrenados (.keras) no se incluyen en el repositorio.Crea una carpeta llamada modelos_entrenados en la raíz.Coloca tus archivos modelo_final_skin_cancer_resnet.keras y modelo_final_skin_cancer_alexnet.keras dentro.5. Configurar MongoDB AtlasCrea un clúster gratuito en MongoDB Atlas.Obtén tu Connection String.En core/settings.py, actualiza la variable:PythonMONGO_URI = "mongodb+srv://<usuario>:<password>@cluster..."
▶️ EjecuciónModo LocalBashpython manage.py runserver
Accede a http://127.0.0.1:8000.Modo Público (Acceso desde celular con Ngrok)Si deseas probar la aplicación desde un dispositivo móvil:Inicia el servidor Django en una terminal:Bashpython manage.py runserver
En otra terminal, inicia el túnel con Ngrok:Bashngrok http 8000
Copia la URL HTTPS generada (ej. https://tu-url.ngrok-free.app) y ábrela en tu celular.Nota: Si usas Ngrok, asegúrate de tener configurado CSRF_TRUSTED_ORIGINS en settings.py para evitar errores 403 Forbidden al subir imágenes.📊 Clases del Dataset (HAM10000)El modelo es capaz de clasificar las siguientes 7 lesiones:AbreviaturaNombre CompletoRiesgoakiecQueratosis Actínica⚠️ PrecancerosobccCarcinoma Basocelular🚨 MalignobklQueratosis Benigna✅ BenignodfDermatofibroma✅ BenignomelMelanoma🚨 Maligno (Alto Riesgo)nvNevus Melanocítico✅ Benigno (Lunar común)vascLesión Vascular✅ Benigno⚠️ Disclaimer MédicoADVERTENCIA: Esta herramienta es un prototipo desarrollado con fines académicos y de investigación.NO sustituye el diagnóstico de un profesional de la salud.Los resultados pueden tener márgenes de error.Ante cualquier duda sobre una lesión cutánea, consulte inmediatamente a un dermatólogo.👨‍💻 AutorIsmaelJrDevEstudiante de Ingeniería en Sistemas Computacionales.GitHub Profile