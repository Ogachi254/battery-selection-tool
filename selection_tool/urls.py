from django.contrib import admin
from django.urls import path,  include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #django admin
    path('admin/', admin.site.urls),

    # user management
    path('accounts/', include ('django.contrib.auth.urls')),

    # local apps
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),
    path('requirements/', include('requirements.urls')),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
