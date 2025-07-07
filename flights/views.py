# flights/views.py

from django.shortcuts import render
from .forms import InspirationSearchForm, AIInspirationSearchFrom
from .services.amadeus import get_inspiration
from .services.gpt_query import flight_query_inspiration

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