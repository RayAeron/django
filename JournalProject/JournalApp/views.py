from django.shortcuts import render
from .models import Mark, Group, Discipline, User

def index(request):
    marks = Mark.objects.all()
    context_obj = {'marks': marks}
    return render(request, 'JournalApp\index.html', context=context_obj)

def student(request):
    marks = Mark.objects.filter(fk_student = request.user)
    context_obj = {'marks': marks}
    return render(request, 'JournalApp\index.html', context=context_obj)