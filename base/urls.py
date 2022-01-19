from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name="home"),
   path('delete/<list_id>', views.delete, name="delete"),
path('TaskUndone/<list_id>', views.TaskUndone, name="TaskUndone"),
path('TaskDone/<list_id>', views.TaskDone, name="TaskDone"),
]