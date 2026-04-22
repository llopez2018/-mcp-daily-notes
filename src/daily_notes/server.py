from mcp.server.fastmcp import FastMCP
import os
import re
from typing import List

# --- Configuración de Dominio ---
mcp = FastMCP("Daily Notes")
NOTES_DIR = os.path.join(os.getcwd(), "notes")

# Aseguramos infraestructura mínima (Practicality beats purity)
os.makedirs(NOTES_DIR, exist_ok=True)

def _get_safe_path(title: str) -> str:
    """Helper interno: Limpia el título y devuelve la ruta absoluta."""
    safe_title = re.sub(r'[^\w\s-]', '', title).strip()
    return os.path.join(NOTES_DIR, f"{safe_title}.md")

# --- Herramientas MCP (Capa de Aplicación) ---

@mcp.tool()
def create_note(title: str, content: str) -> str:
    """
    Crea una nueva nota Markdown.
    Aplica filosofía EAFP: Intenta escribir y maneja si ya existe.
    """
    path = _get_safe_path(title)
    
    try:
        # Usamos 'x' para forzar error si el archivo ya existe
        with open(path, 'x', encoding='utf-8') as f:
            f.write(content)
        return f"Éxito: Nota '{title}' creada en el sistema."
    except FileExistsError:
        return f"Conflicto: La nota '{title}' ya existe. Usa append_to_note para actualizarla."
    except Exception as e:
        return f"Fallo Crítico: No se pudo crear la nota debido a: {str(e)}"

@mcp.tool()
def read_note(title: str) -> str:
    """
    Lee el contenido de una nota.
    Usa EAFP para evitar chequeos redundantes de 'os.path.exists'.
    """
    path = _get_safe_path(title)
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f"--- {title} ---\n\n{f.read()}"
    except FileNotFoundError:
        return f"Error: La nota '{title}' no fue encontrada en el repositorio local."
    except Exception as e:
        return f"Error de Lectura: {str(e)}"

@mcp.tool()
def list_notes() -> List[str]:
    """
    Devuelve una lista de todos los títulos de notas disponibles.
    """
    try:
        return [f.replace(".md", "") for f in os.listdir(NOTES_DIR) if f.endswith(".md")]
    except Exception:
        return []

@mcp.tool()
def append_to_note(title: str, content: str) -> str:
    """
    Añade contenido al final de una nota existente sin borrar lo anterior.
    """
    path = _get_safe_path(title)
    try:
        # 'a' (append) fallará en sistemas de archivos si hay problemas de permisos
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n---\n{content}")
        return f"Nota '{title}' actualizada exitosamente."
    except Exception as e:
        return f"Error al intentar actualizar '{title}': {str(e)}"

if __name__ == "__main__":
    mcp.run()
