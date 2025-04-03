# # # productivity_app/views.py
# # from django.shortcuts import render
# # # from rest_framework.views import APIView
# # # from rest_framework.response import Response
# # from rest_framework import viewsets, permissions
# # from .models import Task, Comment
# # from .serializers import TaskSerializer, CommentSerializer


# # class TaskViewSet(viewsets.ModelViewSet):
# #     queryset = Task.objects.all()
# #     serializer_class = TaskSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# #     def perform_create(self, serializer):
# #         serializer.save(assigned_to=self.request.user)
        

# # class CommentViewSet(viewsets.ModelViewSet):
# #     queryset = Comment.objects.all()
# #     serializer_class = CommentSerializer
# #     permission_classes = [permissions.IsAuthenticated]

# #     def perform_create(self, serializer):
# #         serializer.save(author=self.request.user)







# from django.views.generic import View
# from django.shortcuts import render
# from rest_framework import viewsets, permissions
# from .models import Task, Comment
# from .serializers import TaskSerializer, CommentSerializer
# from django.db import transaction
# from django.http import HttpResponse
# import logging
# logger = logging.getLogger(__name__)


# class HomeView(View):
#     def get(self, request):
#         return render(request, 'home.html')


# # def home(request):
# #     return render(request, 'home.html')


# # def home(request):
# #     return HttpResponse("Welcome to the Productivity App!")


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         # with transaction.atomic():
#         #     print(f"Authenticated user: {self.request.user}")  # Debugging line
#         #     serializer.save(assigned_to=self.request.user)
#         try:
#             logger.debug(
#                 f"User: {self.request.user}, Data: {self.request.data}")
#             serializer.save(assigned_to=self.request.user)
#         except Exception as e:
#             logger.error(f"Error creating task: {e}")
#             raise

#     def perform_update(self, serializer):
#         with transaction.atomic():
#             serializer.save()


# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         with transaction.atomic():
#             serializer.save(author=self.request.user)

#     def perform_update(self, serializer):
#         with transaction.atomic():
#             serializer.save()


# # productivity_app/views.py
# from django.shortcuts import render


# def home(request):
#     """
#     View function for the home page.
#     """
#     return render(request, 'productivity_app/home.html', {})


# from django.http import HttpResponse



# def home(request):
#     return HttpResponse("Welcome to the Productivity App!")


# productivity_app/views.py
from django.shortcuts import render


def index(request):
    """
    The index view function is the main entry point for your application.
    It handles the logic and rendering of the homepage or the default view.
    """
    # Perform any necessary data processing or logic here
    context = {
        # Add any data or variables you want to pass to the template
    }
    return render(request, 'app_name/index.html', context)

def home(request):
    """
    View function for the home page.
    """
    # Add your logic for the home page here
    return render(request, 'productivity_app/home.html', {})


def parse_view(request, url):
    """
    Parses the provided URL and displays the results.
    """
    try:
        parsed_url = urlparse(url)
        context = {
            'scheme': parsed_url.scheme,
            'netloc': parsed_url.netloc,
            'path': parsed_url.path,
            'params': parsed_url.params,
            'query': parsed_url.query,
            'fragment': parsed_url.fragment,
        }
        return render(request, 'parse.html', context)
    except ValueError:
        # Handle the case where the provided URL is invalid
        return redirect('home')
