from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('golgavzabon/', admin.site.urls),
    path('home/', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts'))
]
