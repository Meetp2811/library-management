import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_management.settings')  # Ensure this points to settings.py

application = get_wsgi_application()
