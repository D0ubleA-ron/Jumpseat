# flights/views.py

from django.shortcuts import render
from .forms import InspirationSearchForm, AIInspirationSearchFrom
from .services.amadeus import get_inspiration
from .services.gpt_query import flight_query_inspiration
from django.http import JsonResponse, HttpResponseBadRequest
from django.conf import settings
from .services.amadeus import get_access_token
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import requests

def inspiration_search_view(request):
    results = None
    error = None

    if request.method == "GET":
        form = InspirationSearchForm(request.GET or None)

        if form.is_valid():
            origin = form.cleaned_data["origin"]
            budget = form.cleaned_data["budget"]
            currency = form.cleaned_data["currency"] or "USD"
            departureDate = form.cleaned_data["departure_date"]
            duration = form.cleaned_data["duration"]

            try:
                results = get_inspiration(origin.upper(), budget, currency.upper(), departureDate, duration)
            except Exception as e:
                error = str(e)
        else:
            form = InspirationSearchForm()

    return render(request, "flights/inspiration_search.html", {
        "form": form,
        "results": results,
        "error": error
    })
def gpt_inspiration_search_view(request):
    results = None
    error = None

    if request.method == "POST":
        form = AIInspirationSearchFrom(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            try:
                results = flight_query_inspiration(query)
            except Exception as e:
                error = str(e)
    else:
        form = AIInspirationSearchFrom()

    return render(request, "flights/gpt_inspiration_search.html", {
        "form": form,
        "results": results,
        "error": error
    })

def remove_query_params(url, params_to_remove):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    for param in params_to_remove:
        query_params.pop(param, None)

    new_query = urlencode(query_params, doseq=True)
    new_url = urlunparse(parsed_url._replace(query=new_query))
    return new_url

def proxy_view(request):
    amadeus_url = request.GET.get("url")
    if not amadeus_url:
        return HttpResponseBadRequest("Missing 'url' parameter.")
    
    cleaned_url = remove_query_params(amadeus_url, ['viewBy', 'duration'])

    try:
        token = get_access_token()  # Ensure you have a function to get the token
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(cleaned_url, headers=headers)
        response.raise_for_status()
        return JsonResponse(response.json(), safe=False)
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)