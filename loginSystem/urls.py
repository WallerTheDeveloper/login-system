from django.urls import path
from loginSystem import views

urlpatterns = [
    path('', views.mainPage, name = 'mainPage'),
    path('login/', views.loginPage, name="loginPage"),
    path('signout/', views.logout, name="logoutPage"),
    path('register/', views.registerUser, name="registerPage")
]