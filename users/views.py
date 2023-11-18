from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm
from django.views.generic import DetailView
from django.contrib.auth.models import User

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        
    
        if form.is_valid():
            form.save()
            return redirect('login')
        
class ProfileView(View):
    pass