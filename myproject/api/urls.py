from django.urls import path
from . import views
# from .views import TaskListCreate

urlpatterns = [
    path('api',views.getData),
    path('task-list',views.taskList,name="task-list"),
]