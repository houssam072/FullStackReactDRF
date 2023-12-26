from django.urls import path
from .views import DesignList
app_name = 'design'

urlpatterns = [
    path('design_list/',DesignList.as_view(), name = 'design_list'),
]