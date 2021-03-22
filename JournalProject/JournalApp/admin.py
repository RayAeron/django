from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active','date_joined','fk_group')
    list_filter = ('email', 'is_staff', 'is_active','date_joined','fk_group')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','date_joined','fk_group')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active', 'date_joined','fk_group')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User,CustomUserAdmin)

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch_code', 'branch_name', )
    fields = ('name', 'branch_code', 'branch_name', )


@admin.register(Mark)
class MarkAdmin(admin.ModelAdmin):
    list_display = ('date', 'mark', )
    fields = ('date', 'mark', 'fk_student', 'fk_discipline', )

@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name', )
    fields = ('name', 'fk_group', 'fk_teacher')




