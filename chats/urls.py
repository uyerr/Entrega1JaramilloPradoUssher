from django.urls import include, path
from .views import CreateThread, ListThreads, ThreadView, CreateMessage

urlpatterns = [
    path('messages/', ListThreads.as_view(), name='inbox'),
    path('messages/create-thread/', CreateThread.as_view(), name='create_thread'),
    path('messages/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('messages/<int:pk>/create-message', CreateMessage.as_view(), name='create_message'),
]
