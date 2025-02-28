from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class GoogleSocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        
        # Get profile info from Google
        if sociallogin.account.provider == 'google':
            user.first_name = data.get('given_name', '')
            user.last_name = data.get('family_name', '')
            user.save()
            
            # Update profile
            profile = user.profile
            profile.full_name = data.get('name', '')
            profile.profile_picture = data.get('picture', '')
            profile.save()
        
        return user

# Then add this to settings.py:
SOCIALACCOUNT_ADAPTER = 'users.adapters.GoogleSocialAccountAdapter'