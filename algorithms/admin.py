from django.contrib import admin

# Register your models here.
from .models import Type, Algorithm

admin.site.register(Type)
admin.site.register(Algorithm)
