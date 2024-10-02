from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),          # Admin site URL
    path('', include('ex6app.urls')),        # Include app URLs
]
