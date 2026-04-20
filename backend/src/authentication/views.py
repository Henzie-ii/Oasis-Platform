from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import CustomTokenObtainPairView, RegisterSerializer, UserSerializer

class RegisterView(generics.CreateAPIView):
    #this allows anyone (even unauthenticated users) to access this view
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       if serializer.is_valid():
           user = serializer.save()
           return Response({
               'user':UserSerializer(user, context=self.get_serializer_context()).data,
               'message':'User created successfully. You can now log in.'
            }, status=status.HTTP_201_CREATED)
        
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(CustomTokenObtainPairView):
    serializer_class = CustomTokenObtainPairView

