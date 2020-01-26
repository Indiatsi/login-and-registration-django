from django import forms
from login.models import CustomUser

class SignUp(forms.Form):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    re_password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_password(self):
            password = self.cleaned_data.get('password')
            re_password = self.cleaned_data.get('re_password')
            if password and re_password and password == re_password:
                return re_password
            raise forms.ValidationError("Passwords don't match")
    
    def clean_email(self):
            email = self.cleaned_data['email'].strip()
            try:
                CustomUser.objects.get(email__iexact=email)
                raise forms.ValidationError('This email already exists')
            except CustomUser.DoesNotExist:
                return email