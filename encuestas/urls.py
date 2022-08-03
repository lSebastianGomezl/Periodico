from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('deportes/', views.deportes, name='deportes'),
    path('contactenos/', views.contacto, name='contacto')
]