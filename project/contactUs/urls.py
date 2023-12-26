from django.urls import path
from . import views

app_name = 'contactUs'

urlpatterns = [
    path('send_email/', views.send_email, name='send_email')
]