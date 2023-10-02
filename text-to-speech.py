import requests
import json
import os
from dotenv import load_dotenv

def apiTextToSpeech():
    load_dotenv()

    url = "https://ttsmp3.com/makemp3_new.php"
    API_KEY = os.getenv("RAPIDAPI_KEY")

    data = {
        'msg': 'el diego el mas grande gato, el gran barrilete cosmico',
        'lang': 'Mia',
        'source': 'ttsmp3',
        'audioFormat': 'mp3',
        'tasktype': 'direct',
    }

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': "text-to-speech-for-28-languages.p.rapidapi.com"
    }

    response = requests.post(url, data=data, headers=headers)

    print(response.json())
    
apiTextToSpeech()