from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from account.models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'phone',]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['email','username', 'phone',]


class ProfileChangeForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
