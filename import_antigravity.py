import os
import shutil
import zipfile
import sys

def import_antigravity_data(zip_path):
    if not os.path.exists(zip_path):
        print(f"Error: No se encontró el archivo de respaldo en {zip_path}")
        return

    # Define paths
    home_dir = os.path.expanduser("~")
    gemini_dir = os.path.join(home_dir, ".gemini")
    antigravity_dir = os.path.join(gemini_dir, "antigravity")

    print(f"Iniciando la importación de las conversaciones...")
    
    # Ensure .gemini directory exists
    if not os.path.exists(gemini_dir):
        os.makedirs(gemini_dir)
        print(f"Directorio creado: {gemini_dir}")

    # Backup existing antigravity directory if it exists
    if os.path.exists(antigravity_dir):
        backup_dir = f"{antigravity_dir}_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        shutil.move(antigravity_dir, backup_dir)
        print(f"El directorio existente de Antigravity fue respaldado en: {backup_dir}")

    # Extract zip file
    try:
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            # We are extracting directly to .gemini since the zip contains the 'antigravity' folder inside
            zipf.extractall(gemini_dir)
            
        print(f"\n¡Importación exitosa! 🎉")
        print(f"Tus conversaciones y configuración se han restaurado en {antigravity_dir}")
        print("Ahora puedes abrir Antigravity en este equipo y continuar donde lo dejaste.")
        
    except Exception as e:
        print(f"Ocurrió un error durante la importación: {e}")

if __name__ == "__main__":
    from datetime import datetime
    
    # Check if a file was provided as an argument
    if len(sys.argv) > 1:
        backup_file = sys.argv[1]
    else:
        print("Por favor, proporciona la ruta del archivo de respaldo (.zip) como argumento.")
        print("Ejemplo: python import_antigravity.py /ruta/al/archivo/antigravity_backup_20260512.zip")
        sys.exit(1)
        
    import_antigravity_data(backup_file)
