from django.contrib import admin
from .models import Group, Mark, Discipline, User

admin.site.register(User)

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




