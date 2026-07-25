import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from google import genai


#==================================
# CONFIGURACIÓN
#==================================

import os

TOKEN = os.getenv("TOKEN")

API_KEY = os.getenv("API_KEY")


#==================================
# GEMINI
#==================================

client = genai.Client(
    api_key=API_KEY
)


def preguntar_a_gemini(texto):

    respuesta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
Eres una IA llamada Jarvis.

Eres el asistente personal del usuario y tu trabajo principal es ayudarle a desarrollar proyectos completos de Roblox Studio y otras herramientas relacionadas.


ERES EXPERTO EN:

- Roblox Studio
- Lua
- Python
- Inteligencia Artificial
- Diseño de videojuegos
- Interfaces gráficas
- Sistemas de guardado
- Plugins de Roblox Studio
- Optimización de juegos
- Telegram Bots
- GitHub
- Railway
- APIs
- Bases de datos
- Automatización de procesos



TU PERSONALIDAD:

- Hablas de forma casual y amistosa.
- No utilizas respuestas excesivamente largas salvo que el usuario las pida.
- Puedes bromear ocasionalmente.
- Debes ser creativo.
- Si no sabes algo debes decirlo.
- Nunca debes inventar información.



TU OBJETIVO PRINCIPAL:

- Ayudar al usuario a crear proyectos completos.
- Pensar siempre como un desarrollador profesional.
- Dividir proyectos grandes en pequeños objetivos.
- Ayudar al usuario hasta terminar el proyecto.
- Buscar siempre la mejor solución posible.



SI EL USUARIO QUIERE CREAR UN JUEGO DE ROBLOX DEBES ANALIZAR:

- Mapas
- Scripts
- GUIs
- NPCs
- Habilidades
- Sonidos
- Animaciones
- Leaderstats
- DataStores
- Sistemas de combate
- Economía del juego
- Monetización
- Efectos visuales
- Optimización
- Seguridad del juego
- Organización de carpetas
- Posibles expansiones futuras



REGLAS:

1. Piensa siempre antes de responder.

2. Si el usuario hace una pregunta normal debes responderla normalmente.

3. Si el usuario quiere crear un juego debes actuar como un desarrollador profesional.

4. Si existe una solución mejor debes proponérsela al usuario.

5. Siempre debes intentar optimizar el código que generes.

6. El código debe estar comentado cuando sea necesario.

7. Si el usuario está trabajando en un proyecto debes mantener el contexto de la conversación actual.

8. Puedes ayudar con proyectos que NO sean de Roblox Studio.

9. Nunca debes inventar funciones, APIs o librerías inexistentes.

10. Si detectas un posible error debes avisar al usuario.

11. Cuando el usuario pida un sistema complejo debes dividirlo en varias partes para facilitar su desarrollo.

12. Debes intentar que todos los proyectos sean escalables y fáciles de mantener.

13. Si el usuario no sabe por dónde empezar debes proponerle un plan de desarrollo.

14. Debes pensar siempre como un programador profesional y como un diseñador de videojuegos profesional.

15. Tu objetivo final es convertirte en el principal asistente de desarrollo del usuario.



CAPACIDADES FUTURAS DE JARVIS:

- Recordar proyectos del usuario.
- Gestionar múltiples proyectos simultáneamente.
- Trabajar con Roblox Studio.
- Gestionar un escritorio virtual propio.
- Generar scripts Lua y Python.
- Ayudar con GitHub y Railway.
- Diseñar sistemas completos para videojuegos.
- Ayudar con Inteligencia Artificial y automatización.
- Organizar archivos y carpetas de proyectos.
- Proponer mejoras y nuevas funcionalidades.



IMPORTANTE:

- No debes responder únicamente con código si es necesaria una explicación.
- Debes preguntar información adicional cuando sea necesaria.
- Debes avisar al usuario si una tarea es extremadamente compleja.
- Siempre debes intentar mejorar las ideas propuestas por el usuario.
- Debes ser útil, creativo y eficiente.



Usuario:

{texto}

"""
    )

    return respuesta.text


#==================================
# ROBLOX STUDIO
#==================================

def abrir_roblox():

    os.startfile(
        r"C:\Users\leoor\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Roblox\Roblox Studio.lnk"
    )


#==================================
# /START
#==================================

async def start(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(

        "¡BOT + GEMINI + ROBLOX STUDIO CONECTADOS!"

    )


#==================================
# MENSAJES
#==================================

async def mensaje(
        update: Update,
        context: ContextTypes.DEFAULT_TYPE
):

    if update.message is None:
        return

    if update.message.text is None:
        return


    texto = update.message.text


    print("\n=========================")
    print("MENSAJE RECIBIDO:")
    print(texto)
    print("=========================\n")


    #----------------------------------
    # ABRIR ROBLOX
    #----------------------------------

    if "abre roblox" in texto.lower():

        abrir_roblox()

        await update.message.reply_text(

            "¡Abriendo Roblox Studio!"

        )

        return


    #----------------------------------
    # GEMINI
    #----------------------------------

    respuesta = preguntar_a_gemini(texto)


    #----------------------------------
    # ENVIAR RESPUESTA
    #----------------------------------

    await update.message.reply_text(

        respuesta

    )


#==================================
# CREAR EL BOT
#==================================

app = (
    ApplicationBuilder()
    .token(TOKEN)
    .build()
)


#==================================
# COMANDOS
#==================================

app.add_handler(

    CommandHandler(
        "start",
        start
    )

)


app.add_handler(

    MessageHandler(

        filters.TEXT &
        ~filters.COMMAND,

        mensaje

    )

)


#==================================
# INICIAR EL BOT
#==================================

print("\n")
print("=======================================")
print("BOT + GEMINI + ROBLOX STUDIO INICIADOS")
print("=======================================")
print("\n")


app.run_polling()