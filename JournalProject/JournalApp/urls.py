from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = 'main_url'),
    path('student/', student, name='student_url'),
    path('prepod/', prepod, name='prepod_url'),
    path('prepod/add', MarkAdd.as_view(), name='add_mark_url'),
   #     path('prepod/<int:mark_id>', mark_detail, name='mark_detail_url'),
    path('prepod/<int:mark_id>/update', MarkUpdate.as_view(), name='mark_update_url'),
    path('prepod/<int:mark_id>/delete', MarkDelete.as_view(), name='mark_delete_url'),
]