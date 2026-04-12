from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView

urlpatterns = [
    #Login sends back the JWT tokens 
    path('login/', TokenObtainPairView.as_view(), name='tokeen_obtain_pair'),
    #Refresh: Get a new access token when the old one expires
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #Register: Our Cutsom view to create users
    path('register/', RegisterView.as_viwe(), name='register'),
]