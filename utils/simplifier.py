from groq import Groq
from config import GROQ_API_KEY



def simplify_text(text):
    client = Groq(api_key=GROQ_API_KEY)
    response =client.chat.completions.create(model="llama-3.1-8b-instant",messages=[
    {"role": "system", "content": "You are an ISL interpreter. Simplify English text to basic words only. Keep original meaning. No extra words. No added context. Remove filler words. Keep nouns, verbs, key adjectives only.Output simple English only, nothing else."},
    {"role": "user", "content": f"Simplify this: {text}"}
])
    return response.choices[0].message.content  