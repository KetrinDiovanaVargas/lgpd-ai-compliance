import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_chatgpt(question):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em LGPD."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content
