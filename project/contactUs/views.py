from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_email(request):
    print('1')
    if request.method == 'POST':
        print('2')
        name = request.data.get('name')
        message = request.data.get('message')
        mobile_number = request.data.get('phone')
        sender_email = request.data.get('email')
        print('3')


        subject = f'new contact message from{name}'
        message += f'\n mobile phone : {mobile_number}\n Email : {sender_email}'
        admin_email = ['houssamsaleh072@gmail.com']
        print('4')

        send_email(subject, message, sender_email, admin_email)
        print('5')

        return Response(status= status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)