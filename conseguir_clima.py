import os
from dotenv import load_dotenv

load_dotenv()

# Componentes modulares del proyecto
from model import model
from utils import format_content

from skycast_google import Weather
from langchain.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

API_KEY = os.getenv("API_KEY_GOOGLE_CLIMA")
if not API_KEY:
    raise ValueError("⚠️ No se encontró API_KEY_GOOGLE_CLIMA en el .env")

weather = Weather(api_key=API_KEY)


@tool
def get_weather(city: str, days: int = 1) -> str:
    """
    Obtiene el pronóstico del clima real para una ciudad. 
    Útil para responder preguntas sobre el clima actual o el pronóstico de los próximos días.
    """
    try:
        return weather.request_forecast_text(city=city, days=days)
    except Exception as e:
        return f"Ocurrió un error al consultar el clima: {str(e)}"


tools = [get_weather]
checkpointer = MemorySaver()

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=(
        "Eres un meteorólogo experto y un asistente útil. "
        "Usa la herramienta disponible para responder a las preguntas sobre el clima con precisión."
    ),
    checkpointer=checkpointer,
)


def main():
    print("=== Chatbot Meteorológico ===")
    print("Escribe tu consulta o 'salir' para terminar.\n")
    
    config = {"configurable": {"thread_id": "session-weather-1"}}

    while True:
        try:
            user_input = input("Tú: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ("salir", "exit", "quit"):
                print("\n¡Hasta luego!")
                break

            response = agent.invoke(
                {"messages": [{"role": "user", "content": user_input}]},
                config=config,
            )
            
            last_message = response["messages"][-1]
            answer = format_content(last_message)
            print(f"\nAgente: {answer}\n")
        except (KeyboardInterrupt, EOFError):
            print("\n¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
