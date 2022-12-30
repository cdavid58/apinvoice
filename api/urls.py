from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^company/', include('company.urls')),
    url(r'^employee/', include('employee.urls')),
    url(r'^client/', include('client.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^invoice_fe/', include('invoice.urls')),
    url(r'^pos/', include('pos.urls')),
    url(r'^data/', include('data.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)