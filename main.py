import asyncio
from dotenv import load_dotenv
load_dotenv()

from google.genai import types
from agent.motor import engine
from agent.memory import sesion_servicio

async def main():
    app_name = "mi_agente"
    user_id = "u1"
    session_id = "sesion_chat_1"

    await sesion_servicio.create_session(
        app_name=app_name, user_id=user_id, session_id=session_id
    )

    print("🤖 Agente listo. Escribe 'salir' para terminar.\n")

    while True:
        texto_usuario = input("Tú: ")

        if texto_usuario.lower() in ["salir", "exit", "quit"]:
            print("👋 ¡Hasta luego!")
            break

        if not texto_usuario.strip():
            continue

        mensaje = types.Content(
            role="user", 
            parts=[types.Part(text=texto_usuario)]
        )

        print("🤖 Agente: ", end="", flush=True)

        respuesta_impresa = False
        
        # Consumimos el stream de eventos
        async for evento in engine.run_async(
            user_id=user_id, 
            session_id=session_id, 
            new_message=mensaje
        ):
            # Solo imprimimos el primer evento final que tenga texto
            if not respuesta_impresa and evento.is_final_response() and evento.content and evento.content.parts:
                texto = evento.content.parts[0].text
                if texto: # Verificamos que no esté vacío
                    print(texto)
                    respuesta_impresa = True
                    break # Detenemos el bucle de eventos inmediatamente

        print() # Salto de línea

if __name__ == "__main__":
    asyncio.run(main())