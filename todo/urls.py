from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create/', CreateTodo.as_view(template_name='add_task.html'), name='create-task'),
    path('update/<int:pk>/', UpdateTodo.as_view(template_name='update_task.html'), name='update-task'),
    path('delete/<int:pk>/', DeleteTodo.as_view(template_name='delete.html'), name='delete-task'),
    path('search/', search, name='search'),
    
]
