from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, JsonResponse
from googleapiclient.discovery import build
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import MediaFileUpload
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
json_file = os.getenv("GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE")

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

def google_login(request) :
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uris": [REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
    )
    flow.redirect_uri = REDIRECT_URI
    authorization_url, _ = flow.authorization_url(prompt="consent")
    return redirect(authorization_url)


# Step 1: Redirect user to Google's OAuth 2.0 server
def google_login(request):
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uris": [REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
    )
    flow.redirect_uri = REDIRECT_URI
    authorization_url, _ = flow.authorization_url(prompt="consent")
    return redirect(authorization_url)

# Step 2: Handle Google callback
def google_callback(request):
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "redirect_uris": [REDIRECT_URI],
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
            }
        },
        scopes=["openid", "https://www.googleapis.com/auth/userinfo.email"],
    )
    flow.redirect_uri = REDIRECT_URI
    flow.fetch_token(authorization_response=request.build_absolute_uri())

    credentials = flow.credentials
    return JsonResponse(
        {"access_token": credentials.token, "refresh_token": credentials.refresh_token}
    )


'''
def upload(response) :
    creds = service_account.Credentials.from_service_account_file(
        json_file,
        scopes=['https://www.googleapis.com/auth/drive']
    )

    drive_service = build('drive', 'v3', credentials=creds)

    folder_metadata = {
        'name' : 'MyFolder'
    }
    file_metadata = {
        'name': 'MyFile.txt',  
        'parents': 'home'  # ID of the folder where you want to upload
    }
    file_path = '/Users/yashbalyan/yashbalyan08/4.pdf'

    media = MediaFileUpload(file_path, mimetype='text/plain')

    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(type(media))
    return HttpResponse(status=200)

def download(response) :
    permission = GoogleDriveFilePermission(
        GoogleDrivePermissionRole.READER,
        GoogleDrivePermissionType.USER,
        ""
    )
    gd_storage = GoogleDriveStorage(permissions=(permission, ))
'''