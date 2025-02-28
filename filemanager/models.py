# models.py
from django.db import models

class DriveJSONFile(models.Model):
    """Model to store JSON data from Google Drive files."""
    file_id = models.CharField(max_length=255, unique=True)
    file_name = models.CharField(max_length=255)
    content = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.file_name