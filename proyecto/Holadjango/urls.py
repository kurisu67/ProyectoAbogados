from django.urls import path
from Holadjango import views

urlpatterns = [
    path('', views.index, name="index"),
    path('demandas/', views.demandas, name="demandas"),
    path('informe/', views.informe, name="informe"),
    path('casos/', views.casos, name="casos"),
    path('listas_casos/', views.listas_casos, name="listas_casos"),
    path('listas_demandas/', views.listas_demandas, name="listas_demandas"),
    path('reabririnforme/', views.reabririnforme, name="reabririnforme"),
    path('listas_informes/', views.listas_informes, name="listas_informes"),
    path('modificarinforme/<id>/', views.modificarinforme, name="modificarinforme"),
    path('rest/', views.rest, name="rest"),
    path('ultimademanda/', views.ultimademanda, name="ultimademanda"),
    path('modificarcaso/<id>/', views.modificarcaso, name="modificarcaso"),
    path('reabrircaso/', views.reabrircaso, name="reabrircaso"),
    path('eliminarcaso/<id>/', views.eliminarcaso, name="eliminarcaso"),
    path('reabrirdemanda/', views.reabrirdemanda, name="reabrirdemanda"),
    path('modificardemanda/<id>/', views.modificardemanda, name="modificardemanda"),
    path('eliminardemanda/<id>/', views.eliminardemanda, name="eliminardemanda"),
    path('eliminarinforme/<id>/', views.eliminarinforme, name="eliminarinforme"),
    path('verdemanda/<id>/', views.verdemanda, name="verdemanda"),
    path('verinforme/<id>/', views.verinforme, name="verinforme"),
    path('vercaso/<id>/', views.vercaso, name="vercaso"),
    path('logout/', views.logout_view, name="Logout"),

    
    
]