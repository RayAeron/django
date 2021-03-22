from django.shortcuts import render, redirect
from .models import Mark, Group, Discipline, User
from .forms import MarkForm
from django.views.generic import View
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    marks = Mark.objects.all()
    context_obj = {'marks': marks}
    return render(request, 'JournalApp\index.html', context=context_obj)


@login_required     
def student(request):
    marks = Mark.objects.filter(fk_student = request.user)
    context_obj = {'marks': marks}
    return render(request, 'JournalApp\mark.html', context=context_obj)

@permission_required('JournalApp.add_mark')
@login_required     
def prepod(request):
    marks = Mark.objects.all()
    
    groups = Group.objects.all()
    form = MarkForm
    context_obj = {'marks': marks, 'groups': groups, 'form':form}
    return render(request, 'JournalApp\mark.html', context=context_obj)

class MarkAdd(View):
    def get(request, self):
        form = MarkForm
        context_obj = {'form':form}
        return render(request, 'JournalApp\mark.html', context=context_obj)

    def post(self, request):
        bound_form = MarkForm(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect('prepod_url')
        return render(request, 'JournalApp\mark.html', context={'form':bound_form})

