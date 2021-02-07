from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response    
# Create your views here.

class HelloApiView(APIView):
    """Test Api View """
    
    def get(self,request):
        """returns a list of api feature """
        an_apiview = [
            'Uses HTTP methods as functions(get,put,patch,update,delete)',
            'is similar to traditional django view',
            'it mapped manually to urls',
        ]
        return Response({'message':
        'Hello', 'an_apiview': an_apiview})