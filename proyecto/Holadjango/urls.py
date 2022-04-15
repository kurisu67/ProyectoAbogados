from django.urls import path
from Holadjango import views

urlpatterns = [
    path('', views.index, name="index"),
    path('demandas/', views.demandas, name="demandas"),
    path('informe/', views.informe, name="informe"),
    path('casos/', views.casos, name="casos"),
    path('listas/', views.listas, name="listas"),
    path('rest/', views.rest, name="rest"),
    path('ultimademanda/', views.ultimademanda, name="ultimademanda"),
    path('nombre', views.get_nombre, name="nombre")
]