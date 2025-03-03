from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.contrib.auth.models import User

def home(request):
    return render(request, './backend/home.html')

@login_required
def profile(request):
    # Fetch the user's access token
    access_token = None
    try:
        social_account = SocialAccount.objects.get(user=request.user, provider='google')
        token = SocialToken.objects.filter(account=social_account).first()
        if token:
            access_token = token.token
            request.session['access_token'] = access_token  # Store in session
    except SocialAccount.DoesNotExist:
        pass

    return render(request, './backend/profile.html', {'access_token': access_token})
