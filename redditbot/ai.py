import os
import pickle
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

# imports the comments as a file

with open('comments.pkl', 'rb') as f:
    commentsR = pickle.load(f)



comments = []
for comment in commentsR:
    comments.append(comments.title)

# feeding comments to groq api to train and reiterate 

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def generator():
    sysprompt = comments
    def create():
        messages=[
            {"role": "system", "content": sysprompt}, ]
        chat_completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages= messages
            )
        return chat_completion
    
    final= create()
    return final

# generates the title
output = generator()
print(output)