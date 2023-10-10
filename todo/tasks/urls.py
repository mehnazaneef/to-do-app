from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list"),
    path('updatetask/<str:pk>/', views.updateTask, name="update-task"),
    path('deletetask/<str:pk>/', views.deleteTask, name="delete-task"),
]