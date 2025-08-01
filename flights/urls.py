
from django.urls import path
from .views import inspiration_search_view, gpt_inspiration_search_view, flight_offers_view

urlpatterns = [
    path('inspiration/', inspiration_search_view, name='inspiration'),
    path('gpt-inspiration/', gpt_inspiration_search_view, name='gpt_inspiration'),
    path("flight-offers/", flight_offers_view, name="flight_offers")
]