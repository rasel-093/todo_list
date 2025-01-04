from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect


from .models import Task

# Create your views here.
class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')  # Replace 'home' with the name of your desired redirect URL pattern


class CustomLoginView(LoginView):
     template_name = 'base/login.html'
     fields = '__all__'
     redirect_authenticated_user = True

     def get_success_url(self):
          return reverse_lazy('tasks')
     
class TaskList(LoginRequiredMixin, ListView):
     model = Task
     context_object_name = 'tasks'

class TaskDetail(LoginRequiredMixin, DetailView):
     model = Task
     context_object_name = 'task'
     template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
     model = Task
     fields = '__all__' #['title', 'description']
     success_url = reverse_lazy('tasks')

class TaskUpdate(LoginRequiredMixin, UpdateView):
     model = Task
     fields = '__all__'
     success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin, DeleteView):
     model = Task
     context_object_name = 'task'
     success_url = reverse_lazy('tasks')
     template_name = 'base/task_confirm_delete.html'