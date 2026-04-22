import pytest
import os
import shutil
from daily_notes.server import (
    create_note, 
    extract_pending_tasks, 
    _get_safe_path, 
    NOTES_DIR
)

@pytest.fixture(autouse=True)
def setup_teardown():
    """Limpia la carpeta de notas antes y después de cada test."""
    if os.path.exists(NOTES_DIR):
        shutil.rmtree(NOTES_DIR)
    os.makedirs(NOTES_DIR)
    yield
    if os.path.exists(NOTES_DIR):
        shutil.rmtree(NOTES_DIR)

def test_extract_pending_tasks():
    """Foco Atómico: Verificar que extrae checkboxes correctos."""
    content1 = "Reunión OK\n- [ ] Arreglar bug\n- [x] Hecho"
    content2 = "Ideas:\n- [ ] Comprar café"
    
    create_note("Trabajo", content1)
    create_note("Personal", content2)
    
    tasks = extract_pending_tasks()
    assert "Arreglar bug" in tasks
    assert "Comprar café" in tasks
    assert "Hecho" not in tasks # No debe traer tareas completadas
