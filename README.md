# 🏥 API de Detección de Cáncer de Piel

API desarrollada como evaluación de la materia de graficación, la cual permite a los usuarios enviar una foto de la piel y detectar si tiene cáncer o no utilizando redes neuronales convolucionales (ResNet y AlexNet).

## 🚀 Características

- **Detección de Cáncer de Piel**: Utiliza modelos de deep learning para detectar cáncer de piel en imágenes
- **Dos Modelos Disponibles**: 
  - **ResNet50**: Red neuronal profunda con arquitectura residual
  - **AlexNet**: Arquitectura clásica de deep learning
- **Visualización de Áreas**: Grad-CAM para mostrar dónde se detecta el cáncer en la imagen
- **Frontend Moderno**: Interfaz web profesional con TailwindCSS
- **API RESTful**: Endpoints para integración con otras aplicaciones

## 🛠️ Tecnologías

- **Backend**: Django 5.0, Django REST Framework
- **Machine Learning**: TensorFlow 2.15, Keras
- **Procesamiento de Imágenes**: OpenCV, Pillow
- **Frontend**: HTML5, TailwindCSS, JavaScript
- **Tunneling**: ngrok, rathole

## 📋 Requisitos

- Python 3.8+
- pip
- Virtual environment (recomendado)

## 🔧 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd API_Skin_Cancer
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Linux/Mac
# o
venv\Scripts\activate  # En Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

Edita el archivo `.env` y agrega:
```
SECRET_KEY=tu-clave-secreta-aqui
DEBUG=True
NGROK_AUTH_TOKEN=tu-token-de-ngrok  # Opcional, para ngrok
```

### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

## 🚀 Uso

### Iniciar servidor de desarrollo

```bash
python manage.py runserver
```

La aplicación estará disponible en `http://localhost:8000`

### Iniciar con ngrok (para acceso público)

```bash
# Opción 1: Usar el script automatizado
chmod +x scripts/start_server.sh
./scripts/start_server.sh

# Opción 2: Manual
python manage.py runserver 8000 &
python scripts/start_ngrok.py 8000
```

### Iniciar con rathole (requiere servidor remoto)

1. Edita `scripts/rathole_config.toml` con tu configuración
2. Ejecuta:
```bash
chmod +x scripts/start_rathole.sh
./scripts/start_rathole.sh
```

## 📡 API Endpoints

### POST `/api/detect/`

Detecta cáncer de piel en una imagen.

**Parámetros:**
- `image` (file): Archivo de imagen a analizar
- `model` (string, opcional): Modelo a usar (`resnet` o `alexnet`). Por defecto: `resnet`

**Ejemplo con curl:**
```bash
curl -X POST http://localhost:8000/api/detect/ \
  -F "image=@ruta/a/imagen.jpg" \
  -F "model=resnet"
```

**Respuesta:**
```json
{
  "success": true,
  "detection_id": 1,
  "has_cancer": false,
  "confidence": 0.2345,
  "model_used": "resnet",
  "heatmap": "data:image/jpeg;base64,...",
  "message": "No se detectó cáncer"
}
```

### GET `/api/health/`

Verifica el estado de la API.

**Respuesta:**
```json
{
  "status": "healthy",
  "models_loaded": true
}
```

## 🎨 Frontend

El frontend está disponible en la ruta raíz (`/`) y permite:
- Subir imágenes mediante drag & drop o selección de archivo
- Seleccionar entre modelos ResNet50 y AlexNet
- Visualizar resultados con mapa de calor (Grad-CAM)
- Ver nivel de confianza de la detección

## 🧠 Modelos de Machine Learning

### ResNet50
- Arquitectura: ResNet50 pre-entrenada en ImageNet
- Capas personalizadas: GlobalAveragePooling2D, Dense layers con Dropout
- Salida: Clasificación binaria (cáncer / no cáncer)

### AlexNet (basado en VGG16)
- Arquitectura: VGG16 pre-entrenada en ImageNet (arquitectura similar a AlexNet)
- Capas personalizadas: Dense layers grandes (4096, 1024, 256) estilo AlexNet
- Salida: Clasificación binaria (cáncer / no cáncer)
- Nota: Usamos VGG16 como base ya que TensorFlow no incluye AlexNet pre-entrenado directamente

### Grad-CAM
- Visualización de áreas de interés en la imagen
- Mapa de calor que muestra dónde el modelo detecta características relevantes

## 📁 Estructura del Proyecto

```
API_Skin_Cancer/
├── detection/              # App principal de detección
│   ├── models.py          # Modelos de Django
│   ├── views.py           # Vistas de la API
│   ├── ml_models.py       # Modelos de ML (ResNet, AlexNet)
│   └── urls.py            # URLs de la app
├── skin_cancer_api/       # Configuración del proyecto
│   ├── settings.py        # Configuración de Django
│   └── urls.py            # URLs principales
├── templates/             # Plantillas HTML
│   └── index.html         # Frontend principal
├── scripts/               # Scripts de utilidad
│   ├── start_ngrok.py     # Script para ngrok
│   ├── start_server.sh    # Script para iniciar servidor
│   └── rathole_config.toml # Configuración de rathole
├── media/                 # Archivos subidos (generado)
├── models/                # Modelos entrenados (generado)
└── requirements.txt       # Dependencias
```

## ⚠️ Notas Importantes

1. **Modelos Pre-entrenados**: Los modelos se crean automáticamente la primera vez que se ejecuta la aplicación. Para mejores resultados, deberías entrenar los modelos con un dataset de cáncer de piel.

2. **Producción**: Este proyecto está configurado para desarrollo. Para producción:
   - Cambia `DEBUG = False`
   - Configura una base de datos adecuada (PostgreSQL, MySQL)
   - Usa un servidor web (Gunicorn, uWSGI)
   - Configura HTTPS

3. **Datos Médicos**: Esta API es solo para fines educativos. No debe usarse para diagnósticos médicos reales sin validación clínica adecuada.

## 📝 Licencia

Ver archivo LICENSE

## 👥 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o pull request.

## 📧 Contacto

Para preguntas o soporte, abre un issue en el repositorio.
