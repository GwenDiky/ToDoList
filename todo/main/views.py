from django.shortcuts import render
from django.http import HttpResponse 
from .models import Task, Category
from django.template import loader 
from django.shortcuts import render 
from django.views.generic.edit import CreateView
from .forms import TaskForm
from django.urls import reverse_lazy
# Create your views here.

from django.views.generic import ListView

class PersonListView(ListView):
    model = Task
    template_name = "main/table.html"



def taskList(request): #taskList - наш контролер / вид / представление 
    """
    s = "Список объявлений \r\n\r\n\r\n"
    for task in Task.objects.order_by('-created'):
        s += task.title + ":" + task.created
    return HttpResponse(s, content_type="text/plain; charset=utf-8")
    
    """
    #любой контролер-функция в качестве единственного обязательного параметра (request) принимает экземпляр класса HttpRequest
    #HttpRequest хранит различные сведения о получаемом запросе: запрашиваемый интернет-адрес, данные, полученные от поситителя и т.д
    """
    template = loader.get_template("main/taskList.html")
    tasks = Task.objects.order_by("-created")
    context = {"tasks":tasks}
    return HttpResponse(template.render(context, request))
    """
    #Выполняем рендеринг шаблона, т.е. генерирование на его основе веб-страницы
    #Использум средства более высокого уровня из моделя shortcuts для выполнения рендеринга шаблона
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(request, "main/taskList.html", {"tasks":tasks, "categories":categories})

def show_category(request, category_id):
    tasks = Task.objects.filter(category=category_id)
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {"tasks":tasks, "categories":categories, 
    "current_category":current_category}
    return render(request, 'main/show_category.html', context)

#Класс-контролер
class TaskCreateView(CreateView):
    template_name = 'main/create.html' #Путь к файлу шаблона, создающего страницу с формой
    form_class = TaskForm 
    success_url = reverse_lazy('main:tasks-list') #интернет-адрес для перенаправления после успешного сохранения данных
    #функция reverse_lazy() принимает значение маршрута и значение всех входящих в маршрут URL-параметров
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #Получаем контекст шаблона от метода базового класса
        context['categories'] = Category.objects.all() #Добавляем в него список категорий
        return context
