from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('post/<str:pk>', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    path('profile/', views.profile, name='profile'),
]