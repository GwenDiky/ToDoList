from django.urls import path 
from . import views
from .views import TaskCreateView, PersonListView
app_name = "main"
urlpatterns = [
    path('', views.taskList, name="tasks-list"), #name = обратное разрешение интернет-адресов
    path('<int:category_id>/', views.show_category, name="show-category"),
    #Маршруты, содержащие URL-параметры, носят название параметризованных
    path('create', TaskCreateView.as_view(), name="create"),
    path('table', PersonListView.as_view(), name="table"),
]