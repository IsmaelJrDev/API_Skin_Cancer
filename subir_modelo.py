# upload_models.py
import pymongo
import gridfs
import os
from core.settings import MONGO_URI

def upload_to_atlas():
    print("Conectando a MongoDB Atlas...")
    client = pymongo.MongoClient(MONGO_URI)
    db = client['SkinCancerDB']
    fs = gridfs.GridFS(db)

    # Lista tus modelos aquí
    modelos = {
        #'resnet_model': 'modelo_final_skin_cancer_resnet.keras', # Nombre en DB : Nombre archivo real
        'alexnet_model': 'mejor_modelo_skin.keras'
    }

    for db_name, file_path in modelos.items():
        if os.path.exists(file_path):
            print(f"Subiendo {db_name}...")
            
            # Borrar si ya existe para actualizarlo
            existing = fs.find_one({"filename": db_name})
            if existing:
                fs.delete(existing._id)
            
            with open(file_path, 'rb') as f:
                fs.put(f, filename=db_name)
            print(f"✅ {db_name} subido correctamente.")
        else:
            print(f"❌ Error: No encuentro el archivo {file_path}")

if __name__ == "__main__":
    upload_to_atlas()