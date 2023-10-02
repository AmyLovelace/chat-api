import http.client
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("RAPIDAPI_KEY")
conn = http.client.HTTPSConnection("text-to-speech-for-28-languages.p.rapidapi.com")

payload = "msg=el diego el mas grande gato, el gran barrilete cosmico"

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'X-RapidAPI-Key': API_KEY,
    'X-RapidAPI-Host': "text-to-speech-for-28-languages.p.rapidapi.com"
}

conn.request("POST", "/", payload, headers)

res = conn.getresponse()
data = res.read()
with open('audio.mp3', 'wb') as audio_file:
    audio_file.write(data)

print("Audio file downloaded successfully.")
print(data.decode("utf-8"))