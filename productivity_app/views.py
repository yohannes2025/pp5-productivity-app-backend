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


def home(request):
    """
    View function for the home page.
    """
    # Add your logic for the home page here
    return render(request, 'productivity_app/home.html', {})
