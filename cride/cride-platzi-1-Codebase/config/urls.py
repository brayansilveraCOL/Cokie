"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from cride.views import index

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    path('', index),
    path('', include(('cride.pharma.urls', 'circles'), namespace='circle')),
    path('', include(('cride.users.urls', 'users'), namespace='user')),
    path('', include(('cride.rides.urls', 'rides'), namespace='rides')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
