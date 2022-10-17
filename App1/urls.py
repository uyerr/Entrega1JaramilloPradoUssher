from App1 import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('usuarios/', views.user_list, name='users')
    
    
]
