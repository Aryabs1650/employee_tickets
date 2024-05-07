from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("tickets/", include("task1.urls")),
    path("admin/", admin.site.urls),
]
