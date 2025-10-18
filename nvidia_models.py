from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "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"
)

completion = client.chat.completions.create(
  model="google/gemma-2-9b-it",
  messages=[{"role":"user","content":"how to keep system stable with AI"}],
  temperature=0.2,
  top_p=0.7,
  max_tokens=1024,
  stream=True
)

for chunk in completion:
  if chunk.choices[0].delta.content is not None:
    print(chunk.choices[0].delta.content, end="")

