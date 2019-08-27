from django.contrib import admin

# Register your models here.

from .models import weatherdata

admin.site.register(weatherdata)