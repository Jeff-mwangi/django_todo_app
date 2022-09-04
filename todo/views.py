from email import message
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from todo.models import Todo

@login_required
def home(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'home.html', context)


class ListTodo(ListView):
    model = Todo
    template_name = 'home.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.all()

class CreateTodo(CreateView):
    model = Todo
    fields = ['title']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateTodo(UpdateView):
    model = Todo
    fields = ['title', 'completed']
    template_name = 'home.html'
    success_url= '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class DeleteTodo(DeleteView):
    model = Todo
    template_name = 'home.html'
    success_url= '/'

    def test_func(self):
        return self.request.user == self.get_object().author

def search(request):
    if request.method == 'POST':
        search_term = request.POST['search']
        search_results = Todo.objects.filter(title__icontains=search_term)
        context = {
            'search_term': search_term,
            'search_results': search_results
        }
        return render(request, 'search.html', context)
    

