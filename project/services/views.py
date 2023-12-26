from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Service
from .serializers import ServicesSerializers

# Create your views here.
@api_view(['GET', 'POST'])
def services_list(request):
    if request.method == 'GET':
        services = Service.objects.all()
        serializer = ServicesSerializers(services, context = {'request' : request}, many = True)
        context = {
            'data' : serializer.data,
        }
        return Response(context)
    
    elif request.method == 'POST':
        serializer = ServicesSerializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def service_detailes(request, slug):
    try:
        service_detail = Service.objects.get(slug = slug)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ServicesSerializers(service_detail, context = {'request' : request}, many = False)
        context = {
            'data' : serializer.data
        }
        return Response(context)
    
    elif request.method == 'PUT':
        serializer = ServicesSerializers(service_detail, data= request.data, context = {'request':request})
        if serializer.is_valid():
            serializer.save()
            context = {
                'data':serializer.data
            }
            return Response(context)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        service_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)