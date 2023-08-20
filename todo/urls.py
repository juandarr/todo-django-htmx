from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]

htmxpatterns = [
    path('create_todo/', views.create_todo, name='create_todo'),
    path('mark_todo/<int:pk>/', views.mark_todo, name='mark_todo'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('edit_todo/<int:pk>/', views.edit_todo, name='edit_todo')
]

urlpatterns += htmxpatterns