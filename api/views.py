from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
#from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView

from .models import Account
from .serializers import AccountSerializer

# Create your views here.

class AccountViewSet(viewsets.ModelViewSet):
    serializer_class=AccountSerializer
    queryset = Account.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    #permission_classes = [IsAuthenticatedOrReadOnly]


@api_view(['GET'])
def api_urls(request):
    api_urls={
        'Create': 'api/create/',
        'Read': 'api/read/<str:pk>/',
        'Edit': 'api/edit/<str:pk>/',
        'Delete': 'api/delete/<str:pk>/',

        'account_view': 'api/server/incoming_data',
        'login': 'api/login/',
        'auth': 'api/auth/',
        'gettoken': 'api/gettoken/',
        'Create': 'api/create/',
    }
    return Response(api_urls)


@api_view(['GET'])
# @permission_classes((IsAuthenticated, ))
def account_view(request):
    account = Account.objects.all()
    serializer=AccountSerializer(account, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer = AccountSerializer(data=request.data)
    data={}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "Registered a New Account"
        data['email_id'] = account.email_id
        data['account_id'] = account.account_id
        data['account_name'] = account.account_name
        #data['token'] = Token.objects.get(user=account).key
        return Response(serializer.data)
    else:
        data['response'] = "Error"
        data['error_message'] = "Invalid Data"
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET'])
def read(request, pk):
    account = Account.objects.get(id=pk)
    serializer=AccountSerializer(account, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def edit(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(instance=account, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)
    

@api_view(['DELETE'])
def delete(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()
    if account:
        return Response(f"Successfully deleted id-{pk} ")
    else:
        return Response(f"id-{pk} - delete Failed")


#########################
#Token Generator
###################################
# import string
# import secrets
#
# def generate_token_hex(length: int = 16):
#     return secrets.token_hex(length)
# generate_token_hex()