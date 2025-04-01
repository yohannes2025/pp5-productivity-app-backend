# productivity_app/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    #path('', include(router.urls)),
]