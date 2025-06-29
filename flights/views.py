# flights/views.py

from django.shortcuts import render
from .forms import InspirationSearchForm
from .services.amadeus import get_inspiration

def inspiration_search_view(request):
    results = None
    error = None

    if request.method == "GET":
        form = InspirationSearchForm(request.GET or None)

        if form.is_valid():
            origin = form.cleaned_data["origin"]
            budget = form.cleaned_data["budget"]
            currency = form.cleaned_data["currency"] or "USD"

            try:
                results = get_inspiration(origin.upper(), budget, currency.upper())
            except Exception as e:
                error = str(e)
        else:
            form = InspirationSearchForm()

    return render(request, "flights/inspiration_search.html", {
        "form": form,
        "results": results,
        "error": error
    })
