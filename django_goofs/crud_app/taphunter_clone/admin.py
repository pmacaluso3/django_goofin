from django.contrib import admin

# Register your models here.
from .models import Beer, Bar
admin.site.register(Beer)
admin.site.register(Bar)
