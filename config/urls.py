from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('amenities/', include('amenities.urls')),
    path('room/', include('rooms.urls')),
    path('blog/', include('blog.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('contact/', include('contact.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)