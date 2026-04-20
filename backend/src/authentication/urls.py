from django.urls import path
from .views import RegisterView, LoginView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    #Login sends back the JWT tokens 
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    #Register: Our Cutsom view to create users
    path('register/', RegisterView.as_view(), name='register'),
    #Refresh: Get a new access token when the old one expires
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]