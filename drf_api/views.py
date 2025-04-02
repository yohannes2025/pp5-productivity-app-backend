# drf_api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE, JWT_AUTH_SAMESITE,
)


@api_view()
def root_route(request):
    return Response({
        "message": "Welcome to drf_api productivity app"
    })
