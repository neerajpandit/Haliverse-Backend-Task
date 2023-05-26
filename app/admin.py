from django.contrib import admin

# Register your models here.
from .models import Quiz
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display=['id','question','options','status']