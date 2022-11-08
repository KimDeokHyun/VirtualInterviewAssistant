from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('SK1', views.SK1 ),
    path('SK2', views.SK2  ),
    path('SK3', views.SK3  ),    
]
