import os
from google.adk.models import Gemini
from google.adk.models.lite_llm import LiteLlm

def obtener_modelo(proveedor: str = "groq"):
    if proveedor == "groq":
        if not os.getenv("GROQ_API_KEY"):
            raise ValueError("❌ Falta GROQ_API_KEY en el .env")
        # El prefijo "groq/" le dice a LiteLLM a dónde enviar la petición
        return LiteLlm(model="groq/openai/gpt-oss-20b")
    
    else:
        if not os.getenv("GOOGLE_API_KEY"):
            raise ValueError("❌ Falta GOOGLE_API_KEY en el .env")
        return Gemini(model="gemini-2.5-flash")