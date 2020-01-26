from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms

# Create your views here.
def home(request):
    return render(request , 'home.html')
    
def signup(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            messages.error(request, 'This form is invalid')
    else:
        form = forms.SignUp()
        return render(request, 'registration/signup.html', {'form' : form})