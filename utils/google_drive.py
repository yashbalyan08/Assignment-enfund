# utils/google_drive.py
import json
import requests
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from io import BytesIO

def get_drive_service(access_token):
    """Create a Google Drive service using an access token."""
    credentials = Credentials(access_token)
    return build('drive', 'v3', credentials=credentials)

def get_file_content(access_token, file_id):
    """Download a file's content from Google Drive."""
    drive_service = get_drive_service(access_token)
    
    # Get the file metadata to check type
    file_metadata = drive_service.files().get(fileId=file_id).execute()
    mime_type = file_metadata.get('mimeType', '')
    
    # Download the file
    request = drive_service.files().get_media(fileId=file_id)
    file_content = BytesIO()
    downloader = MediaIoBaseDownload(file_content, request)
    
    done = False
    while not done:
        status, done = downloader.next_chunk()
    
    # Reset the file pointer to the beginning
    file_content.seek(0)
    
    # For JSON files, parse the content
    if mime_type == 'application/json':
        try:
            return json.loads(file_content.read().decode('utf-8'))
        except json.JSONDecodeError:
            return {"error": "Invalid JSON format"}
    
    # For other file types, return the raw content
    return file_content.read()