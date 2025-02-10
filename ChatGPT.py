import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

import openai
openai.api_key = OPENAI_KEY

def send_to_chatgpt(messages, model="gpt-3.5-turbo"):

  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
  )

message = response.choices[0].message.message.content
messages.append(response.choices[0].message)
return message
