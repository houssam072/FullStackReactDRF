from django.urls import path
from . import views

app = ['services']

urlpatterns = [
    path('services_list/', views.services_list, name = 'services_list'),
    path('service_detailes/<str:slug>', views.service_detailes, name = 'service_detailes'),
]