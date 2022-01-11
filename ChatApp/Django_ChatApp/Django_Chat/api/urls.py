from django.urls import path
from .views import index_view, add_friend_view, login_user
urlpatterns = [
    path('index', index_view),
    path('addFriend', add_friend_view),
    path('login', login_user)
]