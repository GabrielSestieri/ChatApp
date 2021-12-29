from django.urls import path
from .views import index_view, chat_view
urlpatterns = [
    path('', index_view),
    path('chat', chat_view)
]