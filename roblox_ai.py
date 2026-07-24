from google import genai
import json


#--------------------------------------


API_KEY = "AQ.Ab8RN6IaqUYerSRvwAwdAmBQkmU9hizzN4-Rh-L3CNc1QzHklQ"


client = genai.Client(
    api_key=API_KEY
)


#--------------------------------------


def ask_gemini(message):

    response = client.models.generate_content(

        model="gemini-3.6-flash",

        contents=message

    )

    return response.text


#--------------------------------------


def analyze_project(message):


    prompt = f"""

Eres una IA experta en Roblox Studio.

Analiza el siguiente proyecto:

{message}


Devuelve SOLAMENTE un JSON.


Ejemplo:


{{
"name":"Tycoon",

"difficulty":"7/10",

"time":"35 minutos",

"scripts":"150",

"guis":"50",

"npcs":"20",

"animations":"30",

"description":"Juego Tycoon futurista."

}}


NO expliques nada.

NO escribas texto adicional.

SOLO el JSON.

"""


    response = client.models.generate_content(

        model="gemini-3.6-flash",

        contents=prompt

    )


    return response.text


#--------------------------------------


def convert_json(text):


    text = text.replace(

        "```json",

        ""

    )


    text = text.replace(

        "```",

        ""

    )


    text = text.strip()


    try:

        return json.loads(text)


    except:

        return None