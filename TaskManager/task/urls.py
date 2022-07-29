from django.urls import path
from .views import HomePageView, TaskList, NewTaskView, TaskUpdateView, TaskDeleteView,CompletedTaskList,TodayTaskList


app_name = 'task'
urlpatterns = [
    path('',HomePageView.as_view(), name='home'),
    path('task', TaskList.as_view(), name='tasks'),
    path('completed-task', CompletedTaskList.as_view(), name='completed-task'),
    path('today-task', TodayTaskList.as_view(), name='today-task'),    
    path('add-task', NewTaskView.as_view(), name='add-task'),
    path('update-task/<slug:slug>/', TaskUpdateView.as_view(), name='update-task'),
    path('delete-task/<slug:slug>/', TaskDeleteView.as_view(), name='delete-task'),

]
