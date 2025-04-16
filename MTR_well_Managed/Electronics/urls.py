from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('', views.electronics, name='electronics'),
    path("CtegorySort", views.CtegorySort,name="CtegorySort"),
    # APIs to postcomment
    path("postComment", views.postComment, name="postComment"),
    path('<str:slug>', views.Electronicpost, name='Electronicpost'),
]
