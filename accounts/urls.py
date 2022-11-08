from django.urls import path, include
from accounts import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', views.iniciar_sesion, name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'accounts/logout.html'), name = 'logout'),
    path('register/', views.register, name = 'register'),
    path('profile/', views.profile, name='profile'),
    path('profile/editar', views.edit_profile, name="edit_profile"),
    path('profile/password', views.password.as_view(), name="password"),
]
