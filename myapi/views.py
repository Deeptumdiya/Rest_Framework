from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response    
from . import  serializers
from rest_framework import status
# Create your views here.

class HelloApiView(APIView):
    """Test Api View """
    
    serializer_class = serializers.HelloSerializer
    
    def get(self,request,formate=None):
        """returns a list of api feature """
        an_apiview = [
            'Uses HTTP methods as functions(get,put,patch,update,delete)',
            'is similar to traditional django view',
            'it mapped manually to urls',
        ]
        return Response({'message':
        'Hello', 'an_apiview': an_apiview})
    
    def post(self,request):
        """Hello Message with The name"""
        
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello, {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)