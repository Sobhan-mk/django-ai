from django.contrib import admin

# plants/admin.py
from django.contrib import admin
from .models import Plants

admin.site.register(Plants)

