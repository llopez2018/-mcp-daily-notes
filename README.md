# 📓 MCP Daily Notes Pro

[English](#english) | [Español](#español)

---

<a name="english"></a>
## 🇺🇸 English: Your AI Second Brain in Markdown

**MCP Daily Notes Pro** is a professional-grade server for the Model Context Protocol (MCP). It enables AI assistants (Cursor, Claude, Gemini CLI) to manage your knowledge, journals, and tasks directly in local Markdown files with YAML metadata.

### ✨ Key Features
- 📝 **Professional Metadata**: Automatic YAML Frontmatter injection (Obsidian & Notion compatible).
- 🔍 **Global Search**: Search terms across all notes in milliseconds.
- 📅 **Task Tracker**: Extract all pending `- [ ]` checkboxes into a single report.
- 🎲 **Serendipity Engine**: Surface random past ideas to break creative blocks.
- 🛡️ **Senior Security**: Path Jail (no directory traversal) and Payload limits.

### 🚀 Quick Setup
1. **Requirements**: Python 3.10+
2. **Install SDK**: `pip install mcp`
3. **Configure Client (mcp.json)**:
```json
{
  "mcpServers": {
    "daily-notes": {
      "command": "python",
      "args": ["C:/Path/To/src/daily_notes/server.py"]
    }
  }
}
```

---

<a name="español"></a>
## 🇲🇽 Español: Tu Segundo Cerebro de IA en Markdown

**MCP Daily Notes Pro** es un servidor de nivel profesional para el protocolo MCP. Permite que tus asistentes de IA gestionen tu conocimiento, diarios y tareas directamente en archivos Markdown locales con metadatos YAML.

### ✨ Funcionalidades Clave
- 📝 **Metadatos Profesionales**: Inyección automática de YAML Frontmatter (Compatible con Obsidian y Notion).
- 🔍 **Búsqueda Global**: Busca términos en todas tus notas en milisegundos.
- 📅 **Rastreador de Tareas**: Extrae todos los pendientes `- [ ]` en un solo reporte.
- 🎲 **Motor de Serendipia**: Recupera ideas al azar para romper bloqueos creativos.
- 🛡️ **Seguridad Senior**: Protección de rutas (Path Jail) y límites de carga.

### 🚀 Configuración Rápida
1. **Requisitos**: Python 3.10+
2. **Instalar SDK**: `pip install mcp`
3. **Configurar Cliente (mcp.json)**:
*(Ver ejemplo arriba en la sección English)*

---
**Developed by Luis Lopez** | [GitHub](https://github.com/llopez2018)
