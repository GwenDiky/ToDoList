from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model): #Вторичная
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Пользователь")
    title = models.CharField(max_length=200, verbose_name="Что нужно сделать")
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Оцените задачу по уровню важности")
    #Первым параметром конструктуру этого класса передается строка с именем класса первичной модели, поскольку вторичная модель у нас объявлена раньше первичной
    #все поля модели обязательны к заполнению. следовательно, добавить новое обязателное к заполнению поле в модель, которая уже содержит записи,
    #нельзя — сама СУБД откажется это делать и выведет сообщение об ошибке
    #нам придется пометить поле category как необязательное, присвоим параметру null значение True
    description = models.TextField(null=True, blank=True, verbose_name="Описание")
    complete = models.BooleanField(default=False, verbose_name="Действие завершено?")
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    def __str__(self):
        return self.title 
    class Meta:
        verbose_name_plural = "Задачи" #Название модели во множетсвенном числе
        verbose_name = "Задача" #Название модели в единственном числе
        ordering = ['-created']

class Category(models.Model): #Первичная
    name = models.CharField(max_length=200, db_index=True, verbose_name="Оцените задачу по уровню важности")
    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "Категория"
        ordering = ["name"]
    def __str__(self):
        return self.name