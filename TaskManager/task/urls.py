from django.urls import path
from .views import HomePageView, TaskList, NewTaskView


app_name = 'task'
urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('task', TaskList.as_view(), name='tasks'),
    path('add-task', NewTaskView.as_view(), name='add-task'),
]

