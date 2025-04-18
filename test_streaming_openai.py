import sys
import openai

client = openai.OpenAI()

messages = [
  {"role": "system", "content": "you are a math professor"},
  {"role": "user", "content": "count to 10"},
]

completion = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=messages,
    temperature=0,
    stream=True  
)

for chunk in completion:
    content = chunk.choices[0].delta.content
    if content is not None:
        sys.stdout.write(content)
        sys.stdout.flush()
