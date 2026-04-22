# 📓 MCP Daily Notes: Tu Cerebro Externo en Markdown

[![MCP Protocol](https://img.shields.io/badge/MCP-Standard-blue.svg)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)

**MCP Daily Notes** es un servidor para el Model Context Protocol que permite a cualquier IA (Cursor, Claude Desktop, OpenClaw, Gemini CLI) gestionar tu conocimiento personal, diario y notas directamente en archivos Markdown locales con metadatos profesionales (YAML).

> "No más 'se me olvidó'. Ahora tu IA tiene memoria persistente, categorizada y buscable en tu propio disco duro."

---

## 🎯 Casos de Uso e Integraciones

Este MCP no es solo para escribir texto; es un "Segundo Cerebro" estructurado. Al generar archivos `.md` con Frontmatter YAML, la interoperabilidad es total.

### 💼 Entorno Profesional (Productividad y Gestión)

**1. El Asistente de Reuniones (Integración Local)**
*   **El Problema:** Tienes reuniones por Zoom y haces notas dispersas.
*   **La Solución:** Le dictas a la IA los puntos clave.
*   **El Prompt:** *"Crea una nota de la reunión de hoy con el equipo de Naves Industriales. Categoría: 'Reuniones'. Pon los acuerdos a los que llegamos."*
*   **Impacto:** El MCP genera el archivo. Si usas un software como **Notion** (vía importación) o **Obsidian** en tu trabajo, ese archivo `.md` aparece automáticamente en tu bóveda con la fecha de hoy.

**2. Gestor de Tareas y Contexto de Proyecto (Integración con Cursor IDE)**
*   **El Problema:** Cuando cierras tu editor de código (Cursor/VS Code), la IA olvida dónde te quedaste.
*   **La Solución:** Usar el MCP como "Bitácora de Arquitectura".
*   **El Prompt:** *"Añade al final de la nota 'Contexto-Proyecto-X' que mañana debo arreglar el timeout de la base de datos."*
*   **Impacto:** Al día siguiente, le dices a la IA *"Lee la nota 'Contexto-Proyecto-X' y dime qué nos faltó ayer"*. La IA recupera la memoria instantáneamente.

### 🏠 Entorno Personal (Desarrollo y Hábitos)

**1. Diario Personal de Fricción Cero (Integración con Obsidian)**
*   **El Problema:** Quieres llevar un diario, pero abrir la app y formatear da pereza.
*   **La Solución:** Hablas con tu IA.
*   **El Prompt:** *"Guarda en mi diario de hoy: Fui a correr 5km y me sentí genial. Categoría: 'Salud'."*
*   **Impacto:** Debido a que el MCP inyecta metadatos YAML (`category: Salud`, `date: ...`), si tienes la carpeta `/notes` configurada como tu Bóveda de Obsidian, verás un gráfico perfecto de tus hábitos de salud.

**2. El "Buscador de Ideas" Perdidas**
*   **El Problema:** Sabes que tuviste una idea de negocio, pero no recuerdas dónde ni cuándo la anotaste.
*   **La Solución:** Usar la herramienta de búsqueda semántica del MCP.
*   **El Prompt:** *"Busca en mis notas dónde mencioné algo sobre 'comprar servidores locales'."*
*   **Impacto:** El MCP escaneará recursivamente tus archivos usando la herramienta `search_notes` y le devolverá a la IA los resultados exactos para que te responda.

---

## ✨ Funcionalidades Principales

| Herramienta | Acción | Ventaja Profesional |
| :--- | :--- | :--- |
| `create_note` | Crea nota con YAML | Soporte nativo para Obsidian/Notion. |
| `search_notes` | Búsqueda global | Ahorra tokens, no lee archivos innecesarios. |
| `list_by_category`| Filtrado por YAML | Permite separar "Personal" de "Trabajo". |
| `read_note` | Lee una nota completa | Recupera contexto histórico. |
| `append_to_note` | Añade sin borrar | Ideal para bitácoras y diarios que crecen. |
| `extract_pending_tasks` | Rastreador global | Busca checkboxes `- [ ]` sin marcar en todo tu sistema. |
| `get_recent_notes` | Resumen Ejecutivo | Filtra notas de los últimos X días. |

## 🚀 Instalación y Configuración

### 1. Requisitos
- Python 3.10 o superior.
- Instalación del SDK de MCP:
  ```bash
  pip install mcp
  ```

### 2. Configuración en Gemini CLI (Recomendado)
Para usar este MCP directamente en tu terminal con Gemini CLI, tienes dos opciones:

**Opción A: Inyección Directa (La más segura)**
Abre tu archivo `~/.gemini/settings.json` y añade este bloque dentro de `"mcpServers"`:
```json
{
  "mcpServers": {
    "daily-notes-pro": {
      "command": "python",
      "args": ["C:/Ruta/Absoluta/A/Tu/Repositorio/src/daily_notes/server.py"],
      "trust": true
    }
  }
}
```
*Nota: Reemplaza la ruta por donde clonaste este repositorio. Reinicia tu sesión de Gemini CLI para aplicar los cambios.*

**Opción B: Vía Comando**
Dentro de una sesión interactiva de Gemini CLI:
```bash
!gemini mcp add daily-notes-pro python "C:/Ruta/Absoluta/A/Tu/Repositorio/src/daily_notes/server.py" --trust
```

### 3. Configuración en Cursor IDE / Claude Desktop
Añade la siguiente configuración a tu `mcp.json`. Asegúrate de ajustar la ruta al archivo `server.py`:

```json
{
  "mcpServers": {
    "daily-notes": {
      "command": "python",
      "args": ["C:/Ruta/Absoluta/A/Tu/Repositorio/src/daily_notes/server.py"]
    }
  }
}
```

## 🧠 ¿Cómo entrenar a tu IA? (Prompting Avanzado)
Hemos incluido un archivo `mcp_prompts.json` en la raíz del proyecto. Si estás construyendo agentes (como con LangChain o OpenClaw), puedes pasar este JSON como "System Prompt" para que la IA entienda automáticamente las reglas de oro de categorización y los flujos de trabajo de este MCP.

## 🛠️ Estructura del Proyecto (SRC Layout)

```text
mcp-daily-notes/
├── src/
│   └── daily_notes/
│       └── server.py           # 🧠 El corazón del servidor MCP
├── tests/                      # 🧪 Pruebas unitarias
├── notes/                      # 📂 Aquí viven tus archivos .md (tu Segundo Cerebro)
├── pyproject.toml              # 📦 Dependencias y metadatos
├── mcp_prompts.json            # 🤖 Instrucciones máquina para Agentes IA
└── PROMPT_INSTRUCTIONS.md      # 🤖 Guía rápida para humanos
```

## 🤝 Contribuciones

¿Tienes una idea para mejorar este MCP? ¡Los Pull Requests son bienvenidos! Revisa [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo, modificarlo y compartirlo.

---
**Desarrollado por Luis Lopez** | [GitHub](https://github.com/llopez2018) | Suite de MCPs Comunitarios.