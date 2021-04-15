from django.contrib import admin
from django.urls import path, include
from list import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('list.urls')),
]
