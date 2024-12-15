from django.db import models

# Create your models here.


class ToDo(models.Model):
    # Define status choices
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    # Fields for the To-Do model
    title = models.CharField(max_length=200)  # To-Do title
    description = models.TextField(blank=True)  # Optional description
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending'  # Default value is 'pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when last updated

    def __str__(self):
        return self.title
