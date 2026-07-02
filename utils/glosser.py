from groq import Groq
from config import GROQ_API_KEY

def gloss_text(text):
    client = Groq(api_key=GROQ_API_KEY)
    response = client.chat.completions.create(model="llama-3.1-8b-instant", messages=[
        {"role": "system", "content": "You are an ISL (Indian Sign Language) gloss converter. Convert English text to ISL gloss format by following these rules:* No articles (a, an, the)* No is/am/are* Verbs in base form* UPPERCASE words* Topic first.Output only the gloss, nothing else."},
        {"role": "user", "content": f"Provide a gloss for this: {text}"}
    ])
    return response.choices[0].message.content