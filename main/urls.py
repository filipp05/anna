from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', main_view, name='main_url'),
    path('hero/<int:hero_id>/', current_hero, name='hero_url')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)