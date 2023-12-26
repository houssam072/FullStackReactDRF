from rest_framework import serializers
from .models import Service

class ServicesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('pk', 'service_name', 'service_bio', 'service_disc', 'service_logo', 'slug')