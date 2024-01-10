from typing import Any
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .models import Task
from django.contrib.auth.views import LoginView
# to restrict user from accesign the task we will use Mixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


class CustomLoginView(LoginView):
  template_name='baseApp/login.html'
  fields='__all__'
  redirect_authenticated_user=True
  def get_success_url(self):
    return reverse_lazy('tasks')  

class RegisterPage(FormView):
  template_name="baseApp/register.html"
  form_class=UserCreationForm
  redirect_authenticated_user=True
  success_url=reverse_lazy('tasks')

  def form_valid(self, form):
      user=form.save()
      if user is not None:
        login(self.request, user)
      return super(RegisterPage, self).form_valid(form)
  
  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect('tasks')
    return super(RegisterPage, self).get(*args, **kwargs)
  

class taskList(LoginRequiredMixin, ListView):
  model=Task
  context_object_name='tasks'
  template_name='baseApp/task_list.html'

  def get_context_data(self, **kwargs):
    context=super().get_context_data(**kwargs)
    context['tasks']=context['tasks'].filter(user=self.request.user)
    context['count']=context['tasks'].filter(complete=False).count()

    search_input = self.request.GET.get('search-area') or ''
    if search_input:
      context['tasks'] = context['tasks'].filter(title__startswith=search_input)
    context['search_input']=search_input
    return context


class taskDetail(LoginRequiredMixin, DetailView):
  model=Task
  context_object_name='task'
  template_name='baseApp/task_detail.html'

class taskCreate(LoginRequiredMixin, CreateView):
  model=Task
  fields=['title','description','complete'] #for all the fields we are using __all__ we can also use [''] for each view
  success_url=reverse_lazy('tasks') #tasks refers to the urls name 
  
  def form_valid(self, form):
    form.instance.user=self.request.user
    return super(taskCreate, self).form_valid(form)
  
class taskUpdate(LoginRequiredMixin, UpdateView):
  model=Task
  fields=['title','description','complete']
  # fields='__all__' #for all the fields we are using __all__ we can also use [''] for each view
  success_url=reverse_lazy('tasks')

class taskDelete(LoginRequiredMixin, DeleteView):
  model=Task
  context_object_name='task'
  success_url=reverse_lazy('tasks')