from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})

def about(request):
    return render(request,'blog/about.html',{'title':'About Page'}) 