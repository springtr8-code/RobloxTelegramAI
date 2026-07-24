from google import genai

API_KEY = "AQ.Ab8RN6IaqUYerSRvwAwdAmBQkmU9hizzN4-Rh-L3CNc1QzHklQ"

client = genai.Client(
    api_key=API_KEY
)

respuesta = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Di solamente HOLA."
)

print(respuesta.text)