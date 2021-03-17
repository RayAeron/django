from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'main_url'),
    path('student/', student, name='student_url')
]