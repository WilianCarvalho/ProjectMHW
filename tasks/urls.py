from django.urls import path

from . import views

#Paginas da Internet
urlpatterns = [
    path('helloword/', views.helloWord),
    path('',views.taskslist, name='Task List')
]
