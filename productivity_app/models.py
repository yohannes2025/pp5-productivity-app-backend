# models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model that extends the default Django user model."""
    pass


class Task(models.Model):
    """Model for user tasks."""
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.IntegerField(default=1)
    category = models.CharField(max_length=50, blank=True)
    assigned_users = models.ManyToManyField(User, related_name='tasks')
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Attachment(models.Model):
    """Model for task attachments."""
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    created_at = models.DateTimeField(auto_now_add=True)
