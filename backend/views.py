from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, './backend/home.html')

@login_required
def profile(request):
    return render(request, './backend/profile.html')