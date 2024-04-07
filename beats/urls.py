from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.home_view, name='search'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
