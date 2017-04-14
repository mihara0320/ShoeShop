from django.contrib.auth.models import User
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'username': None,
        }
        widget=forms.TextInput(attrs={'class':'form-control'})
        fields = ['username', 'email', 'password']
