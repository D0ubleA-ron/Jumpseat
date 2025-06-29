
from django.urls import path
from .views import InspirationView

urlpatterns = [
    path('inspiration/', InspirationView.as_view(), name='inspiration'),
]