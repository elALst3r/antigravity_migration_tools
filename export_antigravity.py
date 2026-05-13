import os
import shutil
import zipfile
from datetime import datetime

def export_antigravity_data():
    # Define paths
    home_dir = os.path.expanduser("~")
    antigravity_dir = os.path.join(home_dir, ".gemini", "antigravity")
    
    if not os.path.exists(antigravity_dir):
        print(f"Error: No se encontró el directorio de Antigravity en {antigravity_dir}")
        return

    # Create export filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_filename = f"antigravity_backup_{timestamp}.zip"
    export_path = os.path.join(home_dir, "Desktop", export_filename)

    print(f"Iniciando la exportación de las conversaciones...")
    print(f"Directorio origen: {antigravity_dir}")
    print(f"Archivo destino: {export_path}")

    # Create zip file
    try:
        with zipfile.ZipFile(export_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(antigravity_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Create relative path to keep the directory structure clean inside the zip
                    arcname = os.path.relpath(file_path, os.path.join(antigravity_dir, '..'))
                    zipf.write(file_path, arcname)
        
        print(f"\n¡Exportación exitosa! 🎉")
        print(f"El archivo de respaldo se ha guardado en tu Escritorio: {export_path}")
        print("Ahora puedes transferir este archivo .zip a tu otro equipo.")
        
    except Exception as e:
        print(f"Ocurrió un error durante la exportación: {e}")

if __name__ == "__main__":
    export_antigravity_data()
