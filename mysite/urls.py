from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task/', include('api.urls')),
    path('api-auth', include('rest_framework.urls')), # Authorize to access some pages or tools
]
