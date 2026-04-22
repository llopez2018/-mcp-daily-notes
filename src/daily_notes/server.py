from mcp.server.fastmcp import FastMCP
import os
import re
import datetime
from typing import List, Optional

# --- Configuración de Dominio ---
mcp = FastMCP("Daily Notes Pro")
NOTES_DIR = os.path.join(os.getcwd(), "notes")
os.makedirs(NOTES_DIR, exist_ok=True)

def _get_safe_path(title: str) -> str:
    safe_title = re.sub(r'[^\w\s-]', '', title).strip()
    return os.path.join(NOTES_DIR, f"{safe_title}.md")

def _inject_metadata(title: str, content: str, category: str = "General") -> str:
    """Inyecta Frontmatter YAML para que la nota sea profesional y procesable."""
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

# --- Herramientas MCP Profesionales ---

@mcp.tool()
def create_note(title: str, content: str, category: str = "General") -> str:
    """
    Crea una nota con metadatos profesionales (YAML Frontmatter).
    Usa categorías como: Trabajo, Personal, Idea, Proyecto, Finanzas.
    """
    path = _get_safe_path(title)
    formatted_content = _inject_metadata(title, content, category)
    
    try:
        with open(path, 'x', encoding='utf-8') as f:
            f.write(formatted_content)
        return f"Éxito: Nota '{title}' creada con metadatos de categoría '{category}'."
    except FileExistsError:
        return f"Error: La nota '{title}' ya existe."
    except Exception as e:
        return f"Fallo: {str(e)}"

@mcp.tool()
def search_notes(query: str) -> str:
    """
    Busca una palabra o frase dentro de todas las notas.
    Esencial para encontrar información profesional sin conocer el título exacto.
    """
    results = []
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                path = os.path.join(NOTES_DIR, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if query.lower() in content.lower():
                        results.append(filename.replace(".md", ""))
        
        if not results:
            return f"No se encontraron notas que contengan '{query}'."
        return f"Notas que contienen '{query}':\n- " + "\n- ".join(results)
    except Exception as e:
        return f"Error en la búsqueda: {str(e)}"

@mcp.tool()
def list_by_category(category: str) -> str:
    """
    Lista notas filtrando por su categoría en los metadatos.
    """
    results = []
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                path = os.path.join(NOTES_DIR, filename)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if f"category: {category}" in content:
                        results.append(filename.replace(".md", ""))
        
        if not results:
            return f"No hay notas en la categoría '{category}'."
        return f"Notas en '{category}':\n- " + "\n- ".join(results)
    except Exception as e:
        return f"Error al filtrar: {str(e)}"

@mcp.tool()
def read_note(title: str) -> str:
    """Lee una nota completa."""
    path = _get_safe_path(title)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return f"Nota '{title}' no encontrada."

if __name__ == "__main__":
    mcp.run()
