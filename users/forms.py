from django import forms

from .models import User


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'type': 'password'
    }))

class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'email', 'username', 'password', 'tel', 'is_admin']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'last_name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'id': 'email'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'username'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control', 'id': 'password'
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'tel'
            }),
            'is_admin': forms.RadioSelect(attrs={'id': 'is_admin'}),
        }


class ModifyUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'email', 'password', 'tel', 'is_admin']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'first_name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'last_name'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'address'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 'id': 'email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control', 'id': 'password'
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'tel'
            }),
            'is_admin': forms.RadioSelect(attrs={'id': 'is_admin'}),
        }
