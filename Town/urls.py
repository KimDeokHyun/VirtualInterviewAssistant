from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index , name = 'index'),
    path('Town1', views.Town1 ),
    path('Town2', views.Town2  ),
    path('Town3', views.Town3  ),    
]
