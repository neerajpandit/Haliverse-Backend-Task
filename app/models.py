from django.db import models

# Create your models here.
class Quiz(models.Model):
    QUESTION_STATUS_CHOICES = [
        ('inactive', 'Inactive'),
        ('active', 'Active'),
        ('finished', 'Finished'),
    ]

    question = models.TextField()
    options = models.JSONField()
    right_answer = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=QUESTION_STATUS_CHOICES, default='inactive')

    def __str__(self):
        return self.question