from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "accounts"
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name='profile'), 
    path('logout/', views.signout, name='logout')
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)