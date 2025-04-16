from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('', views.electronics, name='electronics'),
    # APIs to postcomment
    path("CtegorySort", views.CtegorySort,name="CtegorySort"),
    path("postComment", views.postComment, name="postComment"),
    path('<str:slug>', views.Electronicpost, name='Electronicpost'),
]
