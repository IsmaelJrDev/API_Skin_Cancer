import os
import numpy as np
import cv2
import tensorflow as tf
import datetime  # <--- NECESARIO PARA LA FECHA
import pymongo   # <--- NECESARIO PARA CONECTAR
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# --- CONFIGURACIÓN MONGO ---
# Usamos el URI que tienes en settings.py
client = pymongo.MongoClient(settings.MONGO_URI)
db = client['SkinCancerDB']
collection = db['historial_diagnosticos'] # Nueva colección para guardar los casos

# --- CACHÉ DE MODELOS (Igual que antes) ---
loaded_models = {}

def get_model(model_key):
    # ... (Mismo código de carga local que te di en la respuesta anterior) ...
    if model_key in loaded_models:
        return loaded_models[model_key]
    
    file_map = {
        #'resnet_model': 'modelo_final_skin_cancer_resnet.keras',
        'alexnet_model': 'mejor_modelo_skin.keras'
    }
    filename = file_map.get(model_key)
    model_path = os.path.join(settings.BASE_DIR, 'modelos_entrenados', filename)
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"No encuentro el modelo en: {model_path}")
        
    model = tf.keras.models.load_model(model_path)
    loaded_models[model_key] = model
    return model

def preprocess_image(filepath):
    # ... (Mismo código de preprocesamiento) ...
    img = cv2.imread(filepath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)
    return img

def home(request):
    context = {}
    
    # Si queremos mostrar el historial reciente en la parte de abajo de la web (Opcional)
    # latests = collection.find().sort("fecha", -1).limit(5)
    # context['historial'] = latests

    if request.method == 'POST' and request.FILES.get('imagen'):
        imagen = request.FILES['imagen']
        modelo_elegido = request.POST.get('modelo_select', 'resnet_model')
        
        # 1. Guardar imagen en disco local
        fs_storage = FileSystemStorage()
        filename = fs_storage.save(imagen.name, imagen)
        file_url = fs_storage.url(filename)      # URL para el navegador (/media/foto.jpg)
        file_path = fs_storage.path(filename)    # Ruta absoluta para OpenCV
        
        try:
            # 2. Predecir
            model = get_model(modelo_elegido)
            processed_img = preprocess_image(file_path)
            prediction = model.predict(processed_img)
            
            # 3. Interpretar
            classes = [
                'Queratosis Actínica (akiec)', 'Carcinoma Basocelular (bcc)', 
                'Queratosis Benigna (bkl)', 'Dermatofibroma (df)', 
                'Melanoma (mel)', 'Nevus (nv)', 'Vascular (vasc)'
            ]
            
            if prediction.ndim > 1: prediction = prediction[0]
            class_idx = np.argmax(prediction)
            confidence = float(np.max(prediction)) * 100
            diagnosis = classes[class_idx]
            is_danger = class_idx in [0, 1, 4] # Akiec, BCC, Melanoma

            # --- AQUÍ ES DONDE GUARDAMOS EN MONGO ATLAS ---
            registro_medico = {
                "nombre_imagen": filename,
                "url_imagen": file_url,         # Guardamos la referencia, no el archivo binario
                "diagnostico": diagnosis,
                "confianza": round(confidence, 2),
                "es_peligroso": is_danger,
                "modelo_usado": "ResNet50" if "resnet" in modelo_elegido else "AlexNet",
                "fecha": datetime.datetime.now(), # Fecha y hora actual
                "ip_usuario": request.META.get('REMOTE_ADDR') # Opcional: IP del usuario
            }
            
            # Insertar en la nube
            collection.insert_one(registro_medico)
            print("✅ Registro guardado en MongoDB Atlas exitosamente.")

            # Contexto para el Frontend
            context = {
                'result': diagnosis,
                'confidence': round(confidence, 2),
                'is_danger': is_danger,
                'image_url': file_url,
                'model_name': registro_medico['modelo_usado']
            }
            
        except Exception as e:
            context['error'] = f"Error en el análisis: {str(e)}"
            print(e)

    return render(request, 'index.html', context)