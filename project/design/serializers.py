from rest_framework import serializers
from .models import Design, DesignImages
class DesignImagreSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignImages
        fields = '__all__'

class DesignSerializer(serializers.ModelSerializer):
    images = DesignImagreSerializer(many = True, read_only = True)
    upload_image = serializers.ListField(
        write_only = True
    )
    class Meta:
        model = Design
        fields = ['id', 'title', 'image_bio', 'created_at', 'images', 'upload_image']

    
    def create(self, validated_data):
        uploaded_images = validated_data.pop('uplload_image')
        design = Design.objects.create(**validated_data)

        for image in uploaded_images:
            DesignImages.objects.create(design = design, images = image)

        return design
