from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
#User = get_user_model()



class Group(models.Model):
    name = models.CharField(verbose_name='Название группы', max_length=50, unique=True)
    branch_code = models.CharField(verbose_name='Код отделения', max_length=8)
    branch_name = models.CharField(verbose_name='Название отделения', max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    fk_group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Discipline(models.Model):
    name = models.CharField(verbose_name='Название дисциплины', max_length=50)
    fk_group = models.ForeignKey(Group, on_delete=models.SET_NULL, blank=True, null=True)
    fk_teacher = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Учебная дисциплина'
        verbose_name_plural = 'Учебные дисциплины'

class Mark(models.Model):
    date = models.DateField(verbose_name='Дата занятия')

    MARK_CHOISES = (
        (5, 'Отлично'),
        (4, 'Хорошо'),
        (3, 'Удовлетворительно'),
        (2, 'Неудовлетворительно'),
        (1, 'Не явка'),
        (0, 'Не аттестован'),
    )

    mark = models.IntegerField(verbose_name='Оценка', choices=MARK_CHOISES, blank=True, null=True)

    fk_student = models.ForeignKey(User, verbose_name='Студент', on_delete=models.CASCADE)
    fk_discipline = models.ForeignKey(Discipline, verbose_name='Дисциплина', on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}, {}'.format(self.mark, self.fk_discipline)

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'