from django.urls import path
from .views import index_view, chat_view, send_message
urlpatterns = [
    path('', index_view),
    path('chat', chat_view),
    path('sendMessage', send_message)
]