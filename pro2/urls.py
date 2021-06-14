from django.contrib import admin
from django.urls import path
from django.conf.urls import include # include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')), # chat.urls
]

