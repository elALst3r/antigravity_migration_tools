# Antigravity Migration Tools 

Conjunto de scripts simples en Python para exportar e importar sin esfuerzo el estado, historial y conocimiento de tus sesiones de **Antigravity**. Ideal para migrar tu entorno de trabajo de un equipo a otro sin perder tus conversaciones o configuraciones.

##  Características

- **Cero dependencias:** Creado utilizando únicamente la Librería Estándar de Python (no requiere `pip install`, ni entornos virtuales).
- **Copias de seguridad seguras:** El script de importación hace automáticamente un respaldo de la configuración existente en el equipo destino antes de sobreescribir los datos.
- **Fácil de usar:** Empaqueta toda la carpeta `~/.gemini/antigravity` en un solo archivo `.zip` comprimido y portátil.

---

##  Cómo utilizarlo

### 1. Exportar datos (Equipo de Origen)

Para crear un respaldo de tu entorno actual de Antigravity:

```bash
python3 export_antigravity.py
```

* **¿Qué hace?**: Generará un archivo `.zip` en tu Escritorio (Desktop) con la fecha y hora actuales (ej. `antigravity_backup_20260512_230139.zip`).
* Simplemente toma ese archivo generado y pásalo a tu nuevo equipo.

### 2. Importar datos (Equipo Destino)

Una vez que tengas el archivo `.zip` en tu nuevo equipo, utiliza el segundo script para restaurarlo:

```bash
python3 import_antigravity.py /ruta/hacia/tu/archivo_de_respaldo.zip
```

* **¿Qué hace?**:
  1. Verifica si ya existe una instalación de Antigravity en el equipo.
  2. Si existe, la renombra como respaldo de seguridad (ej. `antigravity_backup_20260512_230139`).
  3. Extrae el contenido del `.zip` en `~/.gemini/antigravity`.

¡Listo! Ya puedes abrir Antigravity en tu nuevo equipo y continuar justo donde lo dejaste.

---

## 💻 Requisitos

- Python 3.x
- Sistemas Operativos compatibles: macOS, Linux, Windows (requiere ligeros ajustes en las rutas base para Windows si se ejecuta fuera de WSL).
