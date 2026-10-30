from google.adk.agents import LlmAgent
from agent.tools.herramienta import obtener_clima
from agent.conexion_modelo import obtener_modelo

def strip_reasoning_content(callback_context, llm_request):
    """Filtra el contenido de razonamiento para que Groq no lo rechace."""
    for content in llm_request.contents:
        if content.parts:
            content.parts = [
                p for p in content.parts 
                if not (hasattr(p, "thought") and p.thought)
            ]
    return None

root_agent = LlmAgent(
    name = "asistente_clima",
    model = obtener_modelo(),
    instruction =(
        "Eres un asistente del clima. Usa 'obtener_clima' para responder. "
        "IMPORTANTE: Responde SIEMPRE en español, de forma directa y breve. "
        "NO muestres tu proceso de pensamiento, NO expliques lo que estás haciendo. "
        "Solo da la respuesta final al usuario."

    ),
    tools =[obtener_clima],
    before_model_callback=strip_reasoning_content,
)