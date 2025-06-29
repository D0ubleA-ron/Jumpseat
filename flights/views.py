# flights/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.amadeus import get_inspiration

class InspirationView(APIView):
    def get(self, request):
        origin = request.query_params.get("origin")
        budget = request.query_params.get("budget")

        if not origin or not budget:
            return Response({"error": "origin and budget are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            data = get_inspiration(origin, budget)
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

