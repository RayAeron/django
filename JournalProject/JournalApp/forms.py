from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class DisciplineForm(forms.ModelForm):
#     class Meta:
#         model = Discipline
#         fields = ['fk_student', 'name']

#     def __init__(self, *args, **kwargs):
#         super(DisciplineForm, self).__init__(*args, **kwargs)
#         self.fields['fk_student'] = User.objects.filter(fk_group != None )
#         self.fields['fk_discipline'] = 

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['fk_discipline','fk_student','mark',  'date',  ]

        widgets =  {
            'fk_discipline': forms.Select(attrs={'class':'form-select bg-secondary'}),
            'fk_student' : forms.Select(attrs={'class':'form-select bg-secondary'}),
            'mark' : forms.Select(attrs={'class':'form-select bg-secondary'}),
            'date' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }


class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ['fk_discipline','fk_student','mark',  'date',  ]

        widgets =  {
            'fk_discipline': forms.Select(attrs={'class':'form-select bg-secondary'}),
            'fk_student' : forms.Select(attrs={'class':'form-select bg-secondary'}),
            'mark' : forms.Select(attrs={'class':'form-select bg-secondary'}),
            'date' : forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'fk_group')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'fk_group')