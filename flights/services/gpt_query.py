from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  

def flight_query(query):
    response = client.responses.create(
    prompt={
        "id": "pmpt_686ae690e25c819588a4e13cc068e9df026d04b8eb8a20f6",
        "version": "1",
    },
    input = query
    
)
    return(json.loads(response.output[0].content[0].text))
