from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('golgavzabon/', admin.site.urls),
    path('home/', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('plant_leaf_deseases_detector/', include('PLDdetector.urls', namespace='PLDdetector')),
    path('my_plants/', include('my_plants.urls', namespace='my_plants')),
    path('qa/', include('qa.urls', namespace='qa'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


