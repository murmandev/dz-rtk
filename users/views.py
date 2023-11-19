from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.save()
            return redirect('login')
        else:
            form = UserRegisterForm()
            return render(request, 'users/register.html', {'form': form})
    
       

class ProfileView(View):
    def get(self, request):
        return render(request, 'users/profile.html')