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

TOKEN = "8884093302:AAElljc_78tuB44lOcjXnGw7S6-F6Q_fHTc"

API_KEY = "AQ.Ab8RN6IaqUYerSRvwAwdAmBQkmU9hizzN4-Rh-L3CNc1QzHklQ"


#==================================
# GEMINI
#==================================

client = genai.Client(
    api_key=API_KEY
)


def preguntar_a_gemini(texto):

    respuesta = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=f"""
Eres una IA experta en:

- Roblox Studio
- Lua
- Python
- Diseño de videojuegos
- Interfaces gráficas
- Sistemas de guardado
- Plugins de Roblox Studio
- Optimización de juegos
- Y no debes contestar en frases muy largas sino de forma casual
Tu principal trabajo es ayudar al usuario a crear proyectos completos de Roblox Studio.

REGLAS:

1. Si el usuario hace una pregunta normal, respóndela normalmente.

2. Si el usuario pide crear algo para Roblox Studio, explica detalladamente cómo debería ser.

3. Si el usuario pide crear un juego, analiza:
- mapas
- scripts
- GUIs
- habilidades
- sonidos
- animaciones
- NPCs
- DataStores
- Leaderstats
- efectos visuales

4. Piensa siempre como un desarrollador profesional de Roblox Studio.


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