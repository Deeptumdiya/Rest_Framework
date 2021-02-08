from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response    
from . import  serializers
from . import models
from rest_framework import status
from rest_framework import viewsets
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
        
    def put(self,request,pk=None):
        return Response({'method':'put'})
    
    def patch(self,request, pk=None):
        return Response({'method':'patch'})
    
    def delete(self,request, pk=None):
        return Response({'method':'delete'})
    
class HelloViewset(viewsets.ViewSet):
    """Test Api Viewset"""
    
    def list(self,request):
        a_viewset = [
        'User actioins [list, create, retrive,Update,patrtial_update]',
        'Automatically maps to urls Routers',
        'Provide more funtionallity with less code'
        ]
    
        return Response({'Message':'Hello','a_viewset':a_viewset})
    
    def create(self,request):
        """Create a new message with hello"""
        
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.request.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http.method': 'GET'})
    
    def update(self, request, pk=None):
        """Update an object"""
        return Response({'http.method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """Update an object"""
        return Response({'http.method':'PATCH'})
    
    def destroy(self,request, pk=None):
        """Update an object"""
        return Response({'http.method':'DELETE'})
    
    
class UserProfileViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()