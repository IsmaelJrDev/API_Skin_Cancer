# 🩺 API Skin Cancer Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.0-green)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange)
![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-06B6D4)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248)

Un sistema de **apoyo al diagnóstico dermatológico** basado en
Inteligencia Artificial. Esta aplicación web permite a los usuarios
subir imágenes dermatoscópicas y recibir una predicción sobre la
naturaleza de la lesión (benigna o maligna) utilizando modelos de **Deep
Learning (ResNet50 y AlexNet)** entrenados con el dataset HAM10000.

La aplicación registra automáticamente el historial de diagnósticos en
**MongoDB Atlas** y cuenta con una interfaz moderna construida con
**TailwindCSS**.



## 🚀 Características Principales

-   **Multi-Modelo:** El usuario puede elegir entre dos arquitecturas
    neuronales:
    -   **ResNet50** (Transfer Learning): Alta precisión.
    -   **AlexNet** (Custom Architecture): Modelo clásico entrenado
        desde cero.
-   **Análisis en Tiempo Real:** Procesamiento de imágenes y predicción
    en segundos.
-   **Historial en la Nube:** Cada diagnóstico se guarda en MongoDB
    Atlas con metadatos (fecha, confianza, tipo de lesión).
-   **Interfaz Responsive:** Frontend profesional diseñado con
    TailwindCSS.
-   **Detección de Riesgo:** Sistema de alertas automático si la lesión
    es clasificada como Melanoma o Carcinoma.



## 🛠️ Stack Tecnológico

-   **Backend:** Django (Python)
-   **IA / ML:** TensorFlow, Keras, OpenCV, NumPy
-   **Base de Datos:** MongoDB Atlas
-   **Frontend:** HTML5, TailwindCSS (CDN)
-   **Exposición:** Ngrok



## 📂 Estructura del Proyecto

``` bash
API_Skin_Cancer/
├── core/
├── diagnosis/
│   ├── templates/
│   └── views.py
├── media/
├── modelos_entrenados/
│   ├── modelo_final_skin_cancer_alexnet.keras
│   └── modelo_final_skin_cancer_resnet.keras
├── manage.py
└── requirements.txt
```



## ⚙️ Instalación y Configuración

### 1. Clonar el repositorio

``` bash
git clone https://github.com/IsmaelJrDev/API_Skin_Cancer.git
cd API_Skin_Cancer
```

### 2. Crear entorno virtual

``` bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

``` bash
pip install -r requirements.txt
```

### 4. Colocar los modelos entrenados

Crea una carpeta llamada **modelos_entrenados** y coloca:

-   modelo_final_skin_cancer_resnet.keras\
-   modelo_final_skin_cancer_alexnet.keras

### 5. Configurar MongoDB Atlas

En `core/settings.py`:

``` python
MONGO_URI = "mongodb+srv://<usuario>:<password>@cluster..."
```



## ▶️ Ejecución

### Modo Local

``` bash
python manage.py runserver
```

### Modo Público (Ngrok)

``` bash
ngrok http 8000
```



## 📊 Clases del Dataset (HAM10000)

| Abrev. | Nombre                 | Riesgo          |
|--------|-------------------------|-----------------|
| akiec  | Queratosis Actínica    | ⚠️ Precanceroso |
| bcc    | Carcinoma Basocelular  | 🚨 Maligno      |
| bkl    | Queratosis Benigna     | ✅ Benigno      |
| df     | Dermatofibroma         | ✅ Benigno      |
| mel    | Melanoma               | 🚨 Maligno      |
| nv     | Nevus Melanocítico     | ✅ Benigno      |
| vasc   | Lesión Vascular        | ✅ Benigno      |



## ⚠️ Disclaimer Médico

Esta herramienta es un prototipo académico.\
**No sustituye la opinión de un dermatólogo.**



## 👨‍💻 Autor

**IsmaelJrDev**\
Estudiante de Ingeniería en Sistemas Computacionales.\
GitHub: https://github.com/IsmaelJrDev
