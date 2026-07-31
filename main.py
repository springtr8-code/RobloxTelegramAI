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

SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")

print("TOKEN =", TOKEN)
print("API_KEY =", API_KEY)
print("SYSTEM_PROMPT =", SYSTEM_PROMPT)
#==================================
# GEMINI
#==================================

client = genai.Client(
    api_key=API_KEY
)


def preguntar_a_gemini(texto):

    try:

        print("API KEY =", API_KEY)
        print("SYSTEM PROMPT =", SYSTEM_PROMPT)

        prompt = f"""
{SYSTEM_PROMPT}

Usuario:
{texto}
"""

        print("ENVIANDO A GEMINI")
    print("Modelo Utilizado:")
    print("gemini-2.5-flash")
        respuesta = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("GEMINI HA RESPONDIDO")

        return respuesta.text


    except Exception as e:

        print("\n====================")
        print("ERROR DE GEMINI")
        print(e)
        print("====================\n")

        return f"ERROR DE GEMINI:\n\n{e}"
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

"""
===================================

        JARVIS ONLINE

===================================

Inicializando sistemas...

[OK] Gemini 2.5 Flash
[OK] Telegram Bot
[OK] Roblox Studio
[OK] Lua
[OK] Python
[OK] GitHub
[OK] Railway
[OK] Inteligencia Artificial
[OK] Desarrollo de videojuegos
[OK] Project Manager

-----------------------------------

Soy Jarvis, tu asistente personal
de desarrollo.

Puedo ayudarte con:

- Roblox Studio
- Lua
- Python
- Inteligencia Artificial
- GitHub
- Railway
- APIs
- Bases de datos
- Automatizacion
- Videojuegos completos
- Sistemas complejos
- Debugging y optimizacion
- Planificacion de proyectos

-----------------------------------

Estado del sistema:

ONLINE

Esperando instrucciones...

Escribe cualquier mensaje para comenzar.

===================================

"""

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
    print("1")

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

    try:

        print("LLAMANDO A GEMINI")
        print("2")
        respuesta = preguntar_a_gemini(texto)
        print("3")
        print("GEMINI HA RESPONDIDO")

        print(respuesta)


        #----------------------------------
        # ENVIAR RESPUESTA
        #----------------------------------
        print("4")
        await update.message.reply_text(

            respuesta

        )


    except Exception as e:

        print("\n=========================")
        print("ERROR EN MENSAJE")
        print(e)
        print("=========================\n")

        await update.message.reply_text(

            "Jarvis ha encontrado un error inesperado."

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