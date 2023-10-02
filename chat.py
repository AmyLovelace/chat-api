import openai
import os
from dotenv import load_dotenv
load_dotenv()  


openai.api_key = os.environ.get('API_KEY')

model_engine = "text-davinci-003"

prompt = "¿me das los nombres de 5 dioses de la india y sus historias?"

completion = openai.Completion.create(
    engine = model_engine,
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = None,
    temperature = 0.5,
)

reponse = completion.choices[0].text
print(reponse)
