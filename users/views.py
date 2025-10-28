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
from .forms import UserRegisterForm

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

# ✅ Class-based login and logout
class LoginView(LoginView):
    template_name = 'users/login.html'

class LogoutView(LogoutView):
    template_name = 'users/logout.html'
