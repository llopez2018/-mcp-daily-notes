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
        raise ValueError("Invalid title: Title is empty or contains only special characters.")
    potential_path = os.path.abspath(os.path.join(NOTES_DIR, f"{safe_title}.md"))
    if not potential_path.startswith(NOTES_DIR):
        raise PermissionError("Security Alert: Directory Traversal attempt detected.")
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

# --- Core Tools (Pure English Functional Logic) ---

@mcp.tool()
def create_note(title: str, content: str, category: str = "General") -> str:
    """
    Creates a new Markdown note with YAML metadata.
    ES: Crea una nueva nota Markdown con metadatos YAML.
    """
    try:
        path = _get_safe_path(title)
        if len(content.encode('utf-8')) > MAX_NOTE_SIZE_BYTES:
            return "Error: Payload size limit exceeded (1MB)."
        
        with open(path, 'x', encoding='utf-8') as f:
            f.write(_inject_metadata(title, content, category))
        return f"Success: Note '{title}' created in category '{category}'."
    except FileExistsError:
        return f"Error: Note '{title}' already exists. Use append_to_note to add content."
    except (ValueError, PermissionError) as ve:
        return f"Validation Error: {str(ve)}"
    except Exception as e:
        return f"System Failure: {str(e)}"

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
    except (FileNotFoundError, ValueError, PermissionError):
        return f"Error: Note '{title}' not found or access denied."
    except Exception as e:
        return f"Read Error: {str(e)}"

@mcp.tool()
def append_to_note(title: str, content: str) -> str:
    """
    Appends content to an existing note.
    ES: Añade contenido a una nota existente.
    """
    try:
        path = _get_safe_path(title)
        # Size validation for existing file + new content
        current_size = os.path.getsize(path) if os.path.exists(path) else 0
        if (current_size + len(content.encode('utf-8'))) > MAX_NOTE_SIZE_BYTES:
            return "Error: Appending this content would exceed the 1MB limit."

        with open(path, 'a', encoding='utf-8') as f:
            f.write(f"\n\n---\n{content}")
        return f"Success: Note '{title}' updated."
    except Exception as e:
        return f"Update Failure: {str(e)}"

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
        
        if not results:
            return f"No matches found for query: '{query}'"
        return f"Matches found in:\n- " + "\n- ".join(results)
    except Exception as e:
        return f"Search System Error: {str(e)}"

@mcp.tool()
def get_pending_tasks() -> str:
    """
    Extracts all pending tasks (- [ ]) from every note.
    ES: Extrae todas las tareas pendientes (- [ ]) de todas las notas.
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
        
        if not tasks:
            return "No pending tasks detected in the system."
        return "Consolidated Pending Tasks:\n" + "\n".join(tasks)
    except Exception as e:
        return f"Task Extraction Error: {str(e)}"

if __name__ == "__main__":
    mcp.run()
