from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('supersecret/', admin.site.urls),
    path('blog/',include('apps.blog.urls'),name='blog-app'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
