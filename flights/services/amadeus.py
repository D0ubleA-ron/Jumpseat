import requests
import os

def get_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    payload = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('AMADEUS_CLIENT_ID'),
        'client_secret': os.getenv('AMADEUS_CLIENT_SECRET')
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    response = requests.post(url, data=payload, headers=headers)
    response.raise_for_status()  # Raise error if failed
    return response.json()['access_token']

def get_inspiration(origin, budget, currency='CAD', departureDate=None, duration=None):
    endpoint = "https://test.api.amadeus.com/v1/shopping/flight-destinations"
    headers = {"Authorization": f"Bearer {get_access_token()}"}
    
    params = {
        "origin": origin,
        "maxPrice": budget,
        "currency": currency,
        "departureDate": departureDate,
        "duration": duration
    }
    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()
    
    if 'data' in data:
        filtered_data = [
            item for item in data['data']
            if float(item['price']['total']) <= float(budget)
        ]
        unique_destinations = {}
        for item in filtered_data:
            destination = item['destination']
            price = float(item['price']['total'])
            
            if (destination not in unique_destinations or 
                price < float(unique_destinations[destination]['price']['total'])):
                unique_destinations[destination] = item
    data['data'] = list(unique_destinations.values())
    print(f"Filtered data: {data['data']}")
    return data
