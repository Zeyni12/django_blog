# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
# def profile_view(request):
#     return render(request, 'users/profile.html', {'user': request.user, 'name': 'Zeyneb'})

# def about(request):
#     return render(request,'blog/about.html',{'title':'About Page'}) 

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserRegisterForm , UserUpdateForm,ProfileUpdateForm 
from django.contrib import messages

# ✅ Register view
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# ✅ Profile view
@login_required
def profile(request):
    return render(request, 'users/profile.html')

def profile_update(request):
        if request.method == 'POST':
           u_form = UserUpdateForm(request.POST, instance=request.user)
           p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
           if u_form.is_valid() and p_form.is_valid():
              u_form.save()
              p_form.save()
              messages.success(request, f'Your Profile was Updated!!')
              return redirect('profile')
        else:
           u_form = UserUpdateForm(instance=request.user)
           p_form = ProfileUpdateForm(instance=request.user.profile)
            
        context = {
         'u_form': u_form,
         'p_form': p_form
        
        }
        return render(request, 'users/profile_update.html', context)


# # ✅ Class-based login and logout
# class LoginView(LoginView):
#     template_name = 'users/login.html'

# class LogoutView(LogoutView):
#     template_name = 'users/logout.html'
