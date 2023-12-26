from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication


from .models import Design, DesignImages
from .serializers import DesignSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class DesignList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            design = Design.objects.all()
            serializer = DesignSerializer(design, context = {'request' : request}, many = True)
            context = {
                'data' : serializer.data,
            }
            return Response(context)    
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
