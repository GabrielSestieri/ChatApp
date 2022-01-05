from django.urls import path
from .views import index_view, add_friend_view
urlpatterns = [
    path('index', index_view),
    path('addFriend', add_friend_view),
]