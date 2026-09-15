from dotenv import load_dotenv
import os
load_dotenv()

keys = os.getenv("OPENAI_API_KEY")
print(keys)
