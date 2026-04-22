from mcp.server.fastmcp import FastMCP
import os
import re
import datetime
import random
from typing import List, Optional

# --- Configuración de Dominio ---
mcp = FastMCP("Daily Notes Pro")

# Usamos ruta absoluta para NOTES_DIR para evitar ambigüedades en la validación
NOTES_DIR = os.path.abspath(os.path.join(os.getcwd(), "notes"))
os.makedirs(NOTES_DIR, exist_ok=True)

# Seguridad: Límite máximo de tamaño para una nota (1 MB) para prevenir DoS
MAX_NOTE_SIZE_BYTES = 1024 * 1024

def _get_safe_path(title: str) -> str:
    """
    Genera una ruta de archivo segura dentro de NOTES_DIR.
    Implementa protección contra Directory Traversal (Path Jail).
    """
    # 1. Sanitización de caracteres (Regex)
    safe_title = re.sub(r'[^\w\s-]', '', title).strip()
    if not safe_title:
        raise ValueError("El título de la nota no puede estar vacío o contener solo caracteres especiales.")
    
    # 2. Resolución de ruta absoluta
    potential_path = os.path.abspath(os.path.join(NOTES_DIR, f"{safe_title}.md"))
    
    # 3. Verificación de Path Jail: la ruta resultante DEBE estar dentro de NOTES_DIR
    if not potential_path.startswith(NOTES_DIR):
        raise PermissionError("Acceso denegado: Intento de salida de directorio (Jailbreak) detectado.")
        
    return potential_path

def _sanitize_yaml_value(value: str) -> str:
    """Sanitiza strings para su inserción segura en el Frontmatter YAML."""
    # Eliminamos saltos de línea y escapamos comillas dobles
    clean_val = value.replace('\n', ' ').replace('\r', '').replace('"', "'")
    return f'"{clean_val}"'

def _inject_metadata(title: str, content: str, category: str = "General") -> str:
    """Inyecta Frontmatter YAML sanitizado para interoperabilidad segura."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    safe_title = _sanitize_yaml_value(title)
    safe_category = _sanitize_yaml_value(category)
    
    header = (
        "---\n"
        f"title: {safe_title}\n"
        f"date: {now}\n"
        f"category: {safe_category}\n"
        "status: active\n"
        "---\n\n"
    )
    return header + content

# --- Herramientas Core ---

@mcp.tool()
def create_note(title: str, content: str, category: str = "General") -> str:
    """Crea una nota con metadatos (YAML Frontmatter). Usa categorías descriptivas."""
    try:
        path = _get_safe_path(title)
        
        # Validación de tamaño de payload
        if len(content.encode('utf-8')) > MAX_NOTE_SIZE_BYTES:
            return "Error de Seguridad: El contenido de la nota excede el límite permitido de 1MB."

        formatted_content = _inject_metadata(title, content, category)
        
        # 'x' para creación exclusiva (falla si el archivo ya existe)
        with open(path, 'x', encoding='utf-8') as f:
            f.write(formatted_content)
        return f"Éxito: Nota '{title}' creada y categorizada como '{category}'."
    except FileExistsError:
        return f"Error: La nota '{title}' ya existe. Usa append_to_note si deseas añadir información."
    except (ValueError, PermissionError) as ve:
        return f"Error de Validación/Seguridad: {str(ve)}"
    except Exception as e:
        return f"Fallo Inesperado: {str(e)}"

@mcp.tool()
def read_note(title: str) -> str:
    """Lee una nota completa. Utiliza EAFP para el manejo de archivos."""
    try:
        path = _get_safe_path(title)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except (FileNotFoundError, ValueError, PermissionError):
        return f"Nota '{title}' no encontrada o ruta no válida."
    except Exception as e:
        return f"Error de lectura: {str(e)}"

@mcp.tool()
def append_to_note(title: str, content: str) -> str:
    """Añade contenido al final de una nota existente sin borrar lo anterior."""
    try:
        path = _get_safe_path(title)
        
        # Validación de tamaño (considerando el archivo actual + el nuevo contenido)
        current_size = os.path.getsize(path) if os.path.exists(path) else 0
        new_content_size = len(content.encode('utf-8'))
        
        if (current_size + new_content_size) > MAX_NOTE_SIZE_BYTES:
            return "Error de Seguridad: La nota resultante excedería el límite de 1MB."

        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n---\n{content}")
        return f"Nota '{title}' actualizada exitosamente."
    except Exception as e:
        return f"Error al actualizar la nota: {str(e)}"

# --- Herramientas de Análisis y Búsqueda ---

@mcp.tool()
def extract_pending_tasks() -> str:
    """
    Consolida todas las tareas pendientes (- [ ]) de todas las notas.
    """
    tasks = []
    task_pattern = re.compile(r'^\s*-\s*\[\s\]\s+(.*)$', re.MULTILINE)
    
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                # No necesitamos _get_safe_path aquí porque listamos directamente del directorio controlado
                with open(os.path.join(NOTES_DIR, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = task_pattern.findall(content)
                    for match in matches:
                        tasks.append(f"[{filename.replace('.md', '')}] {match}")
        
        if not tasks:
            return "No hay tareas pendientes detectadas."
        return "Tareas pendientes consolidadas:\n" + "\n".join(tasks)
    except Exception as e:
        return f"Error al procesar tareas: {str(e)}"

@mcp.tool()
def get_recent_notes(days: int = 7) -> str:
    """
    Lista los títulos de las notas modificadas recientemente.
    """
    recent_notes = []
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
    
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                path = os.path.join(NOTES_DIR, filename)
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path))
                if mtime >= cutoff_date:
                    recent_notes.append(filename.replace(".md", ""))
                    
        if not recent_notes:
            return f"No hay actividad reciente en los últimos {days} días."
        return f"Notas recientes ({days} días):\n- " + "\n- ".join(recent_notes)
    except Exception as e:
        return f"Error al escanear notas recientes: {str(e)}"

@mcp.tool()
def search_notes(query: str) -> str:
    """Busca un término específico dentro del contenido de todas las notas."""
    results = []
    try:
        # Sanitización de la query simple
        clean_query = query.lower().strip()
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                path = os.path.join(NOTES_DIR, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    if clean_query in f.read().lower():
                        results.append(filename.replace(".md", ""))
        
        if not results:
            return f"Cero resultados para '{query}'."
        return f"Coincidencias encontradas en:\n- " + "\n- ".join(results)
    except Exception as e:
        return f"Error en búsqueda global: {str(e)}"

if __name__ == "__main__":
    mcp.run()
