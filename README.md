# 📓 MCP Daily Notes: Tu Cerebro Externo en Markdown

[![MCP Protocol](https://img.shields.io/badge/MCP-Standard-blue.svg)](https://modelcontextprotocol.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-brightgreen.svg)](https://www.python.org/)

**MCP Daily Notes** es un servidor para el Model Context Protocol que permite a cualquier IA (Cursor, Claude Desktop, OpenClaw) gestionar tu conocimiento personal, diario y notas directamente en archivos Markdown locales.

> "No más 'se me olvidó'. Ahora tu IA tiene memoria persistente en tu propio disco duro."

---

## 🌟 ¿Por qué usar este MCP?

A diferencia de las memorias volátiles de los chats, este servidor le da a tu IA:
1. **Persistencia Real**: Todo se guarda en archivos `.md` estándar que puedes abrir con Obsidian, VS Code o Notepad.
2. **Privacidad Total**: Tus notas nunca salen de tu máquina. La IA solo accede a ellas cuando tú lo autorizas mediante el protocolo MCP.
3. **Organización Automática**: Deja que la IA estructure tus pensamientos, añada fechas y organice tus listas de ideas.

## ✨ Funcionalidades Principales

| Herramienta | Acción | Caso de Uso |
| :--- | :--- | :--- |
| `create_note` | Crea una nota nueva | "Guarda esta idea para un nuevo video..." |
| `list_notes` | Lista tus notas | "¿De qué temas hemos estado hablando?" |
| `read_note` | Lee una nota completa | "Recuérdame qué escribí sobre el proyecto X." |
| `append_to_note` | Añade sin borrar | "Añade este nuevo gasto a mi lista de hoy." |

## 🚀 Instalación y Configuración

### 1. Requisitos
- Python 3.10 o superior.
- Instalación del SDK de MCP:
  ```bash
  pip install mcp
  ```

### 2. Configuración en tu Cliente IA (mcp.json)

Añade la siguiente configuración. **Asegúrate de ajustar la ruta al archivo `server.py`**:

```json
{
  "mcpServers": {
    "daily-notes": {
      "command": "python",
      "args": ["C:/Users/llopez/Documents/experimentos/mcp-community-suite/mcp-daily-notes/server.py"]
    }
  }
}
```

## 🤖 Ejemplos de Prompts para usar con la IA

- *"Crea una nota llamada 'Diario 22-04' y resume lo que hicimos hoy."*
- *"¿Tengo alguna nota donde hable sobre mis metas de ahorro?"*
- *"Añade 'Comprar leche' a mi nota de 'Pendientes Semanales'."*

## 🛠️ Estructura del Proyecto

```text
mcp-daily-notes/
├── notes/              # 📂 Aquí viven tus archivos .md
├── server.py           # 🧠 El corazón del servidor MCP
├── requirements.txt    # 📦 Dependencias
└── PROMPT_INSTRUCTIONS.md # 🤖 Guía para que la IA sea más lista
```

## 🤝 Contribuciones

¿Tienes una idea para mejorar este MCP? ¡Los Pull Requests son bienvenidos! Revisa [CONTRIBUTING.md](CONTRIBUTING.md).

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Siéntete libre de usarlo, modificarlo y compartirlo.

---
**Desarrollado por Luis Lopez** | [GitHub](https://github.com/tu-usuario) | Suite de MCPs Comunitarios.
