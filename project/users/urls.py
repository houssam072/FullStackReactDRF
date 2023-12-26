from django.urls import path
from .views import LoginView, register
from rest_framework_simplejwt.views import (TokenRefreshView)

app = ['users']

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),    
    path('token_refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]