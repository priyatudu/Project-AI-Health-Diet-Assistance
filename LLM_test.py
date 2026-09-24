import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
HF_Token =os.getenv("HF_TOKEN")



client = OpenAI(base_url="https://router.huggingface.co/v1",api_key = HF_Token)
response = client.chat.completions.create(model ="openai/gpt-oss-120b",
                               messages = [{
                                   "role":"user",
                                   "content": "what is good source of protine in vegitable",
                               }])

answ =print(response.choices[0].message.content)
print(answ)

# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# response = client.chat.completions.create(
#     model="openai/gpt-oss-120b",
#     messages=[{"role": "user", 
#                "content": "what is the good protin source for vegiterian"}]
# )
# answ =print(response.choices[0].message.content)
# print(answ)