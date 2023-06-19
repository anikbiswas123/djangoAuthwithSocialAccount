
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Account.url')),
    path('accounts/', include('allauth.urls')),
]
