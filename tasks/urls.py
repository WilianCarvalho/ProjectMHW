from django.urls import path

from . import views

#Paginas da Internet
urlpatterns = [
    path('helloword/', views.helloWord),
    path('',views.homepage, name='Homepage'),
    path('yourName/<str:name>', views.yourName, name='yourName' ),
    #path("homepage", views.homepage, name="Pagina Inicial")
]
