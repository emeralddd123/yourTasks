from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView
from .models import Task
from .forms import TaskUpdateForm, TaskForm 

class HomePageView(TemplateView):
    template_name = 'home.html'

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name= 'tasks'
    template_name = 'tasks_list.html'
    
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context['tasks'].filter(user=self.request.user)
#        context["count"] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__icontains=search_input)

        context['search_input'] = search_input

        return context

    
class NewTaskView(LoginRequiredMixin,View):
    form_class = TaskForm
    initial = {'key': 'value'}
    template_name = 'task_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form.instance.user = self.request.user #to set the owner of the task to the current user
        if form.is_valid():
            form.save()
            return redirect('task:tasks')

        return render(request, self.template_name, {'form': form})


class TaskUpdateView(LoginRequiredMixin,UpdateView):
    model = Task 
    form_class = TaskUpdateForm
    template_name = 'task_update.html'
    success_url = reverse_lazy('task:tasks')
    