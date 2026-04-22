# 📓 Daily Notes Pro: The AI-First Knowledge Infrastructure
## [English](#english) | [Español](#español)

---

<a name="english"></a>
## 🇺🇸 English: Professional Knowledge Management for AI Agents

**Daily Notes Pro** is a "Next Level" Model Context Protocol (MCP) server. It transforms your local directory into a structured, machine-readable **Second Brain**. It's not just about storing text; it's about providing your AI (Cursor, Claude, Gemini) with a secure, high-performance infrastructure to manage your life and work.

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

### 🚀 Key Features
- **Semantic Path Jail**: Military-grade path validation prevents any directory traversal.
- **YAML Infrastructure**: Automatic metadata injection for 100% compatibility with Obsidian/Notion.
- **Divergent Tools**: Global task extraction, weekly time-machine summaries, and serendipity engines.
- **Bilingual Core**: Code documented for international collaboration.

### 🛠️ Quick Start
1. **Requirements**: Python 3.10+
2. **Setup**:
   ```bash
   pip install mcp
   ```
3. **Integration (Gemini CLI / Cursor / Claude)**:
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

**Daily Notes Pro** es un servidor MCP de "Siguiente Nivel". Transforma tu directorio local en un **Segundo Cerebro** estructurado y legible por máquinas. No se trata solo de guardar texto; se trata de darle a tu IA una infraestructura segura y de alto rendimiento para gestionar tu vida y trabajo.

### 🏛️ Arquitectura del Proyecto
*(Ver mapa visual en la sección English arriba)*

### 🚀 Funcionalidades Clave
- **Cárcel de Rutas Semántica**: Validación de rutas de grado militar que previene cualquier intento de hackeo del sistema de archivos.
- **Infraestructura YAML**: Inyección automática de metadatos para compatibilidad total con Obsidian y Notion.
- **Herramientas Divergentes**: Extracción global de tareas, resúmenes semanales (máquina del tiempo) y motores de serendipia creativa.
- **Núcleo Bilingüe**: Código diseñado para la colaboración internacional.

### 🤖 Ecosistema de Agentes (docs/agents)
No solo te damos herramientas, te damos el **equipo virtual** para usarlas:
- **Archivist**: Experto en metodologías PARA y Zettelkasten.
- **Task Master**: Implementación de GTD (Getting Things Done).
- **Creative Muse**: Inspiración basada en SCAMPER y Primeros Principios.
- **Reviewer**: Analista de rendimiento y retrospectivas semanales.

---
**Developed by Luis Lopez** | [GitHub](https://github.com/llopez2018) | **MCP Community Suite**
