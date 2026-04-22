# 🤖 AI Prompt Guide / Guía de Prompts para la IA
## [English](#english) | [Español](#español)

---

<a name="english"></a>
## 🇺🇸 English: Mastering Interaction

To get the best out of Daily Notes Pro, your AI assistant should follow these core principles. You can paste this into your System Prompt.

### 🛠️ Usage Rules
1. **Think Before Writing**: Always check if a note already exists using `search_notes` before creating a new one.
2. **Standardized Metadata**: Always use categories like `Work`, `Personal`, `Idea`, `Finance`, `Health`.
3. **Atomic Context**: Create notes for single, discrete ideas to make them easier to find later.

### 💡 Example Interaction
**User:** "Remind me to call Luis tomorrow about the project."
**AI:** (Calls `create_note(title="Call Luis", content="- [ ] Call Luis about project status.", category="Work")`)

---

<a name="español"></a>
## 🇲🇽 Español: Dominando la Interacción

Para obtener lo mejor de Daily Notes Pro, tu asistente de IA debe seguir estos principios fundamentales. Puedes pegar esto en tu System Prompt.

### 🛠️ Reglas de Uso
1. **Piensa antes de escribir**: Siempre verifica si una nota ya existe usando `search_notes` antes de crear una nueva.
2. **Metadatos Estandarizados**: Usa siempre categorías como `Trabajo`, `Personal`, `Idea`, `Finanzas`, `Salud`.
3. **Contexto Atómico**: Crea notas para ideas únicas y discretas para que sean más fáciles de encontrar después.

### 💡 Ejemplo de Interacción
**Usuario:** "Recuérdame llamar a Luis mañana sobre el proyecto."
**IA:** (Llama a `create_note(title="Llamar a Luis", content="- [ ] Llamar a Luis sobre estatus del proyecto.", category="Trabajo")`)
