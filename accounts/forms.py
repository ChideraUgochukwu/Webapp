from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'avatar', 'interests']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3}),
            'interests': forms.TextInput(attrs={'placeholder': 'e.g. Math, Science, Art'})
        }
