from django.urls import path, include
from accounts import views
urlpatterns = [
    path('login/', views.login, name = 'login'),
]
