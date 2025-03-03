# Assignment-Enfund

## Overview
Assignment-Enfund is a Django-based project that integrates Google Picker API for file selection, Google OAuth for authentication, and WebSockets for real-time interactive chat. The project provides a seamless experience for users to authenticate via Google, select and manage files from Google Drive, and engage in real-time communication.

## Features

- **Google OAuth Authentication**: Secure user login using Google accounts.
- **Google Picker API Integration**: Allows users to select and manage files from their Google Drive.
- **WebSockets-powered Chat**: Real-time messaging for an interactive user experience.
- **Django Backend**: Manages user authentication, file handling, and chat functionalities.
- **Responsive UI**: HTML templates with dynamic interactions.

## Tech Stack

- **Backend**: Django, Django Channels (for WebSockets)
- **Frontend**: HTML, JavaScript, Google Picker API
- **Authentication**: Google OAuth 2.0
- **Database**: SQLite (or PostgreSQL if configured)
- **WebSockets**: Django Channels for real-time chat

## Installation & Setup

### 1. Clone the Repository
```bash
 git clone https://github.com/yashbalyan08/Assignment-enfund.git
 cd Assignment-enfund
```

### 2. Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Configure Google OAuth & Picker API
1. Register your application on [Google Developer Console](https://console.developers.google.com/)
2. Enable Google Drive API & Picker API
3. Obtain OAuth credentials (Client ID & Secret) and update them in the Django settings.
4. You need to create your own Google OAuth credentials, as they are unique to each project.

### 4. Run Database Migrations
```bash
python manage.py migrate
```

### 5. Start the Django Server
```bash
daphne -b 127.0.0.1 -p 8000 config.asgi:application
```

### 6. Running WebSocket Server
Ensure Django Channels is correctly configured and run the WebSocket server to enable real-time chat.

## Usage

- **Login with Google**: Users authenticate using their Google account.
- **File Management**: Select files from Google Drive using the Picker API.
- **Real-time Chat**: Engage in interactive messaging via WebSockets.

## Folder Structure

```
Assignment-enfund/
│── backend/         # Django project configuration
│── chat/            # WebSockets chat implementation
│── filemanager/     # Handles Google Picker file selections
│── templates/       # Frontend HTML templates
│── utils/           # Helper functions and utilities
│── manage.py        # Django management script
│── requirements.txt # Project dependencies
│── token.json       # Stores OAuth tokens (if applicable)
│── .gitignore       # Ignored files and folders
```
