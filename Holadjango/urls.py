from django.urls import path
from Holadjango import views

urlpatterns = [
    path('', views.index, name="Index"),
    path('Serv2/', views.serv2, name="Serv2"),
]