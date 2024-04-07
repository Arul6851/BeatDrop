from django.urls import path

from . import views

urlpatterns = [
  path('', views.home_view, name='home'),
  path('search/', views.home_view, name='search'),
  path('login/', views.login_view, name='login'),
  path('register/', views.register_view, name='register'),
  path('logout/', views.logout_view, name='logout'),
  path('about/', views.about, name='about'),
  path('watchlater/', views.watch_later_list, name='watchlater'),
  path('addtowatchlater/<int:song_id>/', views.add_to_watch_later, name='addtowatchlater')
]
