from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'nickname']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4, 
                'placeholder': '請輸入留言', 
                'class': 'form-control'
            })
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['full_name', 'birthday', 'email', 'address', 'profile_picture']