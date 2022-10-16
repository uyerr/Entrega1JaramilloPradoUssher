from App1 import views
from django.urls import path
from importlib.resources import path


urlpatterns = [
    path('home/', views.home),   
]
