from django.contrib import admin
admin.autodiscover()
from django.urls import path, include
from django.conf import settings	
from django.conf.urls.static import static

urlpatterns = [
    path('', include('cartola.core.urls', namespace='core')),
    path('cartolas/', include('cartola.cartolas.urls', namespace='cartolas')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:	
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)