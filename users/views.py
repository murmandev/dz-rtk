from django.shortcuts import render, redirect
from django.views import View

from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from .forms import UserUpdateForm, AccountUpdateForm

from django.contrib.auth import authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Account




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            group = Group.objects.get(name="ReadOnly")
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            authenticate(username=username, password=password)
            
            acc = Account(user.id)
            acc.save()
            messages.success(request, f'{username} был зарегистрирован!')
            return redirect('login')
    else:
        form = UserCreationForm()
        context = {'form': form}
    return render(request, 'users/register.html', context)



def profile_show(request):
    context = dict()
    context['nav_bar_color'] = 'profile'
    return render(request, 'users/profile.html', context)

def profile_update(request):
    user = request.user
    account = Account.objects.filter(user=user).first()
    if account is None:
        account = Account(user.id)
        account.save()
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=account)

        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            messages.success(request,"Профиль успешно обновлен")
            return redirect('profile')
        else:
            messages.success(request,"Что то пошло не так")
    else:
        context = {'account_form':AccountUpdateForm(instance=account),
                   'user_form':UserUpdateForm(instance=user)}
    return render(request,'users/profile_edit.html',context)

    
