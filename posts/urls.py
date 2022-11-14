from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post'),
    path('posts/crear/', views.PostCreate.as_view(), name='post_create'),
    path('posts/editar/<int:pk>', views.PostEdit.as_view(), name='post_edit'),
    path('posts/eliminar/<int:pk>', views.PostDelete.as_view(), name='post_delete'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),        
]