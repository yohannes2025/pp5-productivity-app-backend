# # productivity_app/urls.py
# from django.urls import include, path
# from rest_framework.routers import DefaultRouter
# from . import views

# router = DefaultRouter()
# router.register(r'tasks', views.TaskViewSet)
# router.register(r'comments', views.CommentViewSet)

# urlpatterns = [
#     path('', views.home, name='home'),
#     #path('', include(router.urls)),
# ]


# productivity_app/urls.py
from django.urls import path
from . import views
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to the Productivity App!")


urlpatterns = [
    path('', views.home, name='home'),
    path('favicon.ico', lambda request: HttpResponse(
        status=204)),  # Placeholder for favicon
    path('parse/<str:url>/', views.parse_view, name='parse'),
]



