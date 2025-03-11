from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # This routes to Django's built-in admin page
    path('', include('library_management_backend.urls')),  # Routes to your app's URLs
]
