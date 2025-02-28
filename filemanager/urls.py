# urls.py
from django.urls import path
from . import views

app_name = 'filemanager'

urlpatterns = [
    path('picker/', views.picker_view, name='picker_view'),
    path('process-picked-file/', views.process_picked_file, name='process_picked_file'),
]