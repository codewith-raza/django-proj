
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from . import settings
admin.site.site_header="My Shopify Admin "
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myshopify.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
