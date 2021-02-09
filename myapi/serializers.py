from rest_framework import serializers
from . import  models

class HelloSerializer(serializers.Serializer):
    """serializer a name field for testing APIView."""
    
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile serializer"""
    
    class Meta:
        model = models.UserProfile
        fields = ('id','name','email','password')
        extra_kwargs = {'password':{'write_only':True}}
        
    def create(self,validated_Data):
        """Create and retunr a new user"""
        
        user = models.UserProfile(
            email = validated_Data['email'],
            name = validated_Data['name'])
        
        user.set_password(validated_Data['password'])
        user.save()
        
        return user