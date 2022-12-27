from django.contrib import admin
from eapp.models import *

# Register your models here.
# class catogeryadmin(admin.ModelAdmin):
#    list_display = ("name","images","status")

# admin.site.register(catogery,catogeryadmin)
admin.site.register(catogery)
admin.site.register(product)