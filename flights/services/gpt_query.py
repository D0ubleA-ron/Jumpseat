from openai import OpenAI
import json
import os
from flights.services.amadeus import get_inspiration
from datetime import date

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  

def flight_query_structure(query):
    response = client.responses.create(
    prompt={
        "id": "pmpt_686ae690e25c819588a4e13cc068e9df026d04b8eb8a20f6",
        "version": "3",
    },
    input = "Today is " + str(date.today()) + "." + query
    
)
    return(json.loads(response.output[0].content[0].text))

def flight_query_inspiration(query):
    structured_query = flight_query_structure(query)
    print(f"Structured Query: {structured_query}")
    
    origin = structured_query.get("origin")
    budget = structured_query.get("budget")
    currency = structured_query.get("currency") or "CAD"
    departureDate = structured_query.get("departureDate")
    duration = structured_query.get("duration")

    if not origin or not budget:
        raise ValueError("Origin and budget are required fields.")

    try:
        results = get_inspiration(origin.upper(), budget, currency.upper(), departureDate, duration)
        return results
    except Exception as e:
        raise RuntimeError(f"Failed to fetch inspiration: {str(e)}") from e
    
#print(flight_query_inspiration("Find me a flight from Madrid to anywhere under $500, leaving next week sunday"))