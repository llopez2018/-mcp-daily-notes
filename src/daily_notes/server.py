from mcp.server.fastmcp import FastMCP
import os
import re
import datetime
import random
from typing import List, Optional

# --- Domain Configuration ---
mcp = FastMCP("Daily Notes Pro")
NOTES_DIR = os.path.abspath(os.path.join(os.getcwd(), "notes"))
os.makedirs(NOTES_DIR, exist_ok=True)
MAX_NOTE_SIZE_BYTES = 1024 * 1024

def _get_safe_path(title: str) -> str:
    """Security: Ensures path jail and sanitizes filenames."""
    safe_title = re.sub(r'[^\w\s-]', '', title).strip()
    if not safe_title:
        raise ValueError("Invalid title.")
    potential_path = os.path.abspath(os.path.join(NOTES_DIR, f"{safe_title}.md"))
    if not potential_path.startswith(NOTES_DIR):
        raise PermissionError("Directory Traversal detected.")
    return potential_path

def _sanitize_yaml_value(value: str) -> str:
    """Sanitizes strings for safe YAML injection."""
    return f'"{value.replace(chr(10), " ").replace(chr(34), str(chr(39)))}"'

def _inject_metadata(title: str, content: str, category: str = "General") -> str:
    """Injects YAML Frontmatter for professional interoperability."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = (
        "---\n"
        f"title: {_sanitize_yaml_value(title)}\n"
        f"date: {now}\n"
        f"category: {_sanitize_yaml_value(category)}\n"
        "status: active\n"
        "---\n\n"
    )
    return header + content

# --- Core Tools (English names for Global Standards) ---

@mcp.tool()
def create_note(title: str, content: str, category: str = "General") -> str:
    """
    Creates a new Markdown note with YAML metadata.
    ES: Crea una nueva nota Markdown con metadatos YAML.
    """
    try:
        path = _get_safe_path(title)
        if len(content.encode('utf-8')) > MAX_NOTE_SIZE_BYTES:
            return "Error: Payload exceeds 1MB limit."
        
        with open(path, 'x', encoding='utf-8') as f:
            f.write(_inject_metadata(title, content, category))
        return f"Success: Note '{title}' created in category '{category}'."
    except FileExistsError:
        return f"Error: Note '{title}' already exists."
    except Exception as e:
        return f"Failure: {str(e)}"

@mcp.tool()
def read_note(title: str) -> str:
    """
    Reads the full content of a specific note.
    ES: Lee el contenido completo de una nota específica.
    """
    try:
        path = _get_safe_path(title)
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return f"Error: Note '{title}' not found or invalid."

@mcp.tool()
def append_to_note(title: str, content: str) -> str:
    """
    Appends content to an existing note without overwriting.
    ES: Añade contenido a una nota existente sin sobrescribir.
    """
    try:
        path = _get_safe_path(title)
        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n---\n{content}")
        return f"Success: Note '{title}' updated."
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def search_notes(query: str) -> str:
    """
    Global search for a term inside all notes.
    ES: Búsqueda global de un término dentro de todas las notas.
    """
    results = []
    try:
        q = query.lower().strip()
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                with open(os.path.join(NOTES_DIR, filename), 'r', encoding='utf-8') as f:
                    if q in f.read().lower():
                        results.append(filename.replace(".md", ""))
        return f"Results for '{query}':\n- " + "\n- ".join(results) if results else "No results found."
    except Exception as e:
        return f"Search Error: {str(e)}"

@mcp.tool()
def list_by_category(category: str) -> List[str]:
    """
    Lists note titles filtered by YAML category.
    ES: Lista títulos de notas filtrados por categoría YAML.
    """
    results = []
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                with open(os.path.join(NOTES_DIR, filename), 'r', encoding='utf-8') as f:
                    if f"category: \"{category}\"" in f.read():
                        results.append(filename.replace(".md", ""))
        return results
    except Exception:
        return []

@mcp.tool()
def get_pending_tasks() -> str:
    """
    Extracts all pending tasks (- [ ]) from every note.
    ES: Extrae todas las tareas pendientes (- [ ]) de cada nota.
    """
    tasks = []
    pattern = re.compile(r'^\s*-\s*\[\s\]\s+(.*)$', re.MULTILINE)
    try:
        for filename in os.listdir(NOTES_DIR):
            if filename.endswith(".md"):
                with open(os.path.join(NOTES_DIR, filename), 'r', encoding='utf-8') as f:
                    matches = pattern.findall(f.read())
                    for m in matches:
                        tasks.append(f"[{filename.replace('.md', '')}] {m}")
        return "Pending Tasks:\n" + "\n".join(tasks) if tasks else "No pending tasks found."
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def get_random_note(category: Optional[str] = None) -> str:
    """
    Picks a random note, optionally filtered by category.
    ES: Selecciona una nota al azar, opcionalmente filtrada por categoría.
    """
    try:
        notes = list_by_category(category) if category else [f.replace(".md", "") for f in os.listdir(NOTES_DIR) if f.endswith(".md")]
        if not notes: return "No notes found."
        chosen = random.choice(notes)
        return f"Random Note: '{chosen}'. Use read_note to explore it."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
