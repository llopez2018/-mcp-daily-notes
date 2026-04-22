import pytest
import os
import shutil
from daily_notes.server import create_note, _get_safe_path, NOTES_DIR

@pytest.fixture(autouse=True)
def setup_teardown():
    """Limpia la carpeta de notas antes y después de cada test."""
    if os.path.exists(NOTES_DIR):
        shutil.rmtree(NOTES_DIR)
    os.makedirs(NOTES_DIR)
    yield
    if os.path.exists(NOTES_DIR):
        shutil.rmtree(NOTES_DIR)

def test_create_note_success():
    """Foco Atómico: Verificar creación exitosa."""
    result = create_note("Test Note", "Contenido de prueba")
    assert "Éxito" in result
    assert os.path.exists(_get_safe_path("Test Note"))

def test_create_note_duplicate_eafp():
    """Foco Atómico: Verificar que EAFP maneja duplicados correctamente."""
    create_note("Duplicada", "Original")
    result = create_note("Duplicada", "Copia")
    assert "Conflicto" in result
