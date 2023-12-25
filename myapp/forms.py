from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "userID", "email", "password1", "password2"]


class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
