#pip install python-dotenv
#pip install openai
import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = api_key

#model_lst = openai.Model.list()
model_lst = openai.FineTune.list()
print(model_lst)

