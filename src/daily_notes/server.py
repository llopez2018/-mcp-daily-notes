from mcp.server.fastmcp import FastMCP
import os
import re
import datetime
import random
from typing import List, Optional

# --- Configuración de Dominio ---
mcp = FastMCP("Daily Notes Pro")
NOTES_DIR = os.path.join(os.getcwd(), "notes")
os.makedirs(NOTES_DIR, exist_ok=True)

def _get_safe_path(title: str) -> str:
    safe_title = re.sub(r'[^\w\s-]', '', title).strip()
    return os.path.join(NOTES_DIR, f"{safe_title}.md")

def _inject_metadata(title: str, content: str, category: str = "General") -> str:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = (
        "---\n"
        f"title: {title}\n"
        f"date: {now}\n"
        f"category: {category}\n"
        "status: active\n"
        "---\n\n"
    )
    return header + content

# --- Herramientas Core ---

@mcp.tool()
def create_note(title: str, content: str, category: str = "General") -> str:
    """Crea una nota con metadatos (YAML Frontmatter). Usa categorías descriptivas."""
    path = _get_safe_path(title)
    formatted_content = _inject_metadata(title, content, category)
    try:
        with open(path, 'x', encoding='utf-8') as f:
            f.write(formatted_content)
        return f"Éxito: Nota '{title}' creada."
    except FileExistsError:
        return f"Error: La nota '{title}' ya existe."
    except Exception as e:
        return f"Fallo: {str(e)}"

@mcp.tool()
def read_note(title: str) -> str:
    """Lee una nota completa."""
    path = _get_safe_path(title)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Nota '{title}' no encontrada."

@mcp.tool()
def append_to_note(title: str, content: str) -> str:
    """Añade contenido al final de una nota existente sin borrar lo anterior."""
    path = _get_safe_path(title)
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n---\n{content}")
        return f"Nota '{title}' actualizada."
    except Exception as e:
        return f"Error: {str(e)}"

# --- Herramientas Divergentes (IA Avanzada) ---

@mcp.tool()
def extract_pending_tasks() -> str:
    """
    Busca en TODAS las notas buscando checkboxes markdown sin marcar: '- [ ]'.
    Útil para consolidar tareas dispersas en un solo reporte.
    """
    tasks = []
    task_pattern = re.compile(r'^\s*-\s*\[\s\]\s+(.*)$', re.MULTILINE)
    
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                with open(os.path.join(NOTES_DIR, filename), 'r', encoding='utf-8') as f:
                    content = f.read()
                    matches = task_pattern.findall(content)
                    for match in matches:
                        tasks.append(f"[{filename.replace('.md', '')}] {match}")
        
        if not tasks:
            return "No hay tareas pendientes (- [ ]) en ninguna nota."
        return "Tareas pendientes encontradas:\n" + "\n".join(tasks)
    except Exception as e:
        return f"Error extrayendo tareas: {str(e)}"

@mcp.tool()
def get_recent_notes(days: int = 7) -> str:
    """
    Obtiene las notas modificadas o creadas en los últimos X días.
    Útil para generar resúmenes semanales o recordar qué pasó recientemente.
    """
    recent_notes = []
    cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
    
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                path = os.path.join(NOTES_DIR, filename)
                # Obtenemos la fecha de modificación del archivo (EAFP)
                mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path))
                if mtime >= cutoff_date:
                    recent_notes.append(filename.replace(".md", ""))
                    
        if not recent_notes:
            return f"No hay notas en los últimos {days} días."
        return f"Notas de los últimos {days} días:\n- " + "\n- ".join(recent_notes)
    except Exception as e:
        return f"Error buscando notas recientes: {str(e)}"

@mcp.tool()
def get_random_note(category: Optional[str] = None) -> str:
    """
    Obtiene el título de una nota al azar. Opcionalmente filtrada por categoría.
    Útil para romper bloqueos creativos, hacer repasos espaciados o buscar serendipia.
    """
    valid_notes = []
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                if category:
                    path = os.path.join(NOTES_DIR, filename)
                    with open(path, 'r', encoding='utf-8') as f:
                        if f"category: {category}" in f.read():
                            valid_notes.append(filename.replace(".md", ""))
                else:
                    valid_notes.append(filename.replace(".md", ""))
        
        if not valid_notes:
            return "No se encontraron notas para sacar al azar."
            
        chosen = random.choice(valid_notes)
        return f"Nota aleatoria seleccionada: '{chosen}'. Usa read_note('{chosen}') para leerla."
    except Exception as e:
        return f"Error seleccionando nota al azar: {str(e)}"

@mcp.tool()
def search_notes(query: str) -> str:
    """Busca una palabra o frase dentro de todas las notas."""
    results = []
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                path = os.path.join(NOTES_DIR, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    if query.lower() in f.read().lower():
                        results.append(filename.replace(".md", ""))
        
        if not results:
            return f"No se encontraron notas que contengan '{query}'."
        return f"Notas que contienen '{query}':\n- " + "\n- ".join(results)
    except Exception as e:
        return f"Error en la búsqueda: {str(e)}"

if __name__ == "__main__":
    mcp.run()
