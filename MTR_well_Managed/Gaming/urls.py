from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('', views.gaming, name='gaming'),
    # APIs to postcomment
    path("postComment", views.postComment, name="postComment"),
    path('<str:slug>', views.Gamingpost, name='Gamingpost'),
]