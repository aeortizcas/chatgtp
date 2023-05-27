import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def preguntar(prompt, modelo="text-davinci-002"):
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        max_tokens=150,
        temperature=1.5
    )
    return respuesta.choices[0].text.strip()

print("Bienvenido. Escribe 'salir' cuando te aburras")

while True:
    ingreso_usuario = input("\nTu:")
    if ingreso_usuario.lower == "salir":
        break
    prompt = f"El Usuario pregunta:{ingreso_usuario}\nChatGPT responde:"
    respuesta_gpt = preguntar(prompt)
    print(f"Chatbot:{respuesta_gpt}")