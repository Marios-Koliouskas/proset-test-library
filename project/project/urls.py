from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),

    #If its not admin/ or __debug__/, search the cores urls
    path("", include("core.urls")),
]
