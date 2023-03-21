from django.contrib import admin
from django.urls import path, include
from rango.views import index
from django.conf import settings
from django.conf.urls.static import static
from rango.views import news_list

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('news/', news_list, name='news_list'),
    path('rango/', include('rango.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
