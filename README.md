# Diseño y optimización de una base de datos NoSQL

En un entorno de fintech, es crucial gestionar grandes volúmenes de datos de manera eficiente. Tu misión es diseñar una base de datos NoSQL que permita almacenar y extraer información de manera óptima. La base de datos debe soportar operaciones de lectura y escritura a alta velocidad, manejar grandes cantidades de datos y ofrecer flexibilidad en el esquema.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | Creación de bases de datos NoSQL |
| **Nivel** | advanced-l3 |
| **Tipo** | practical |
| **Tiempo estimado** | 4-6 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Diseño del esquema de la base de datos

**Objetivo:** Definir el esquema de la base de datos NoSQL que cumpla con los requisitos del negocio.

**Tiempo estimado:** 1 hora

**Instrucciones:**

- Identifica las entidades y relaciones clave que deben almacenarse en la base de datos.
- Define las claves partición y secundarias necesarias para optimizar las consultas.
- Considera la flexibilidad del esquema y cómo afectará a las operaciones de lectura y escritura.

**Entregable:** Descripción del esquema de la base de datos NoSQL.

<details>
<summary>Pistas de conocimiento</summary>

- Piensa en cómo las claves partición influyen en la distribución de los datos.
- Recuerda que la flexibilidad del esquema puede tener un impacto en el rendimiento.

</details>

### Fase 2: Implementación de operaciones básicas

**Objetivo:** Implementar operaciones de lectura y escritura en la base de datos NoSQL.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Crea las operaciones necesarias para insertar, actualizar y eliminar datos en la base de datos.
- Implementa consultas para extraer información de la base de datos utilizando las claves partición y secundarias definidas.
- Considera la consistencia y el rendimiento de las operaciones.

**Entregable:** Operaciones básicas de lectura y escritura implementadas.

<details>
<summary>Pistas de conocimiento</summary>

- Recuerda que la consistencia y el rendimiento son críticos en una base de datos NoSQL.
- Piensa en cómo las consultas pueden aprovechar las claves partición para optimizar el rendimiento.

</details>

### Fase 3: Optimización y escalabilidad

**Objetivo:** Optimizar el rendimiento y asegurar la escalabilidad de la base de datos NoSQL.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identifica posibles puntos de cuello de botella en el rendimiento de la base de datos.
- Implementa estrategias de optimización para mejorar el rendimiento de las operaciones.
- Considera la escalabilidad de la base de datos y cómo manejar grandes volúmenes de datos.
- Evalúa el impacto de las decisiones tomadas en las fases anteriores en la optimización y escalabilidad.

**Entregable:** Estrategias de optimización y escalabilidad implementadas.

<details>
<summary>Pistas de conocimiento</summary>

- Recuerda que la optimización del rendimiento puede requerir trade-offs en la consistencia o la flexibilidad del esquema.
- Piensa en cómo la escalabilidad afectará a las operaciones de lectura y escritura.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una clave partición en una base de datos NoSQL y por qué es importante?
- **paraQueSirve**: ¿Para qué sirve definir claves secundarias en una base de datos NoSQL?
- **comoSeUsa**: ¿Cómo se pueden aprovechar las claves partición para optimizar las consultas en una base de datos NoSQL?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar operaciones de lectura y escritura en una base de datos NoSQL?
- **queDecisionesImplica**: ¿Qué decisiones implica la optimización del rendimiento y la escalabilidad de una base de datos NoSQL?

## Criterios de Evaluacion

- Definir un esquema de base de datos NoSQL que cumpla con los requisitos del negocio.
- Implementar operaciones básicas de lectura y escritura en la base de datos NoSQL.
- Optimizar el rendimiento y asegurar la escalabilidad de la base de datos NoSQL.

## Como trabajar con un asistente de IA

- **AGENTS.md** — instrucciones nativas del repo (Cursor, Codex, Copilot, Gemini, Claude Code). Abrí el proyecto y el agente las carga solo.
- **PROMPT_MEJORA.md** — el mismo prompt, para copiar y pegar en un chat (claude.ai, ChatGPT, etc.).

---

*Reto generado automaticamente por Challenge Generator - Pragma*
