from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'main_url'),
    path('student/', student, name='student_url'),
    path('prepod/', prepod, name='prepod_url'),
    path('prepod/add', MarkAdd.as_view(), name='add_mark_url'),
]