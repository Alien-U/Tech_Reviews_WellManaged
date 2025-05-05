from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [    
    path("", views.AccountPage, name="AccountPage"),
    path('signup', views.handleSignup,name="handleSignup"),
    path('login', views.handleLogin,name="handleLogin"),
    path('logout/', views.handleLogout,name="handleLogout"),
    path('Profile/', views.ProfilePage,name="ProfilePage"),
    path('deleteElectpost/<slug:slug>', views.deleteElectpost, name='deleteElectpost'),
    path('deleteGamepost/<slug:slug>', views.deleteGamepost, name='deleteGamepost'),
    path('deleteSoftpost/<slug:slug>', views.deleteSoftpost, name='deleteSoftpost'),
]