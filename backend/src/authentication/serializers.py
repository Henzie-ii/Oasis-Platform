from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_pic']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']

    def create (self, validated_data):
        user = CustomUser.objects.create_user(
                username=validated_data['username'],
                email=validated_data['email'],
                password=validated_data['password']
            )
        return user
        
class CustomTokenObtainPairView(TokenObtainPairSerializer):
    def validate(self,attrs):
        #the base validate method handles the actual authentication and token generation
        data = super().validate(attrs)

        #add custom JSON data to get login response
        data['user'] = {
            'username': self.user.username,
            'email': self.user.email,
            'bio': self.user.bio,
        } 
        return data 
