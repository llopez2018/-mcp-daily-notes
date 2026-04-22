# 📓 Daily Notes Pro: The AI-First Knowledge Infrastructure
## [English](#english) | [Español](#español)

---

<a name="english"></a>
## 🇺🇸 English: Professional Knowledge Management for AI Agents

**Daily Notes Pro** is a high-performance Model Context Protocol (MCP) server designed to transform your local directory into a structured **Second Brain**. It provides your AI (Cursor, Claude, Gemini) with a secure, machine-readable infrastructure to manage your life and work.

### 🏛️ Project Architecture
```text
mcp-daily-notes/
├── docs/                   # 🧠 Intelligence & Methodology
│   ├── agents/             # Specialized AI Personas (GTD, PARA, SCAMPER)
│   └── prompt_guide.md     # How to master AI interaction
├── src/                    # ⚙️ Core Logic (Senior Python)
│   └── daily_notes/        # Safe, high-performance Server
├── tests/                  # 🧪 Robustness Suite (Pytest & Hypothesis)
├── notes/                  # 📂 Your Vault (The data lives here)
├── examples/               # 💡 Sample professional notes
├── mcp_prompts.json        # 🤖 Machine-readable AI instructions
├── pyproject.toml          # 📦 Modern Python packaging
└── README.md               # 📖 The Gateway
```

### 🎯 Professional & Personal Use Cases

**1. The Meeting Assistant (Professional Integration)**
- **Problem:** Scattered notes from Zoom/Teams meetings.
- **Solution:** Dictate key points to the AI.
- **Prompt:** *"Create a meeting note for today's 'Naves Industriales' sync. Category: 'Meeting'. Record all the agreements."*
- **Impact:** The MCP generates a YAML-ready file. If you use **Obsidian** or **Notion**, the note appears automatically in your workplace vault.

**2. Zero-Friction Personal Journal (Habit Tracking)**
- **Problem:** Opening an app and formatting is a barrier to journaling.
- **Solution:** Talk to your AI via Claude Desktop or Gemini CLI.
- **Prompt:** *"Record in today's journal: I ran 5km and felt great. Category: 'Health'."*
- **Impact:** Because of the YAML metadata (`category: Health`), your Obsidian graph will automatically track your health habits.

**3. The "Lost Idea" Searcher (Semantic Retrieval)**
- **Problem:** You remember having a business idea but can't find where you wrote it.
- **Solution:** Use the global search tool.
- **Prompt:** *"Search all my notes for 'local server buy' or 'hardware ideas'."*
- **Impact:** The MCP scans all files locally and returns the exact matches, saving tokens and time.

### 🚀 Key Features
- **Semantic Path Jail**: Military-grade path validation prevents directory traversal.
- **YAML Metadata**: Automatic injection for 100% compatibility with Obsidian/Notion.
- **Divergent Tools**: Global task extraction (`- [ ]`), weekly summaries, and serendipity engines.

### 🛠️ Integration (Gemini CLI / Cursor / Claude)
Add this to your `settings.json` or `mcp.json`:
```json
{
  "mcpServers": {
    "daily-notes-pro": {
      "command": "python",
      "args": ["C:/YOUR_PATH/src/daily_notes/server.py"],
      "trust": true
    }
  }
}
```

---

<a name="español"></a>
## 🇲🇽 Español: Infraestructura de Conocimiento "AI-First"

**Daily Notes Pro** es un servidor MCP de alto rendimiento diseñado para transformar tu directorio local en un **Segundo Cerebro** estructurado. Le da a tu IA (Cursor, Claude, Gemini) una infraestructura segura y legible por máquinas para gestionar tu vida y trabajo.

### 🏛️ Arquitectura del Proyecto
*(Ver mapa visual en la sección English arriba)*

### 🎯 Casos de Uso Profesionales y Personales

**1. El Asistente de Reuniones (Integración Profesional)**
- **El Problema:** Notas dispersas tras reuniones de Zoom o Teams.
- **La Solución:** Dictarle a la IA los puntos clave.
- **El Prompt:** *"Crea una nota de la reunión de hoy de 'Naves Industriales'. Categoría: 'Reunión'. Guarda todos los acuerdos."*
- **Impacto:** El MCP genera un archivo listo con YAML. Si usas **Obsidian** o **Notion**, la nota aparece automáticamente en tu carpeta de trabajo.

**2. Diario Personal de Fricción Cero (Seguimiento de Hábitos)**
- **El Problema:** Abrir una app y formatear es una barrera para escribir un diario.
- **La Solución:** Hablar con tu IA por Claude Desktop o Gemini CLI.
- **El Prompt:** *"Guarda en mi diario de hoy: Corrí 5km y me sentí genial. Categoría: 'Salud'."*
- **Impacto:** Gracias a los metadatos YAML (`category: Salud`), tu gráfico de Obsidian rastreará tus hábitos de salud automáticamente.

**3. El Buscador de Ideas Perdidas (Recuperación Semántica)**
- **El Problema:** Recuerdas haber tenido una idea de negocio pero no dónde la anotaste.
- **La Solución:** Usar la herramienta de búsqueda global del MCP.
- **El Prompt:** *"Busca en todas mis notas 'comprar servidores locales' o 'ideas de hardware'."*
- **Impacto:** El MCP escanea todos los archivos localmente y devuelve las coincidencias exactas, ahorrando tiempo y tokens.

### 🚀 Funcionalidades Clave
- **Cárcel de Rutas Semántica**: Validación de rutas que previene hackeos del sistema de archivos.
- **Metadatos YAML**: Inyección automática para compatibilidad con Obsidian y Notion.
- **Herramientas Divergentes**: Extracción global de tareas (`- [ ]`), resúmenes semanales y motores de serendipia.

### 🤖 Ecosistema de Agentes (docs/agents)
No solo son herramientas, es un **equipo virtual**:
- **Archivist**: Experto en metodologías PARA y Zettelkasten.
- **Task Master**: Implementación de GTD (Getting Things Done).
- **Creative Muse**: Inspiración basada en SCAMPER y Primeros Principios.
- **Reviewer**: Analista de rendimiento y retrospectivas.

---
**Developed by Luis Lopez** | [GitHub](https://github.com/llopez2018) | **MCP Community Suite**
