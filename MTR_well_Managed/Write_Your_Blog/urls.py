from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('', views.Start_Your_Post, name='Start_Your_Post'),
]