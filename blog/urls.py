from django.contrib import admin
from django.urls import path, include
from home.views import home_view
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('post/', include('post.urls', namespace='post')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
