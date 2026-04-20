from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()

class EmailOrUsernameBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **Kwargs):
        try:
            # Allow users to log in with either their username or email
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        
        except UserModel.DoesNotExist:
            return None
        
        #check password and return is user is valid
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        
        return None
