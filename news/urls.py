from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('daily/', include('daily.urls')),
    path('admin/', admin.site.urls),
]