# views.py
import json
import requests
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.conf import settings
import os
from dotenv import load_dotenv
from .models import DriveJSONFile
from django.contrib.auth.decorators import login_required

load_dotenv()

@ensure_csrf_cookie
def picker_view(request):
    """
    Render the Google Picker interface with the existing OAuth token.
    """
    # Get the access token from your existing OAuth2 implementation
    # This could be from the session, a database, or wherever you store it
    access_token = request.session.get('access_token')
    for key, value in request.session.items():
        print(f"{key}: {value}")  # Print each key-value pair on a new line

    print('access_token -> ', access_token)
    # If no token is available, you might want to redirect to authentication
    if not access_token:
        # Redirect or handle as needed based on your OAuth2 implementation
        pass
    
    context = {
        'access_token': access_token,
        'api_key': os.getenv('GOOGLE_API_KEY'),
    }
    
    
    return render(request, 'filemanager/picker.html', context)

@login_required
def process_picked_file(request):
    """
    Process a file picked from Google Drive and save it to the database.
    """
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        data = json.loads(request.body)
        file_id = data.get('fileId')
        file_name = data.get('fileName')
        mime_type = data.get('mimeType')
        
        # Get the access token from your OAuth implementation
        access_token = request.session.get('google_access_token')
        
        if not access_token:
            return JsonResponse({'error': 'Not authenticated'}, status=401)
        
        # For JSON files, fetch the content
        if mime_type == 'application/json':
            file_content = get_file_content(file_id, access_token)
            
            # Save to database
            json_file, created = DriveJSONFile.objects.update_or_create(
                file_id=file_id,
                defaults={
                    'file_name': file_name,
                    'content': file_content
                }
            )
            
            action = 'Created' if created else 'Updated'
            
            return JsonResponse({
                'status': 'success',
                'message': f'{action} file "{file_name}" in database',
                'content': file_content,
                'file_id': json_file.id
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': 'Only JSON files are supported'
            }, status=400)
            
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@login_required
def get_file_content(file_id, access_token):
    """
    Fetch file content from Google Drive using the existing OAuth token.
    """
    url = f"https://www.googleapis.com/drive/v3/files/{file_id}?alt=media"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # For JSON files, return the parsed JSON
        try:
            return response.json()
        except json.JSONDecodeError:
            # If not valid JSON, return as text
            return response.text
    else:
        raise Exception(f"Failed to get file: {response.status_code} - {response.text}")