from django.contrib import admin
from django.urls import include, path

from campeonatos import urls as campeonatos_urls
from core import urls as core_urls

urlpatterns = [
    path("", include(core_urls)),
    path("campeonatos/", include(campeonatos_urls)),
    path("admin/", admin.site.urls),
]
