from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login') 
