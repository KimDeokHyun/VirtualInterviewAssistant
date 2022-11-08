from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('Edu1', views.Edu1 ),
    path('Edu2', views.Edu2 ),
    path('Edu3', views.Edu3 ),    
]
