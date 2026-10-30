from google.adk.runners import Runner
from agent.cerebro import root_agent
from agent.memory import sesion_servicio

engine = Runner(
    agent=root_agent,
    app_name="mi_agente",
    session_service=sesion_servicio,
)
